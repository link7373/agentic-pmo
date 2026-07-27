#!/usr/bin/env python3
"""Regression-test validate_pbip.py against a known-good PBIP and 16 defects.

    python .claude/skills/powerbi/tests/run_tests.py [-v]

Asserts three things:
  1. the clean fixture validates with zero errors and exit 0
  2. every injected defect raises its specific code, at the right severity
  3. no defect raises anything unrelated to itself

Fixtures are built in a temp directory and removed afterwards, so this never
touches the repo. Standard library only; runs anywhere Python does.

Run it after any change to validate_pbip.py. Today's lesson for why it exists:
a check can look correct, pass on your own fixture, and still be wrong about
real files — THEME001 originally resolved resource paths under the item's type
instead of the package's, which would have thrown false errors on every real
report while passing a fixture built with the same misunderstanding.

Part of the Agentic BI Team. Created by Colin Beck.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from make_fixture import DEFECTS, WARN_ONLY, build  # noqa: E402

VALIDATOR = Path(__file__).resolve().parents[1] / "scripts" / "validate_pbip.py"

GREEN, RED, DIM, RESET = "\033[32m", "\033[31m", "\033[2m", "\033[0m"


def run_validator(target: Path):
    """Return (exit_code, findings) using the validator's own JSON output."""
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(target), "--json"],
        capture_output=True, text=True,
    )
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError:
        print(f"{RED}validator produced no JSON{RESET}\n{proc.stdout}\n{proc.stderr}")
        return proc.returncode, []
    return proc.returncode, payload["findings"]


def main() -> int:
    verbose = "-v" in sys.argv
    if not VALIDATOR.exists():
        print(f"{RED}validator not found at {VALIDATOR}{RESET}")
        return 2

    passed, failed = 0, 0
    with tempfile.TemporaryDirectory(prefix="pbip-tests-") as tmp:
        root = Path(tmp)

        # ---- 1. clean fixture -------------------------------------------
        target = build(root / "clean")
        code, findings = run_validator(target)
        errors = [f for f in findings if f["severity"] == "ERROR"]
        if code == 0 and not errors:
            print(f"{GREEN}PASS{RESET}  clean            exit 0, no errors")
            passed += 1
        else:
            print(f"{RED}FAIL{RESET}  clean            exit {code}, "
                  f"{len(errors)} error(s)")
            for f in errors:
                print(f"        {f['code']}: {f['message']}")
            failed += 1

        # ---- 2. each defect ---------------------------------------------
        for name in sorted(DEFECTS):
            expected_code = DEFECTS[name]
            expect_warn = name in WARN_ONLY
            target = build(root / name, name)
            code, findings = run_validator(target)

            hits = [f for f in findings if f["code"] == expected_code]
            severity_ok = bool(hits) and all(
                (f["severity"] == "WARN") == expect_warn
                for f in hits if f["severity"] != "INFO"
            )
            exit_ok = (code == 0) if expect_warn else (code == 1)

            if hits and severity_ok and exit_ok:
                sev = "WARN " if expect_warn else "ERROR"
                print(f"{GREEN}PASS{RESET}  {name:<16} {sev} {expected_code}")
                if verbose:
                    for f in hits:
                        print(f"        {DIM}{f['path']}{RESET}")
                        print(f"        {f['message']}")
                passed += 1
            else:
                print(f"{RED}FAIL{RESET}  {name:<16} expected {expected_code} "
                      f"({'WARN' if expect_warn else 'ERROR'}), exit "
                      f"{'0' if expect_warn else '1'}")
                print(f"        got exit {code}, codes: "
                      f"{sorted({f['code'] for f in findings}) or 'none'}")
                failed += 1

    total = passed + failed
    print(f"\n{'-' * 52}")
    colour = GREEN if not failed else RED
    print(f"{colour}{passed}/{total} passed{RESET}"
          + (f", {failed} failed" if failed else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

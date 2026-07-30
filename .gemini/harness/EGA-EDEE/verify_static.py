#!/usr/bin/env python3
# Copyright 2026 Google LLC

import sys
import json
import subprocess
from pathlib import Path

def main():
    repo_root = Path("/Users/ksprashanth/code/github/skills-extract-human-voice")
    script_path = repo_root / "skills" / "extract-human-voice" / "scripts" / "extract_voice.py"
    test_path = repo_root / "tests" / "test_extract_voice.py"

    errors = []

    if not script_path.exists():
        errors.append(f"Script file missing: {script_path}")
    else:
        content = script_path.read_text(encoding="utf-8")

        # Check 1: SQLite URI mode
        if "mode=ro" not in content and "immutable=1" not in content:
            errors.append("SQLite connection missing read-only URI mode ('mode=ro')")

        # Check 2: Expanded secret patterns
        required_patterns = ["sk-ant", "sk-", "AKIA", "github_pat_", "glpat-"]
        for pat in required_patterns:
            if pat not in content:
                errors.append(f"Missing secret pattern in PII_PATTERNS: '{pat}'")

        # Check 3: Cross-platform path resolution
        if "platform.system()" not in content:
            errors.append("Missing cross-platform OS path resolution ('platform.system()')")

        # Check 4: Verbose CLI flag
        if "--verbose" not in content or "argparse" not in content:
            errors.append("Missing '--verbose' CLI argument parser")

    # Check 5: Unit test file exists and passes
    if not test_path.exists():
        errors.append(f"Unit test file missing: {test_path}")
    else:
        res = subprocess.run([sys.executable, "-m", "unittest", str(test_path)], capture_output=True, text=True)
        if res.returncode != 0:
            errors.append(f"Unit tests failed:\n{res.stderr or res.stdout}")

    if errors:
        print(json.dumps({"status": "FAIL", "errors": errors}, indent=2))
        sys.exit(1)

    print(json.dumps({"status": "PASS"}, indent=2))
    sys.exit(0)

if __name__ == "__main__":
    main()

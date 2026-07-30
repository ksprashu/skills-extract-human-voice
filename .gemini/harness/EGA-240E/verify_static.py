#!/usr/bin/env python3
# Copyright 2026 Google LLC
# Default General Deterministic Static Verifier
import sys
import json
import re
from pathlib import Path

import subprocess

def main():
    artifact_path = Path("/Users/ksprashanth/code/github/skills-extract-human-voice/.gemini/harness/EGA-240E/deliverable.md")
    if not artifact_path.exists():
        print(json.dumps({"status": "FAIL", "errors": [f"Artifact file missing: {artifact_path}"]}, indent=2))
        sys.exit(1)

    content = artifact_path.read_text(encoding="utf-8")
    errors = []

    # Check minimum word count in deliverable summary
    words = len(content.split())
    if words < 150:
        errors.append(f"Deliverable summary too short ({words} words, minimum is 150)")

    # Verify extract_voice.py implementation details
    script_path = Path("/Users/ksprashanth/code/github/skills-extract-human-voice/skills/extract-human-voice/scripts/extract_voice.py")
    if not script_path.exists():
        errors.append(f"Script missing: {script_path}")
    else:
        script_code = script_path.read_text(encoding="utf-8")
        if "--output-dir" not in script_code:
            errors.append("Script missing '--output-dir' CLI argument")
        if "--tool" not in script_code:
            errors.append("Script missing '--tool' CLI argument")
        if "--user-name" not in script_code:
            errors.append("Script missing '--user-name' CLI argument")
        if "REDACTED_IPV6" not in script_code and "<IP_ADDRESS>" not in script_code:
            errors.append("Script missing IPv6 scrubbing pattern")

    # Run unit tests to ensure all tests pass
    repo_root = Path("/Users/ksprashanth/code/github/skills-extract-human-voice")
    res = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests"], cwd=repo_root, capture_output=True, text=True)
    if res.returncode != 0:
        errors.append(f"Unit tests failed:\n{res.stderr}\n{res.stdout}")

    if errors:
        print(json.dumps({"status": "FAIL", "errors": errors}, indent=2))
        sys.exit(1)

    print(json.dumps({"status": "PASS"}, indent=2))
    sys.exit(0)

if __name__ == "__main__":
    main()

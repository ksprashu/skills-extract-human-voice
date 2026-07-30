#!/usr/bin/env python3
# Copyright 2026 Google LLC
# Default General Deterministic Static Verifier
import sys
import json
import re
from pathlib import Path

def main():
    artifact_path = Path("/Users/ksprashanth/code/github/skills-extract-human-voice/.gemini/harness/EGA-F245/deliverable.md")
    if not artifact_path.exists():
        print(json.dumps({"status": "FAIL", "errors": [f"Artifact file missing: {artifact_path}"]}, indent=2))
        sys.exit(1)

    content = artifact_path.read_text(encoding="utf-8")
    errors = []

    # Check minimum word count
    words = len(content.split())
    if words < 500:
        errors.append(f"Content too short ({words} words, minimum is 500)")

    # Check for required structural headings
    required_patterns = [
        r"#+\s+Executive Summary",
        r"#+\s+.*Architecture",
        r"#+\s+.*Quality Review",
        r"#+\s+.*Strengths",
        r"#+\s+.*Gaps",
        r"#+\s+.*Recommendations"
    ]
    for pattern in required_patterns:
        if not re.search(pattern, content, re.IGNORECASE):
            errors.append(f"Missing required section heading matching pattern: '{pattern}'")

    # Check for placeholder terms
    prohibited = ["TBD", "TODO", "as an AI"]
    for term in prohibited:
        if re.search(rf"\b{re.escape(term)}\b", content, re.IGNORECASE):
            errors.append(f"Contains prohibited placeholder: '{term}'")

    if errors:
        print(json.dumps({"status": "FAIL", "errors": errors}, indent=2))
        sys.exit(1)

    print(json.dumps({"status": "PASS"}, indent=2))
    sys.exit(0)

if __name__ == "__main__":
    main()

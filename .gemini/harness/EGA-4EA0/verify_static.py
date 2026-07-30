#!/usr/bin/env python3
# Copyright 2026 Google LLC

import sys
import json
import re
from pathlib import Path

def main():
    artifact_path = Path("/Users/ksprashanth/code/github/skills-extract-human-voice/.gemini/harness/EGA-4EA0/deliverable.md")
    if not artifact_path.exists():
        print(json.dumps({"status": "FAIL", "errors": [f"Artifact file missing: {artifact_path}"]}, indent=2))
        sys.exit(1)

    content = artifact_path.read_text(encoding="utf-8")
    errors = []

    # Check minimum word count (800 words for deep analysis)
    words = len(content.split())
    if words < 800:
        errors.append(f"Content too short ({words} words, minimum required is 800)")

    # Check for placeholder terms
    prohibited = ["TBD", "TODO", "as an AI"]
    for term in prohibited:
        if re.search(rf"\b{re.escape(term)}\b", content, re.IGNORECASE):
            errors.append(f"Contains prohibited placeholder: '{term}'")

    # Required section headers
    required_sections = [
        "Executive Summary & Architectural Overview",
        "Component & Structural Analysis",
        "Strengths & Unique Capabilities",
        "Gaps, Security & Edge Case Vulnerabilities",
        "Actionable Recommendations & Enhancements"
    ]
    for section in required_sections:
        if not re.search(rf"^#+\s+.*{re.escape(section)}", content, re.MULTILINE | re.IGNORECASE):
            errors.append(f"Missing required section header: '{section}'")

    # Check file link scheme
    if "file:///" not in content:
        errors.append("Missing file links using 'file:///' URI scheme")

    if errors:
        print(json.dumps({"status": "FAIL", "errors": errors}, indent=2))
        sys.exit(1)

    print(json.dumps({"status": "PASS"}, indent=2))
    sys.exit(0)

if __name__ == "__main__":
    main()


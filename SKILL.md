---
name: extract-human-voice
description: Automatically extracts the human voice and writing tone from various AI coding tools like Antigravity, Gemini CLI, Claude Code, Cline, Roo Code, Aider, and Cursor. Use when you need to analyze, compile, and package a user's conversational style and engineering constraints into canonical reference files.
---

# Extract Human Voice Skill

This skill provides an automated pipeline for scanning conversation history logs and databases from all major AI developer tools on your system (e.g., Antigravity CLI, Gemini CLI, Claude Code, Cline, Roo Code, Aider, and Cursor), scrubbing any sensitive metadata or PII, analyzing linguistic style markers, and generating a standard copybara-compatible writing persona profile.

## Quick Start

To extract your voice profile, run the helper script in this skill folder:

```bash
python3 /Users/ksprashanth/.agents/skills/extract-human-voice/scripts/extract_voice.py
```

This will walk the configured storage directories, analyze user prompts, and output three packaged canonical files under `/Users/ksprashanth/.agents/skills/extract-human-voice/output/`:
* `voice_and_tone.md` - Your core style and linguistic guidelines
* `golden_examples.md` - Sample high-bar engineering instructions
* `SKILL.md` - Frontmatter template for the writing assistant

## Workflows

### 1. Verification of Target Folders
Before running the extraction script, verify which AI coding tools you have installed on your Mac. The script automatically probes:
* `~/.gemini/antigravity-cli/brain/` (Antigravity logs)
* `~/.gemini/tmp/` (Gemini CLI logs)
* `~/.claude/projects/` (Claude Code logs)
* `~/Library/Application Support/Code/User/globalStorage/` (Cline and Roo Code)
* `~/.aider.history` (Aider logs)
* `~/Library/Application Support/Cursor/` (Cursor workspace and database logs)

If any directory does not exist, the script skips it gracefully.

### 2. PII & Sensitive Information Scrubbing
To ensure your template is ready for public or team sharing (e.g., in a git repo), the script scrubs:
* **Emails**: Replaced with `<EMAIL>`
* **Domains & URLs**: Corporate or internal endpoints are replaced with `<COMPANY_DOMAIN>` and `<INTERNAL_URL>`
* **Personal Identities**: Full names and specific usernames are replaced with `<USER_NAME>`, `<USER_NICKNAME>`, and `<USER_ID>`
* **Credentials**: API keys, JWTs, and GitHub Personal Access Tokens are replaced with `<REDACTED_SECRET>`

### 3. Packaging into copy-writer-bara
Once the script has completed, you can move the generated files from the `output/` folder into your custom copy-writer skill (e.g., `copy-writer-bara/`):
```bash
cp /Users/ksprashanth/.agents/skills/extract-human-voice/output/voice_and_tone.md /Users/ksprashanth/.agents/skills/copy-writer-bara/references/
cp /Users/ksprashanth/.agents/skills/extract-human-voice/output/golden_examples.md /Users/ksprashanth/.agents/skills/copy-writer-bara/references/
```

## Advanced Technical Specifications
For list of directory paths, schema types, database structures, and linguistic heuristics, see [REFERENCE.md](REFERENCE.md).
For processing comparisons and scrubbing examples, see [EXAMPLES.md](EXAMPLES.md).

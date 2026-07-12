# 🎙️ Extract Human Voice Skill

[![npx skills](https://img.shields.io/badge/skills.sh-installed-brightgreen)](https://skills.sh)

Automatically extracts the human voice and writing tone from various AI coding tools like Antigravity, Gemini CLI, Claude Code, Cline, Roo Code, Aider, and Cursor. Use this skill when you need to analyze, compile, and package a user's conversational style and engineering constraints into canonical reference files.

---

## 🚀 Overview

This skill provides an automated pipeline for scanning conversation history logs and databases from all major AI developer tools on your system, scrubbing any sensitive metadata or PII, analyzing linguistic style markers, and generating a standard Copybara-compatible writing persona profile.

### Key Features
* **Multi-Tool Support**: Scan and extract style parameters from Antigravity, Gemini CLI, Claude Code, Cline, Roo Code, Aider, and Cursor.
* **PII & Secret Scrubbing**: Automatically redacts API keys, credentials, email addresses, personal domains, and usernames.
* **Persona Generation**: Creates standardized markdown profiles suitable for custom agents or copy-writer tools.

---

## 📦 Installation

Install this skill into your local agent environment using `npx skills`:

```bash
npx skills add ksprashu/skills-extract-human-voice
```

---

## 🛠️ Usage

To extract your voice profile, execute the automated Python script included in this repository:

```bash
python3 scripts/extract_voice.py
```

### Outputs

The script walks through your system's logs, analyzes linguistic style markers, and outputs three packaged canonical files under the `output/` directory:

1. **`voice_and_tone.md`**: Your core style guidelines, sentence structures, and linguistic heuristics.
2. **`golden_examples.md`**: Sample high-bar engineering instructions collected from your history.
3. **`SKILL.md`**: Standard frontmatter metadata template ready to be deployed as a writing assistant.

---

## 📂 Repository Structure

```text
skills-extract-human-voice/
├── SKILL.md          # Skill entrypoint metadata and instructions
├── README.md         # Full project and usage documentation
├── EXAMPLES.md       # Examples of scrubbed PII and parsed outputs
├── REFERENCE.md      # Linguistic heuristics and target database structures
├── scripts/
│   └── extract_voice.py  # Automated voice extraction Python pipeline
└── output/           # (Auto-generated) Extracted markdown files
```

---

## 🎓 Technical Details & Reference

* Refer to [REFERENCE.md](REFERENCE.md) for database paths, sqlite schemas, and specific parsing rules.
* Refer to [EXAMPLES.md](EXAMPLES.md) for before/after comparison examples of the scrubbing processor.

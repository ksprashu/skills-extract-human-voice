# Voice and Tone Guidelines: <USER_NICKNAME> Persona

## Core Persona: The Pragmatic Dev Advocate Partner
This persona is modeled directly from historical interactions across different AI assistant logs. It is a blend of personal candor, high technical standards, direct command-driven brevity, and functional developer-focused aesthetics.

---

## 1. Key Style & Linguistic DNA

### Direct & Action-Oriented (No Hype)
* Speaks with authority, getting straight to the point.
* Uses active, imperative verbs: *"Review this repo and fix git history"*, *"Deploy updates to cloud run"*.
* Rejects boilerplate prose or excessive "let's do this!" marketing introductions.

### Typographical Authenticity
* **Spelling**: Prefers **US-English** conventions (e.g., *customisation*, *optimise*, *prioritise*).
* **Speed-Typing Shorthand**: Frequently features natural speed-typing shortcuts like *teh* (the), *anyting* (anything), *deplouyed* (deployed) as authentic live-terminal markings.
* **Dialogue Markers**: Uses conversational check-ins like *"Hello... what's happening here? You were hung."* or *"Is the backend also running?"*.

### Structural Preferences
* **Gap-First Setup**: Begins guides or write-ups by stating the exact real-world gap, discrepancy, or error message (highly pragmatic).
* **Optimized Density**: Prioritizes visual layout density, utilizing tooltips, (i) informational bubbles, collapsible FAQs, and clean whitespace optimizations over verbose copy.

---

## 2. Technical Rigor & "Grounding" Standard

* **Strict Code Grounding**: Absolutely rejects high-level summaries or hand-waving explanations. Every definition or documented formula must match the actual implemented codebase logic.
* **Preflight Verification**: Demands automated safeguards (CI/CD checkers, preflight style and lint steps) before pushing modifications.
* **Atomic Hygiene**: Expects pristine repository practices (feature branch isolation, atomic signed commits, clear workspace structure).

---

## 3. The Frustration Filter: Transforming Critiques
When tools break, redundant parallel loops happen, or designs look generic ("meh"), this persona voices clear critique. **These frustrations are converted into engineering values, omitting any emotional hostility**:

| Raw Critique Triggers | Transformed Writing Attribute |
| :--- | :--- |
| Redundant parallel processes / overlapping subagents | **High Concurrency Efficiency**: Ensure strict thread isolation, clean execution boundaries, and zero redundant steps. |
| Boring tables or minimal, low-density summaries | **High Visual and Presentation Density**: Mandate beautiful, custom dark-mode HTML presentations, charts, and Mermaid visualizations instead of raw Markdown where human review is key. |
| Ungrounded assertions or missing API constraints | **Rigor and Fact Verification**: Demands precise verification against source documentation and runtime endpoints (e.g., verifying Preview vs GA features). |

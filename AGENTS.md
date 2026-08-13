# Repository instructions

This repository contains a skills-only plugin for ChatGPT and Codex. Keep it provider-neutral unless a product-specific instruction is necessary.

## Catalog maintenance

- Treat `plugins/avoid-ai-writing-tropes/skills/avoid-ai-writing-tropes/references/tropes.md` as an editing aid, never an AI-authorship detector.
- Prefer primary research, corpus analyses, transparent methodology, and style guidance with concrete examples.
- Record source metadata, what each source supports, and its limitations.
- Preserve the `supported`, `tentative`, and `preference` distinction.
- Preserve genre exceptions and counterexamples.
- Make no catalog change when the evidence does not clear the documented bar.
- Do not invent sources, quotations, publication details, or empirical certainty.

## Change discipline

- Keep `SKILL.md` concise; detailed entries and citations belong in `references/tropes.md`.
- Before releasing any user-facing copy, review it with the bundled `avoid-ai-writing-tropes` skill. This includes plugin descriptions, interface labels, starter prompts, README text, installation guidance, contribution docs, templates, and release notes.
- Apply the skill with judgment: keep technical meaning, product names, commands, qualifications, and genre-appropriate structure intact. The goal is clear, specific copy, not mechanical removal of flagged words.
- Never commit credentials, tokens, private keys, local `.env` files, security-scan reports, or sensitive personal information. Use synthetic placeholders in documentation and tests.
- Bump the patch version in `.codex-plugin/plugin.json` when a catalog or workflow change is proposed for release.
- Run `pre-commit run --all-files`, `python3 scripts/validate_repository.py`, and the installed plugin validator when available.
- Automated maintenance must use a fresh branch from `origin/main`, open a draft pull request, and never merge it.

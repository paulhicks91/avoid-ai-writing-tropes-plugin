# Avoid AI Writing Tropes

A skills-only plugin for ChatGPT and Codex that finds canned openings, vague claims, forced transitions, repetitive patterns, and generic conclusions.

It can rewrite a draft or point out what is getting in the way. Edits stay close to the original: facts, qualifications, citations, technical terms, and deliberate style choices remain intact. The plugin never treats prose style as proof of AI authorship.

## What it catches

- an introduction that could lead into almost any topic;
- importance asserted with words such as “pivotal” or “profound” but never demonstrated;
- abstract metaphors where a concrete noun would be clearer;
- transitions that announce a connection instead of making one;
- repeated contrast formulas, triplets, recaps, and uniformly polished sentence shapes;
- reassurance, certainty, or uplift that the evidence has not earned.

These are prompts for judgment, not banned words. The same choice may be clumsy in a project update and useful in a speech, legal brief, or accessibility-focused guide.

## What is included

- `plugins/avoid-ai-writing-tropes/`: the installable plugin
- `skills/avoid-ai-writing-tropes/SKILL.md`: the editing and catalog-maintenance workflow
- `references/tropes.md`: the trope catalog, evidence labels, counterexamples, and source ledger
- `evals/cases.json`: positive and negative behavioral test cases
- `scripts/validate_repository.py`: dependency-free repository validation

This plugin has no MCP server, external service, authentication, hooks, or background process.

## Install from this repository

Add the Git-backed marketplace and install the plugin with Codex CLI:

```sh
codex plugin marketplace add paulhicks91/avoid-ai-writing-tropes-plugin --ref main
codex plugin add avoid-ai-writing-tropes@avoid-ai-writing-tropes
```

To refresh the marketplace after a release is merged:

```sh
codex plugin marketplace upgrade avoid-ai-writing-tropes
codex plugin add avoid-ai-writing-tropes@avoid-ai-writing-tropes
```

Start a new conversation after installing or refreshing so the updated skill catalog is loaded.

ChatGPT and Codex share the public OpenAI Plugins Directory. A GitHub merge updates Git-marketplace installations after refresh; it does not update a public-directory release. Public releases follow OpenAI's submission, review, and publishing process.

## Use

Ask for a rewrite, a review without edits, a new draft, or an update to the evidence catalog. For example:

- “Cut the canned setup and vague claims from this draft. Keep my facts and voice.”
- “Show me where this prose sounds generic, but don't rewrite it yet.”
- “Rewrite this in plain, specific language without flattening my style.”

The plugin will not estimate whether text was AI-generated from style alone.

## Validate

```sh
python3 scripts/validate_repository.py
```

Install the pinned pre-commit framework and enable the hooks once per clone:

```sh
python3 -m pip install pre-commit==4.6.2
pre-commit install
pre-commit run --all-files
```

Pre-commit rejects likely secrets, private keys, files over 1 MB, submodules, merge markers, malformed JSON or YAML, and common formatting mistakes. It also runs the repository validator.

GitHub Actions runs the repository validator and Gitleaks against the complete Git history on every pull request and push to `main`. Third-party Actions are pinned to full commit SHAs and run with read-only repository permissions.

## Maintenance

Catalog updates need focused pull requests that say what the sources support and where the evidence falls short. See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/maintenance.md](docs/maintenance.md).

## License

MIT

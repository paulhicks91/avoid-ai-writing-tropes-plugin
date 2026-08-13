# Contributing

Contributions should sharpen the catalog without turning ordinary words into warning signs.

## Evidence standard

For every proposed catalog change:

1. Link the source and record its author or publisher, publication date, access date, source type, and methodology.
2. State exactly which pattern the source supports or challenges.
3. Record important limitations, including genre, model, language, sample size, and publication bias.
4. Use `supported` only for replicated or methodologically transparent evidence.
5. Use `tentative` for plausible but incomplete observations and `preference` for house-style choices.
6. Preserve counterexamples. Ordinary words must not become mechanically forbidden vocabulary.

Do not infer who or what wrote a passage from style alone.

## Pull requests

Keep automated catalog updates focused. A maintenance pull request should include:

- the sources reviewed;
- entries added, strengthened, weakened, merged, or removed;
- the evidence label for each changed entry;
- limitations or disagreements found;
- validation results.

If research finds no evidence strong enough to change the catalog, do not open a pull request.

Run `python3 scripts/validate_repository.py` before submitting.

# Scheduled maintenance design

The `main` branch is the source of truth. A scheduled agent may research and propose catalog changes; a person reviews and merges them.

## Scheduled run

1. Fetch `origin` and start from the current `origin/main` in a clean clone or isolated worktree.
2. Stop when an earlier open pull request from the automation is still awaiting review.
3. Create a branch named `automation/tropes-YYYY-MM-DD`.
4. Review current public sources using the evidence standard in `CONTRIBUTING.md`.
5. Update only the catalog, related workflow text, test cases, and the plugin patch version needed for that evidence.
6. Run `python3 scripts/validate_repository.py` and the plugin validator when available.
7. If there is no meaningful diff, do not commit, push, or open a pull request.
8. Commit, push the branch, and open a draft pull request summarizing sources, evidence changes, limitations, and validation.
9. Stop. Never approve or merge the pull request.

## GitHub access

Use a dedicated fine-grained credential or GitHub App installation limited to this repository. It needs repository contents write access and pull request write access. It does not need administration access. Protect `main`, require pull requests, and prevent force pushes.

## Release behavior

After a merge, Git-marketplace users receive the change when they refresh the marketplace and reinstall or reload the plugin. The public OpenAI Plugins Directory uses reviewed release snapshots, so its copy must go through OpenAI's submission and publishing flow.

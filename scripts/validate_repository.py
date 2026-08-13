#!/usr/bin/env python3
"""Validate the repository's skills-only plugin without external packages."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_NAME = "avoid-ai-writing-tropes"
PLUGIN = ROOT / "plugins" / PLUGIN_NAME
SKILL = PLUGIN / "skills" / PLUGIN_NAME
WORKFLOWS = ROOT / ".github" / "workflows"


def load_json(path: Path, errors: list[str]) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
    return {}


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []
    manifest_path = PLUGIN / ".codex-plugin" / "plugin.json"
    marketplace_path = ROOT / ".agents" / "plugins" / "marketplace.json"
    evals_path = ROOT / "evals" / "cases.json"

    manifest = load_json(manifest_path, errors)
    marketplace = load_json(marketplace_path, errors)
    evals = load_json(evals_path, errors)

    if isinstance(manifest, dict):
        require(manifest.get("name") == PLUGIN_NAME, "manifest name must match plugin directory", errors)
        require(bool(re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", "")))), "manifest version must use strict semver", errors)
        require(bool(manifest.get("description")), "manifest description is required", errors)
        require(bool((manifest.get("author") or {}).get("name")), "manifest author.name is required", errors)
        require(manifest.get("skills") == "./skills/", "manifest skills path must be ./skills/", errors)
        require(manifest.get("license") == "MIT", "manifest license must match LICENSE", errors)

    if isinstance(marketplace, dict):
        entries = marketplace.get("plugins", [])
        match = next((entry for entry in entries if entry.get("name") == PLUGIN_NAME), None)
        require(match is not None, "marketplace must contain the plugin", errors)
        if match:
            require(match.get("source", {}).get("path") == f"./plugins/{PLUGIN_NAME}", "marketplace source path is incorrect", errors)
            require(match.get("policy", {}).get("installation") == "AVAILABLE", "installation policy must be AVAILABLE", errors)
            require(match.get("policy", {}).get("authentication") == "ON_INSTALL", "authentication policy must be ON_INSTALL", errors)

    skill_path = SKILL / "SKILL.md"
    require(skill_path.is_file(), "skill SKILL.md is missing", errors)
    require((SKILL / "references" / "tropes.md").is_file(), "trope catalog is missing", errors)
    require((SKILL / "agents" / "openai.yaml").is_file(), "skill interface metadata is missing", errors)
    if skill_path.is_file():
        skill_text = skill_path.read_text(encoding="utf-8")
        require(skill_text.startswith("---\n"), "SKILL.md must begin with YAML frontmatter", errors)
        require(re.search(r"^name:\s+avoid-ai-writing-tropes$", skill_text, re.MULTILINE) is not None, "SKILL.md name must match plugin", errors)

    if isinstance(evals, dict):
        require(len(evals.get("positive", [])) >= 5, "at least five positive evals are required", errors)
        require(len(evals.get("negative", [])) >= 3, "at least three negative evals are required", errors)

    require((ROOT / ".pre-commit-config.yaml").is_file(), "pre-commit configuration is missing", errors)
    require((WORKFLOWS / "security.yml").is_file(), "security workflow is missing", errors)

    action_pattern = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)", re.MULTILINE)
    immutable_action = re.compile(r"^[^@]+@[0-9a-f]{40}$")
    for workflow in sorted(WORKFLOWS.glob("*.y*ml")):
        workflow_text = workflow.read_text(encoding="utf-8")
        require("pull_request_target:" not in workflow_text, f"{workflow.relative_to(ROOT)} must not use pull_request_target", errors)
        for action in action_pattern.findall(workflow_text):
            if action.startswith("./"):
                continue
            require(
                immutable_action.fullmatch(action) is not None,
                f"{workflow.relative_to(ROOT)} uses an action that is not pinned to a full commit SHA: {action}",
                errors,
            )

    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts and path.suffix.lower() in {".json", ".md", ".yaml", ".yml", ".py"}:
            text = path.read_text(encoding="utf-8")
            placeholder = "[" + "TODO:"
            if placeholder in text:
                errors.append(f"placeholder remains in {path.relative_to(ROOT)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validated {PLUGIN_NAME} repository")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

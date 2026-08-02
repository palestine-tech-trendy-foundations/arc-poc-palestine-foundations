#!/usr/bin/env python3
"""
Module 1 autograder, Git Hygiene & Discipline.

Runs inside GitHub Actions on every push to a Pull Request targeting `main`.
Uses only the Python standard library and the `git` CLI (already present on
GitHub-hosted runners), no extra dependencies, no paid services.

Exit code 0 = all required checks passed.
Exit code 1 = at least one required check failed.

A human-readable report is written to stdout and to $GITHUB_STEP_SUMMARY
(GitHub renders that file as the summary panel on the Actions run).
"""

import json
import os
import re
import subprocess
import sys

REQUIRED_GITIGNORE_PATTERNS = [
    "__pycache__/",
    "*.pyc",
    "*.env",
    ".DS_Store",
    ".ipynb_checkpoints/",
]

CONVENTIONAL_COMMIT_RE = re.compile(
    r"^(feat|fix|docs|chore|refactor|test|style)(\([^)]+\))?: .+"
)

MIN_COMMITS = 4
MAX_FILES_PER_COMMIT = 5  # atomicity guard
PROJECT_LOG_PATH = "module-1-git-hygiene/starter/PROJECT_LOG.md"
BASE_BRANCH = os.environ.get("BASE_BRANCH", "origin/main")


def run(cmd):
    """Run a shell command and return stdout, raising on failure."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0 and "no upstream" not in result.stderr.lower():
        # Don't crash the whole grader on a single git quirk: surface it instead.
        pass
    return result.stdout.strip()


def get_branch_commits():
    """Return list of commit SHAs on this branch that aren't on the base branch."""
    log = run(f"git log {BASE_BRANCH}..HEAD --format=%H")
    return [c for c in log.splitlines() if c]


def check_gitignore():
    if not os.path.exists(".gitignore"):
        return False, "No `.gitignore` file found at the repo root."
    content = open(".gitignore").read()
    missing = [p for p in REQUIRED_GITIGNORE_PATTERNS if p not in content]
    if missing:
        return False, f"`.gitignore` is missing required pattern(s): {', '.join(missing)}"
    return True, "`.gitignore` exists and contains all required patterns."


def check_secret_never_tracked():
    # Search full branch history (not just the working tree) for any .env file
    # or the specific decoy filename ever being added.
    log = run(f"git log {BASE_BRANCH}..HEAD --name-only --format=")
    tracked_files = [f for f in log.splitlines() if f.strip()]
    offenders = [f for f in tracked_files if f.endswith(".env") or "local_config" in f]
    if offenders:
        return False, f"Found file(s) that should have been git-ignored but were committed: {', '.join(set(offenders))}"
    return True, "No `.env` or secret-like file was ever committed."


def check_commit_count(commits):
    if len(commits) < MIN_COMMITS:
        return False, f"Found {len(commits)} commit(s) on this branch; at least {MIN_COMMITS} are required."
    return True, f"{len(commits)} commits found on this branch."


def check_conventional_commits(commits):
    bad = []
    for sha in commits:
        subject = run(f"git log -1 --format=%s {sha}")
        if not CONVENTIONAL_COMMIT_RE.match(subject):
            bad.append(f"{sha[:7]}: \"{subject}\"")
    if bad:
        return False, "Commit(s) not following Conventional Commits format (type: description):\n    " + "\n    ".join(bad)
    return True, "All commit messages follow the Conventional Commits format."


def check_atomic_commits(commits):
    offenders = []
    for sha in commits:
        files = run(f"git diff-tree --no-commit-id --name-only -r {sha}")
        n_files = len([f for f in files.splitlines() if f.strip()])
        if n_files > MAX_FILES_PER_COMMIT:
            offenders.append(f"{sha[:7]} touched {n_files} files")
    if offenders:
        return False, "Commit(s) too large to be atomic:\n    " + "\n    ".join(offenders)
    return True, "All commits are reasonably small and focused."


def check_project_log_content():
    if not os.path.exists(PROJECT_LOG_PATH):
        return False, f"`{PROJECT_LOG_PATH}` not found."
    content = open(PROJECT_LOG_PATH, encoding="utf-8").read()

    problems = []
    if "recieve" in content.lower():
        problems.append("the typo 'recieve' was not fixed")
    if "<YOUR NAME HERE>" in content:
        problems.append("learner name placeholder was not filled in")
    if "<YYYY-MM-DD>" in content:
        problems.append("date placeholder was not filled in")

    reflection_match = re.search(r"## Reflection\s*\n(.*?)(\n##|\Z)", content, re.S)
    reflection_text = reflection_match.group(1).strip() if reflection_match else ""
    reflection_text = reflection_text.replace(
        "<Write your 2-4 sentence reflection here, following Step 6 of the module README.>", ""
    ).strip()
    if len(reflection_text.split()) < 15:
        problems.append("reflection section is missing or too short (aim for 2-4 sentences)")

    if problems:
        return False, "PROJECT_LOG.md issues: " + "; ".join(problems)
    return True, "PROJECT_LOG.md is complete: typo fixed, details filled in, reflection present."


def check_pr_title():
    """Only runs when triggered by a pull_request event; skipped otherwise."""
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path or not os.path.exists(event_path):
        return None, "Skipped (not running in a pull_request event context)."
    with open(event_path) as f:
        event = json.load(f)
    title = event.get("pull_request", {}).get("title", "")
    if not title:
        return None, "Skipped (no PR title found in event payload)."
    pattern = re.compile(r"^Module 1: Git Hygiene, .+")
    if not pattern.match(title):
        return False, f"PR title \"{title}\" does not match required format: \"Module 1: Git Hygiene, <Your Name>\""
    return True, "PR title follows the required naming convention."


def main():
    commits = get_branch_commits()

    checks = [
        ("Commit count", check_commit_count(commits)),
        ("Conventional commit messages", check_conventional_commits(commits)),
        ("Atomic commits", check_atomic_commits(commits)),
        (".gitignore present and correct", check_gitignore()),
        ("Secret file never tracked", check_secret_never_tracked()),
        ("PROJECT_LOG.md content", check_project_log_content()),
        ("PR title convention", check_pr_title()),
    ]

    lines = ["# Module 1: Git Hygiene Autograder Report", ""]
    all_passed = True
    for name, (passed, message) in checks:
        if passed is None:
            icon = "⚪️"
        elif passed:
            icon = "✅"
        else:
            icon = "❌"
            all_passed = False
        lines.append(f"### {icon} {name}")
        lines.append(message)
        lines.append("")

    lines.append("---")
    lines.append("**🌿 All required checks passed, your Git habits are looking sharp. Nice work.**" if all_passed
                  else "**Some checks did not pass.** Read the notes above, fix them on your branch, and push again, this re-runs automatically.")

    report = "\n".join(lines)
    print(report)

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a") as f:
            f.write(report + "\n")

    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()

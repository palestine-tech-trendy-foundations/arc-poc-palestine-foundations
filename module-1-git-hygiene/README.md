# Module 1 — Git Hygiene & Discipline 🌿

**Estimated time:** 90 minutes (30 min lesson + 60 min lab)
**What you need:** Git installed, a GitHub account, a text editor

> **Before you start:** read [`LESSON.md`](./LESSON.md) in this folder first. It covers the concepts behind every step below — what Git is actually tracking, why commit discipline matters, and how `.gitignore` really works. This lab will make a lot more sense with that context, and a couple of steps below assume you've read it.

## Why this module exists

Every professional software team relies on Git to work together without stepping on each other's work. But Git only works well when everyone follows a few shared habits — clear commit messages, small focused commits, branches instead of working directly on `main`, and never accidentally committing secrets or junk files.

This module assumes no prior Git experience. Every command you need is spelled out below, exactly as you should type it. What this module is really teaching isn't the commands themselves — it's Git *discipline*: the habits that separate a messy repo from a professional one. These habits are exactly what a hiring manager or a teammate checks first when they look at your GitHub history.

By the end of this module, you'll have gone through one full, realistic cycle of: branch → small disciplined commits → a clean `.gitignore` → a Pull Request. This is the same cycle you'll repeat in every module from here on.

## Learning objectives

By the end of this module you will be able to:
- Create and work on a feature branch instead of committing directly to `main`
- Write commit messages that follow the **Conventional Commits** format
- Make small, atomic commits instead of one giant commit
- Write a `.gitignore` that actually prevents junk and secret files from being tracked
- Open a Pull Request that follows a clean naming convention

## Before you start

Make sure you've already completed the **"Getting Set Up"** steps in the root [`README.md`](../README.md) — you should be inside the `palestine-tech-trendy-foundations` folder, in a terminal, with your fork cloned. If you haven't done that yet, go do it now before continuing.

Once you're set up, confirm you're on the `main` branch and up to date:

```bash
git status
git pull origin main
```

## Step 1 — Create your feature branch

Never commit directly to `main`. Create a branch named exactly like this (replace `<your-github-username>` with your actual GitHub username, all lowercase):

```bash
git checkout -b feature/git-hygiene-<your-github-username>
```

Example: if your GitHub username is `layla-dev`, run `git checkout -b feature/git-hygiene-layla-dev`.

> **Why it matters:** branch names that follow a predictable pattern (`feature/...`, `fix/...`) let teams automate workflows and instantly understand what a branch is for.

## Step 2 — Fix a typo (your first commit)

Open `starter/PROJECT_LOG.md`. Near the top, you'll find a sentence with a typo in it (read carefully — it's a real word, just misspelled). Fix it.

Commit **only this change**, with this exact message:

```bash
git add starter/PROJECT_LOG.md
git commit -m "fix: correct typo in project log"
```

## Step 3 — Add your name and today's date

In `starter/PROJECT_LOG.md`, find the line that says `Learner: <YOUR NAME HERE>` and replace `<YOUR NAME HERE>` with your actual name. Find the line that says `Date started: <YYYY-MM-DD>` and replace it with today's date.

Commit this as its own separate change:

```bash
git add starter/PROJECT_LOG.md
git commit -m "docs: add learner name and start date"
```

> **Why two separate commits (Step 2 and Step 3) instead of one?** This is the core idea of *atomic commits* — each commit should represent one logical change. If something breaks later, a reviewer (or you, in six months) can tell exactly which commit caused it. Bundling unrelated changes into one commit destroys that.

## Step 4 — Add a proper `.gitignore`

Create a file named `.gitignore` **at the root of the repository** (not inside `module-1-git-hygiene/`). It must include, at minimum, these five entries:

```
__pycache__/
*.pyc
*.env
.DS_Store
.ipynb_checkpoints/
```

These are standard patterns every Python project should ignore: compiled Python cache files, environment/secret files, macOS system files, and Jupyter checkpoint folders.

> **Careful:** `.env` on its own only ignores a file literally named `.env` — it will **not** catch a file like `local_config.env`. Use `*.env` (with the wildcard) so any file ending in `.env` is ignored, no matter what it's called. This is a real, common beginner mistake — catching it here is the whole point of Step 5.

Commit it:

```bash
git add .gitignore
git commit -m "chore: add gitignore for python artifacts"
```

## Step 5 — Prove your `.gitignore` actually works

This is the step most beginners get wrong: adding a `.gitignore` file doesn't matter if you never test that it actually ignores something.

1. In the root of the repo, create a new file called `local_config.env` with any content you like (e.g. `SECRET_KEY=test123`) — pretend this is a real secret file a developer forgot they had.
2. Run `git status`. **`local_config.env` should NOT appear as an untracked file.** If it does, your `.gitignore` from Step 4 is missing the `.env` pattern — fix it and re-commit before continuing.
3. Do **not** commit `local_config.env` itself. It should never enter your Git history at all — that's the entire point.

> **Why it matters:** committing a real `.env` file (API keys, passwords, database credentials) is one of the most common — and most damaging — mistakes junior developers make. Companies have had credentials leaked this way. This step builds the muscle memory to catch it before it happens.

## Step 6 — Add a short reflection

At the bottom of `starter/PROJECT_LOG.md`, under the `## Reflection` heading, write 2–4 sentences (about 20+ words) in your own words answering: *why does commit discipline matter on a real team, even for a solo learner right now?*

Commit it:

```bash
git add starter/PROJECT_LOG.md
git commit -m "feat: add reflection on git hygiene"
```

## Step 7 — Push and open a Pull Request

Push your branch:

```bash
git push origin feature/git-hygiene-<your-github-username>
```

On GitHub, open a Pull Request from your branch into `main`, **within your own fork**. Title it exactly:

```
Module 1: Git Hygiene — <Your Name>
```

Leave the description box with a short one-line summary of what you did — this is good practice, not graded separately.

## Step 8 — Check your results

Within a couple of minutes, an automated check will run and comment on your Pull Request with a breakdown of what passed and what didn't. If anything failed:

1. Read the comment carefully — it tells you exactly which check failed and why
2. Make the fix on the same branch
3. Commit and push again — the check re-runs automatically

There is no penalty for multiple attempts.

## What's being graded

| Check | What it verifies |
|---|---|
| `.gitignore` present and correct | Root `.gitignore` exists and contains all 5 required patterns |
| Secret file never tracked | `local_config.env` (or any `.env` file) never appears in your commit history |
| Commit count | At least 4 commits exist on your branch beyond `main` |
| Conventional commit messages | Every commit message follows the `type: description` format |
| Atomic commits | No single commit changes an unreasonably large number of files |
| PR title | Follows the exact naming convention from Step 7 |
| Content completed | Typo fixed, name/date filled in, reflection is present and substantive |

## Helpful Resources

You shouldn't need these to complete the lab — everything required is in this README and in `LESSON.md`. But if something isn't clicking, or you want to go deeper, these are solid, free, beginner-friendly places to look:

- **[Learn Git Branching](https://learngitbranching.js.org/)** — a free, visual, interactive way to actually see what branches and commits are doing. Great if the concepts in the lesson felt abstract.
- **[Pro Git book](https://git-scm.com/book/en/v2)** — the free, official Git book. Chapter 2 ("Git Basics") covers everything in this module in more depth.
- **[Conventional Commits specification](https://www.conventionalcommits.org/)** — the exact standard this module's commit message format is based on.
- **[GitHub Docs — About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)** — the official explanation of what a PR is and why teams use them.
- **[gitignore.io](https://www.toptal.com/developers/gitignore)** — generates starter `.gitignore` files for any language or tool. Good to know exists for future projects (don't use it to skip Step 4 in this lab — writing it yourself is the point this time).

## Troubleshooting

**"I committed `local_config.env` by accident before adding it to `.gitignore`."**
Adding a file to `.gitignore` after Git is already tracking it doesn't stop tracking it. Remove it from tracking (but keep the file on disk) with:
```bash
git rm --cached local_config.env
git commit -m "chore: stop tracking local_config.env"
```

**"`git checkout -b` says the branch already exists."**
You've already created it — just switch to it: `git checkout feature/git-hygiene-<your-github-username>`

**"My Pull Request check isn't running at all."**
Confirm your PR is targeting `main` in your own fork (not the original upstream repo), and that you actually pushed your branch (`git push origin <branch-name>`) before opening the PR.

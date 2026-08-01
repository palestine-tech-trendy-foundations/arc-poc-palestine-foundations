# Lesson — Why Git Hygiene Matters

Read this before starting the lab in `README.md`. This isn't graded — it's the thinking you need before the exercise makes sense.

## What Git Is Actually Tracking

Git manages three areas at once: your **working directory** (the files you see and edit), a **staging area** (a holding zone for changes you're about to commit), and the **repository** (the permanent, saved history).

`git add` moves a change from the working directory into staging. `git commit` takes a snapshot of everything currently staged and writes it permanently into the repository's history. This two-step process — add, then commit — exists on purpose: it lets you build a commit out of exactly the changes you want, even if you've edited five files but only want to save two of them right now.

This matters for the lab: when you commit "only this change" in Step 2, you're using `git add` on a single file deliberately, not because Git only lets you commit one file at a time.

## Why Commit History Is a Communication Tool, Not Just a Backup

New developers often think of commits as save points — a way to not lose work. That's true, but it undersells what commit history is actually for on a team: **it's the record of *why* the code looks the way it does.**

Six months from now, when something breaks, the fastest way to understand what changed is to read the commit history — not to read every line of code from scratch. A commit history made of clear, small, well-labeled changes turns into a searchable explanation of the project's evolution. A commit history made of one giant "fixed stuff" commit turns into nothing useful at all.

This is also why professional teams enforce a **commit message convention**. The one used in this program is [Conventional Commits](https://www.conventionalcommits.org/) — a free, widely-used open standard — where every commit message starts with a type (`feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `style`) followed by a colon and a short description. It looks small, but it means anyone — a teammate, a future you, or an automated tool generating a changelog — can scan a list of commits and immediately understand what category of change each one was, without opening a single file.

## Why "Atomic" Commits

An atomic commit does exactly one logical thing. Fixing a typo is one thing. Adding your name is a different thing. Even though both edits happen to be in the same file, they're unrelated changes — so they become two separate commits.

The payoff shows up when something goes wrong later. Git has a command called `git bisect` that can automatically binary-search through your commit history to find the exact commit that introduced a bug. That only works well if each commit is small and does one thing — if a single commit changes twenty unrelated things, finding out which *part* of that commit caused the bug becomes guesswork again.

## `.gitignore` — What It Actually Does, and What It Doesn't

`.gitignore` doesn't delete files, hide them from you, or encrypt them. It only tells Git: "don't track changes to anything matching these patterns." Untracked files still exist on your disk; Git simply stops treating them as part of the project's history.

Patterns in a `.gitignore` file use simple wildcard matching, not full regular expressions. The most important symbol is `*`, which matches "any sequence of characters." A pattern like `*.log` matches every filename ending in `.log`, regardless of what comes before it. A pattern with no wildcard, like `notes.txt`, matches *only* a file with that exact name — nothing else.

This distinction — exact match vs. wildcard match — is easy to get wrong, and getting it wrong with a file that's supposed to hold secrets (API keys, passwords, tokens) is one of the most common real-world mistakes junior developers make. The lab will have you verify this yourself rather than just take it on faith — a `.gitignore` line that *looks* like it should ignore a file, and one that actually *does*, aren't always the same thing.

## Why the Pull Request Step Exists

A Pull Request (PR) is a request to merge one branch into another, along with a space for discussion before that merge happens. Even when you're working solo — as in this lab — going through the PR step matters because it's the same mechanic you'll use on every real team project from here forward: work happens on a branch, gets reviewed (by a person or, as in this lab, by an automated check), and only then joins `main`.

Skipping straight to committing on `main` might feel faster today. It also means you never practice the workflow you'll be required to use starting next module, when your commits are being reviewed by a teammate.

---

## Check Your Understanding

Think through these before opening `README.md`. Nothing here is submitted or graded — if you can't answer one, that's a signal to re-read the relevant section above, not a problem.

1. You edit two unrelated things in the same file — a typo fix and a new sentence. Should that be one commit or two? Why?
2. What's the difference between a `.gitignore` pattern of `secrets.txt` and one of `*.txt`?
3. If a file is already being tracked by Git, does adding it to `.gitignore` *after the fact* stop Git from tracking it? (Hint: think about what `.gitignore` actually controls.)
4. Why would `git bisect` become less useful on a repo full of large, mixed-purpose commits?

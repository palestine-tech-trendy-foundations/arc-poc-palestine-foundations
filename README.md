# Palestine Tech Trendy — Foundations Track

Two self-guided, fully autograded modules for complete beginners, built for the **Palestine Tech Trendy** program under the **ARC** curriculum (Istidama Consulting, DELTA v1.1 methodology).

No instructor review is required to complete these modules. Everything is graded automatically by GitHub Actions the moment you push your work. This track assumes **no prior experience** with Git, GitHub, the command line, or programming — every step is spelled out.

---

## Table of Contents

1. [Before You Start — Requirements](#before-you-start)
2. [Getting Set Up — Do This Once](#getting-set-up)
3. [How This Repo Works](#how-this-repo-works)
4. [The Modules](#the-modules)
5. [Completion Checklist](#completion-checklist)
6. [Getting Help](#getting-help)

---

## Before You Start — Requirements {#before-you-start}

Confirm you have all of these before you begin — none of them are part of the graded work, but starting without them will cost you time that should go toward learning instead.

| Requirement | How to check | Where to get it |
|---|---|---|
| A GitHub account | You can log in at [github.com](https://github.com) | Free — [github.com/join](https://github.com/join) |
| Git installed | Run `git --version` in a terminal — should print a version number | [git-scm.com/downloads](https://git-scm.com/downloads) |
| Python 3.10+ (Module 2 only) | Run `python3 --version` — should print `3.10` or higher | [python.org/downloads](https://www.python.org/downloads/) |
| A text editor | Any will do | [VS Code](https://code.visualstudio.com/) recommended, free |
| `pytest` installed (Module 2 only) | Run `pip install pytest` | Installs via pip, no account needed |

Everything above is free. No paid tool or subscription is required anywhere in this track.

**New to the terms "terminal" or "command line"?** It's a text-based way to give your computer instructions, instead of clicking icons. Every operating system has one built in — you don't need to install anything extra to get one:

| Your computer | How to open a terminal |
|---|---|
| **Windows** | Press the Windows key, type `Git Bash` (installed automatically with Git), press Enter |
| **macOS** | Press `Cmd + Space`, type `Terminal`, press Enter |
| **Linux** | Press `Ctrl + Alt + T`, or search for "Terminal" in your applications menu |

You'll type commands into this window and press Enter to run them. Every command in this track is written out exactly — you never need to guess or modify what's shown.

---

## Getting Set Up — Do This Once {#getting-set-up}

Do this before Module 1. It only needs to happen one time for this whole track.

**Step 1 — Get your own copy of this repo.** When you enrolled on Moodle, a background process automatically created a personal copy (called a "fork") of this repository in your own GitHub account. You don't need to click anything to make this happen — it's already done by the time you read this.

**Step 2 — Find your fork's address.** Log into GitHub, go to "Your repositories," and open the one named `palestine-tech-trendy-foundations`. Click the green **"Code"** button, and copy the URL shown under **HTTPS** — it will look like:

```
https://github.com/<your-github-username>/palestine-tech-trendy-foundations.git
```

**Step 3 — Open a terminal** (see the table above if you're not sure how).

**Step 4 — Download ("clone") your fork to your computer.** In the terminal, type the command below, but replace the URL with the one you copied in Step 2, then press Enter:

```bash
git clone https://github.com/<your-github-username>/palestine-tech-trendy-foundations.git
```

You'll see some text scroll by as Git downloads the files. When it's done, you'll be back at a normal prompt.

**Step 5 — Move into the folder you just downloaded:**

```bash
cd palestine-tech-trendy-foundations
```

**Step 6 — Confirm it worked.** Type this and press Enter:

```bash
git status
```

You should see something like `On branch main` and `nothing to commit, working tree clean`. If you see that, you're fully set up.

From here on, every command in Module 1 and Module 2's instructions assumes you're inside this folder, in a terminal, exactly like this.

---

## How This Repo Works {#how-this-repo-works}

1. **You've already forked and cloned this repo** (see Getting Set Up above) — you're working on your own personal copy, not the shared original.
2. **You work through each module locally**, following its instructions inside this folder.
3. **You submit by opening a Pull Request.** When a module's instructions tell you to, you push your work and open a PR from your branch into `main` — inside your own fork, not the original shared repo. (Module 1's lesson explains exactly what a "branch" and a "Pull Request" are, in case those are new terms.)
4. **An automated check grades your PR within minutes.** A bot comments directly on your Pull Request with a pass/fail breakdown of every requirement. There is no waiting for a human reviewer.
5. **You can fix and resubmit as many times as you need.** Push again to the same branch and the check re-runs automatically. There's no penalty for multiple attempts — the goal is that you leave with correct, working code, not that you get it right the first time.

---

## The Modules {#the-modules}

Each module folder contains two documents, always in this order:

- **`LESSON.md`** — read this first. It explains the concepts behind the module: not just *what* to type, but *why* it works that way. Ends with a short "Check Your Understanding" section (not graded — just for you).
- **`README.md`** — the hands-on lab. Step-by-step instructions, starter files to complete, and exactly what's being graded.

| Module | Lesson | Lab |
|---|---|---|
| Module 1 — Git Hygiene & Discipline | [LESSON.md](./module-1-git-hygiene/LESSON.md) | [README.md](./module-1-git-hygiene/README.md) |
| Module 2 — Python & GitHub Foundations | [LESSON.md](./module-2-python-github-foundations/LESSON.md) | [README.md](./module-2-python-github-foundations/README.md) |

Work through Module 1 completely (lesson, then lab, then a passing Pull Request) before starting Module 2 — Module 2 assumes the Git workflow from Module 1 is already comfortable for you.

Within each module: **read the lesson in full before opening the lab.** The lab instructions assume you already have that context, and skipping the lesson is the single most common reason students get stuck on something it already explained.

---

## Completion Checklist {#completion-checklist}

You're done with this track when all of the following are true:

- [ ] Completed the "Getting Set Up" steps above
- [ ] Read `module-1-git-hygiene/LESSON.md`
- [ ] Opened a Pull Request for Module 1, titled correctly, with all automated checks passing
- [ ] Read `module-2-python-github-foundations/LESSON.md`
- [ ] Opened a Pull Request for Module 2, titled correctly, with all automated checks passing (including hidden tests)

Both Pull Requests should be left **open**, not merged — do not merge your own PRs.

---

## Getting Help {#getting-help}

These modules are self-guided by design. Before asking for help on something that isn't a content question:

1. Check the **Troubleshooting** section at the bottom of the relevant module's `README.md` — it covers the most common beginner blockers for that specific module
2. Re-read the failed check's message on your Pull Request comment carefully — it's written to tell you exactly what's wrong, not just that something is wrong
3. If you're still stuck after that, reach out through your program's normal support channel (Moodle / your coordinator)

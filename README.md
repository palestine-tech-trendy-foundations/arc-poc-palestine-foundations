# Palestine Tech Trendy — Foundations Track

Two self-guided, fully autograded modules for complete beginners, built for the **Palestine Tech Trendy** program under the **ARC** curriculum (Istidama Consulting, DELTA v1.1 methodology).

No instructor review is required to complete these modules. Everything is graded automatically by GitHub Actions the moment you push your work.

---

## Table of Contents

1. [Before You Start — Requirements](#before-you-start)
2. [How This Repo Works](#how-this-repo-works)
3. [Your Day-by-Day Plan](#your-day-by-day-plan)
4. [Daily Workflow — What You'll Actually Do Each Day](#daily-workflow)
5. [If You Fall Behind](#if-you-fall-behind)
6. [Completion Checklist](#completion-checklist)
7. [Getting Help](#getting-help)

---

## Before You Start — Requirements {#before-you-start}

Confirm you have all of these **before Day 1** — none of them are part of the graded work, but starting Day 1 without them will cost you time that should go toward learning instead.

| Requirement | How to check | Where to get it |
|---|---|---|
| A GitHub account | You can log in at [github.com](https://github.com) | Free — [github.com/join](https://github.com/join) |
| Git installed | Run `git --version` in a terminal — should print a version number | [git-scm.com/downloads](https://git-scm.com/downloads) |
| Python 3.10+ (Module 2 only) | Run `python3 --version` — should print `3.10` or higher | [python.org/downloads](https://www.python.org/downloads/) |
| A text editor | Any will do | [VS Code](https://code.visualstudio.com/) recommended, free |
| `pytest` installed (Module 2 only) | Run `pip install pytest` | Installs via pip, no account needed |

Everything above is free. No paid tool or subscription is required anywhere in this track.

---

## How This Repo Works {#how-this-repo-works}

1. **You get your own copy of this repo automatically.** When you enroll on Moodle, a background process forks this repository into your own GitHub account — you don't trigger this yourself.
2. **You clone your fork** to your computer and work locally, following each module's instructions.
3. **You submit by opening a Pull Request.** When a module's instructions tell you to, you push your branch and open a PR from your branch into `main` — inside your own fork, not the original shared repo.
4. **An automated check grades your PR within minutes.** A bot comments directly on your Pull Request with a pass/fail breakdown of every requirement. There is no waiting for a human reviewer.
5. **You can fix and resubmit as many times as you need.** Push again to the same branch and the check re-runs automatically. There's no penalty for multiple attempts — the goal is that you leave with correct, working code, not that you get it right the first time.

Each module folder contains two documents, always in this order:

- **`LESSON.md`** — read this first. It explains the concepts behind the module: not just *what* to type, but *why* it works that way. Ends with a short "Check Your Understanding" section (not graded — just for you).
- **`README.md`** — the hands-on lab. Step-by-step instructions, starter files to complete, and exactly what's being graded.

---

## Your Day-by-Day Plan {#your-day-by-day-plan}

This track is designed to be completed over **4 days**, at roughly 45–60 minutes per day. It's built this way on purpose: rushing both modules in one sitting tends to produce exactly the kind of mistakes the autograder is designed to catch, and a Pull Request built in a rush is rarely one you'd be proud to show later.

Day 1 below means "the day you start" — not a fixed calendar date. If your cohort has a fixed start date, your coordinator will tell you what calendar date Day 1 corresponds to.

| Day | Focus | What's due by end of day | Time needed |
|---|---|---|---|
| **Day 01** | Module 1 — Lesson | Read `module-1-git-hygiene/LESSON.md`. Answer the "Check Your Understanding" questions for yourself (not submitted). | ~30 min |
| **Day 02** | Module 1 — Lab | Complete all 7 steps in `module-1-git-hygiene/README.md`. **Pull Request opened**, titled `Module 1: Git Hygiene — <Your Name>`, with all automated checks passing. | ~60 min |
| **Day 03** | Module 2 — Lesson | Read `module-2-python-github-foundations/LESSON.md`. Answer the "Check Your Understanding" questions for yourself (not submitted). | ~30 min |
| **Day 04** | Module 2 — Lab | Complete all 7 steps in `module-2-python-github-foundations/README.md`. **Pull Request opened**, titled `Module 2: Python Foundations — <Your Name>`, with all automated checks passing (visible + hidden tests). | ~60 min |

**Hard rule:** don't start a Lab day before finishing that module's Lesson day. The lab instructions assume you've already read the lesson, and skipping it is the single most common reason students get stuck on something the lesson already explained.

---

## Daily Workflow — What You'll Actually Do Each Day {#daily-workflow}

**Lesson days (Day 01, Day 03):**
1. Open the module's `LESSON.md` in your text editor or directly on GitHub
2. Read it fully, once, without trying to code anything yet
3. Go through the "Check Your Understanding" questions at the end — if you can't answer one confidently, re-read that section before moving on
4. Stop there. Don't start the lab the same day unless you have extra time — the lesson needs to sit for a bit before the lab clicks.

**Lab days (Day 02, Day 04):**
1. Open the module's `README.md` and follow it top to bottom — don't skip steps or jump ahead
2. Commit as you go, exactly as each step instructs (small, separate, clearly-labeled commits — not one commit at the end)
3. Push and open your Pull Request when the instructions tell you to
4. Wait a couple of minutes for the automated comment to appear on your PR
5. If anything failed: read the comment carefully, fix it on the same branch, push again
6. Repeat step 4–5 until everything passes

---

## If You Fall Behind {#if-you-fall-behind}

This plan assumes a normal pace for someone new to these tools — it is not a hard deadline enforced by the autograder. The grading checks don't care what day it is; they only check whether your work is correct.

If Day 1 takes you two days instead of one, that's fine — keep going in order, just shifted. What matters is finishing each Lesson before starting its Lab, and finishing Module 1 before starting Module 2. There's no benefit to rushing past a step you don't understand yet, and no penalty in this repo for taking the time you actually need.

If your program has a hard external deadline (e.g., tied to a cohort schedule in Moodle or TalentLMS), that deadline will be communicated to you separately — it is not enforced by anything in this repository.

---

## Completion Checklist {#completion-checklist}

You're done with this track when all of the following are true:

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

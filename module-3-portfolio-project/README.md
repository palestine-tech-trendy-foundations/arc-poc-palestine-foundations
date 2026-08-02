# Module 3, Portfolio Project: Your Own Data Story

**Estimated time:** 90 minutes (30 min lesson + 60 min project)
**What you need:** Everything from Module 1 and Module 2, plus `matplotlib` (new this project)

> **Before you start:** read [`LESSON.md`](./LESSON.md) in this folder first, it explains why this project has no starter code, and teaches the one new tool you need, a simple matplotlib chart.

## Table of Contents

1. [What You're Building](#what-youre-building)
2. [Step 1: Pick Your Topic](#step-1)
3. [Step 2: Create Your Data](#step-2)
4. [Step 3: Create Your Feature Branch](#step-3)
5. [Step 4: Write Your Functions](#step-4)
6. [Step 5: Make Your Chart](#step-5)
7. [Step 6: Write Your Project Page](#step-6)
8. [Step 7: Commit, Push, Open a PR](#step-7)
9. [Step 8: Check Your Results](#step-8)
10. [What's Being Graded](#whats-being-graded)
11. [After This Passes, Showing It Off](#showing-it-off)

## What You're Building {#what-youre-building}

A small, complete, personal data project: your own small dataset, a few Python functions that analyze it, one chart, and a polished project page explaining what you found. Unlike Modules 1 and 2, there's no fixed answer key, this is graded on completeness and quality, not on matching exact numbers.

By the end, you'll have something real to link from your GitHub profile or CV, not just a completed exercise.

## Step 1: Pick Your Topic {#step-1}

Pick **one** of these (or a close variation, personal and simple is the goal):

| Idea | Example columns | Example question you could answer |
|---|---|---|
| **Personal spending** | date, category, amount | Which category do I spend the most on? |
| **Study or screen time habits** | day, activity, hours | Which day do I study the most/least? |
| **A hobby you track** (books, matches, games) | date, title/opponent, result or rating | What's my average rating this month? |
| **Meals or habits at home** | date, meal type, category | How many home-cooked vs. takeout meals this month? |
| **Fitness or step tracking** | date, steps or minutes | What's my average per day, and my best day? |

Don't overthink this choice, any of these works equally well for the project. Pick whichever you'd actually enjoy looking at.

## Step 2: Create Your Data {#step-2}

Create a file at `module-3-portfolio-project/data/my_data.csv` with:
- At least **10 rows** of data (not counting the header)
- At least **2 columns** beyond any ID or date column (so there's something to actually analyze)

This can be real data about you, or realistic estimated data if you don't have exact records, either is fine, the goal is practicing the skill, not scientific accuracy.

## Step 3: Create Your Feature Branch {#step-3}

```bash
git checkout -b feature/portfolio-project-<your-github-username>
```

## Step 4: Write Your Functions {#step-4}

Create `module-3-portfolio-project/project.py` with **at least 3 functions**, each with a real, descriptive docstring (see `LESSON.md` for what makes a docstring "real"). At minimum:

1. A function that **loads your CSV** into a usable structure (reuse the pattern from Module 2's `load_harvest_data`)
2. A function that **computes at least one summary statistic** from your data (a total, an average, a max, whatever fits your topic)
3. **One more function of your choice** that analyzes your data some other way

Commit as you go, same discipline as every module before this one:
```bash
git add module-3-portfolio-project/project.py
git commit -m "feat: add data loading function"
```
(then repeat with separate commits for each additional function, at least 4 commits total by the end of this project, same standard as Modules 1 and 2)

## Step 5: Make Your Chart {#step-5}

Using the matplotlib pattern from `LESSON.md`, create one chart from your data and save it as `module-3-portfolio-project/chart.png`. Give it a real title and a labeled axis, not placeholder text.

```bash
git add module-3-portfolio-project/chart.png
git commit -m "feat: add chart visualizing my data"
```

## Step 6: Write Your Project Page {#step-6}

Create `module-3-portfolio-project/PROJECT.md`, this is the page someone would actually read if they clicked into your repo. It must include these sections:

```markdown
# [Your Project Title]

## About This Project
[1-2 sentences: what did you explore, and why this topic?]

## What I Found
[At least 2 specific findings, actual numbers from your own data, not vague impressions]

## Chart
![chart](./chart.png)

## Skills Used
[A short list, e.g. Python, Git & GitHub, data analysis, matplotlib]
```

Commit it:
```bash
git add module-3-portfolio-project/PROJECT.md
git commit -m "feat: add project page"
```

## Step 7: Commit, Push, Open a PR {#step-7}

```bash
git push origin feature/portfolio-project-<your-github-username>
```

Open a PR into `main`, titled exactly:
```
Module 3: Portfolio Project, <Your Name>
```

## Step 8: Check Your Results {#step-8}

Within a couple of minutes, an automated comment appears on your PR confirming your submission is complete (all required files present, functions with real docstrings, PROJECT.md has all 3 required sections). Fix and push again as many times as needed.

## What's Being Graded {#whats-being-graded}

| Check | What it verifies |
|---|---|
| `data/my_data.csv` exists | At least 10 rows, at least 2 data columns |
| `project.py` exists | At least 3 functions, each with a non-empty, non-trivial docstring |
| `chart.png` exists | A valid image file |
| `PROJECT.md` exists | Contains all 3 required sections |
| Git hygiene | At least 4 atomic, conventionally-formatted commits |
| PR title | Follows the exact naming convention from Step 7 |

This project does **not** check whether your specific numbers are "correct", there's no answer key for your own data. It checks that your project is real, complete, and well-documented.

## After This Passes, Showing It Off {#showing-it-off}

Once your PR is merged (or even while it's open), a few things worth doing on your own GitHub profile:

- **Pin this repository** on your GitHub profile page (Profile → Customize your pins)
- Add a one-line description to the repo itself, "My first data project, built while learning Python and Git"
- If you're comfortable with it, add a link to this project in the featured/projects section of your LinkedIn profile

None of this is graded, it's just the difference between a project that exists and a project someone else actually sees.

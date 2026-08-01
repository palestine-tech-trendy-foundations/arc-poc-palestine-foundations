# Module 2 — Python & GitHub Foundations 🫒

**Estimated time:** 90 minutes (30 min lesson + 60 min lab) — add 45–60 min first if you're completely new to Python; see the self-check at the top of `LESSON.md`
**What you need:** Python 3.10+, Git, the habits from Module 1

> **Before you start:** read [`LESSON.md`](./LESSON.md) in this folder first — it opens with a quick self-check to confirm you're ready for this module, then covers why functions are structured this way, why input validation matters, and a common bug you're likely to hit when reading the CSV.

## Scenario

You're helping a small olive-growing cooperative in Palestine analyze this season's harvest. They've collected data from 8 plots across Nablus, Jenin, Hebron, Ramallah, and Bethlehem — how much land each plot covers (in dunams, a common regional land unit), how many kilograms of olives were harvested, and the moisture content of the olives at harvest time.

They've asked for four things:
1. A way to compare plots fairly (yield per dunam, not just raw kilograms — a big plot harvesting a lot isn't necessarily doing *well*)
2. A rough estimate of how much oil that harvest will produce
3. A way to flag plots that underperformed, so the cooperative can investigate why
4. A one-shot season summary they can share with members

This is exactly the kind of task real data/AI work starts with: not machine learning, just clean, correct, well-tested functions over real data. Everything from here — pandas, NLP, RAG, agents — is built on this same foundation of writing functions you can trust.

## Learning objectives

By the end of this module you will be able to:
- Write and test small, single-purpose Python functions
- Read structured data from a CSV file using the standard library
- Validate inputs and raise appropriate errors
- Run a test suite locally with `pytest` before pushing your work
- Apply the same Git discipline from Module 1 (branch, atomic commits, PR) to a code-based task

## Before you start

Make sure you're on `main` and up to date, and that Module 1 is already merged or at least complete:

```bash
git checkout main
git pull origin main
```

Install `pytest` if you don't already have it:

```bash
pip install pytest
```

(This is the only dependency this module needs — no paid tools, no heavy libraries.)

## Step 1 — Create your feature branch

```bash
git checkout -b feature/python-foundations-<your-github-username>
```

## Step 2 — Explore the data first

Before writing any code, open `data/harvest_data.csv` and look at it. Notice the columns: `plot_id`, `region`, `dunams`, `kg_harvested`, `moisture_pct`. Notice that everything in a CSV is text by default — even the numbers — which matters for Step 3.

## Step 3 — Implement the functions

Open `starter/functions.py`. There are five functions, each with a docstring explaining exactly what it must do and return. Implement them **one at a time, in this order** — each one builds on the last:

1. `load_harvest_data(filepath)`
2. `yield_per_dunam(kg_harvested, dunams)`
3. `estimate_oil_liters(kg_harvested, extraction_rate=0.18)`
4. `flag_underperforming_plots(records, threshold_kg_per_dunam)`
5. `summarize_season(records)`

After each function, run the tests to check your progress:

```bash
python -m pytest tests/ -v
```

You don't need to get everything passing before your first commit — see Step 4.

## Step 4 — Commit as you go, not all at once

Just like Module 1, commit each function (or small group of related work) separately, using the Conventional Commits format:

```bash
git add starter/functions.py
git commit -m "feat: implement load_harvest_data"
```

Repeat as you complete each function. By the end you should have **at least 4 commits** on this branch — one giant "finished everything" commit will not pass the Git hygiene checks carried over from Module 1.

## Step 5 — Get all visible tests passing

Once all five functions are implemented, run the full visible test suite:

```bash
python -m pytest tests/ -v
```

All tests in `tests/test_functions.py` should pass. If something fails, read the assertion message carefully — it tells you exactly what was expected vs. what your function returned.

> **Note on hidden tests:** the automated check that runs on your Pull Request includes one or two additional test cases you can't see locally — the same way a real code reviewer sometimes catches an edge case your own tests missed. Passing all the visible tests is necessary but not by itself a guarantee. Think about edge cases yourself: What happens with an empty list? A zero value? A negative value? Your functions' docstrings tell you what's expected in each case — implement those cases properly, not just the happy path.

## Step 6 — Push and open a Pull Request

```bash
git push origin feature/python-foundations-<your-github-username>
```

Open a Pull Request into `main`, titled exactly:

```
Module 2: Python Foundations — <Your Name>
```

## Step 7 — Check your results

Same as Module 1: an automated comment appears on your PR within a couple of minutes with a full pass/fail breakdown, including the hidden checks. Fix and push again as many times as you need.

## What's being graded

| Check | What it verifies |
|---|---|
| Visible tests | All tests in `tests/test_functions.py` pass |
| Hidden tests | 1–2 additional edge-case tests not visible in your local repo |
| Git hygiene | Same standard as Module 1 — at least 4 atomic, conventionally-formatted commits on a feature branch |
| PR title | Follows the exact naming convention from Step 6 |

## Helpful Resources

Everything required is in this README and `LESSON.md`, but these are solid, free places to go deeper if something isn't clicking:

- **[The Python Tutorial (official docs)](https://docs.python.org/3/tutorial/)** — Sections 4 (control flow) and 4.6–4.8 (functions) cover exactly what you need for this lab.
- **[learnpython.org](https://www.learnpython.org/)** — free, interactive, runs in your browser. The "Functions" and "Dictionaries" lessons are the most directly relevant here.
- **[csv — official Python docs](https://docs.python.org/3/library/csv.html)** — the standard library module `load_harvest_data` is built on.
- **[Python Errors and Exceptions (official docs)](https://docs.python.org/3/tutorial/errors.html)** — covers `raise` and `ValueError` in more depth than the lesson does.
- **[pytest — Get Started](https://docs.pytest.org/en/stable/getting-started.html)** — the official quick-start guide for the testing tool this lab uses.

## Troubleshooting

**"`ModuleNotFoundError: No module named 'functions'`" when running pytest.**
Run pytest from inside the `module-2-python-github-foundations/` folder, not the repo root: `cd module-2-python-github-foundations && python -m pytest tests/ -v`

**"My CSV values are coming out as strings, not numbers, even though I used DictReader."**
`csv.DictReader` always reads every value as a string — you need to convert the numeric fields yourself with `float(...)` inside `load_harvest_data`.

**"I'm not sure what error message to use when raising `ValueError`."**
The tests only check that a `ValueError` is raised, not its exact message — any message is fine as long as it's a `ValueError`.

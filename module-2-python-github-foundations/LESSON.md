# Lesson: Why We Write Small, Tested Functions

Read this before starting the lab in `README.md`. This isn't graded, it's the thinking you need before the exercise makes sense.

## First: A Quick Check

This lesson explains *why* this module's functions are built the way they are. It assumes you already know basic Python syntax: how to write a `for` loop, how to define a function with `def`, and how to read and write to a dictionary (`some_dict["key"]`).

**If any of those three are unfamiliar, stop here first**, don't struggle through this lesson without them, it'll be frustrating for no reason. Go to **[learnpython.org](https://www.learnpython.org/)** (free, interactive, runs in your browser, no account needed) and complete these lessons first:

- Variables and Types
- Lists
- Loops
- Functions
- Dictionaries

That's roughly 45–60 minutes for someone with zero prior programming experience. Once you can comfortably write a small function that uses a loop and returns a value, come back here.

**If those three already feel familiar, keep going below**, you don't need to do anything else first.

## What a Function Actually Buys You

A function is a named, reusable piece of logic that takes specific inputs and produces a specific output. That sounds obvious, but the real value isn't "reusability" in the abstract, it's that a well-written function becomes a unit you can trust *without re-reading its internals every time you use it*.

Once you've verified `yield_per_dunam(kg_harvested, dunams)` is correct, you never have to think about how it computes that ratio again. You just call it. This is how real data and AI systems are built: not as one giant script, but as many small, individually-verified functions composed together. Every pipeline you'll build later in this program, data cleaning, model training, evaluation, is this same pattern at a larger scale.

## Why Input Validation Isn't Optional

A function that silently returns a wrong answer is far more dangerous than one that clearly fails. If `yield_per_dunam(500, -2)` just returned `-250.0` instead of raising an error, that broken number could flow silently into a report, a chart, or a decision, and nobody would notice until much later, if ever.

This is why the functions in this lab are specified to `raise ValueError` on invalid input rather than trying to "handle" bad data quietly. A loud, immediate failure at the source of the problem is almost always better than a quiet, wrong answer three steps downstream. You'll see this principle again constantly in data and ML work: **fail fast, fail loud, fail close to the source of the mistake.**

## The CSV Type Trap

Every value read from a CSV file arrives as a string, including numbers. `"950"` is not the same value as `950` in Python: you can't do arithmetic on `"950"` the way you can on `950`, and comparisons like `"950" > "100"` don't behave the way you'd expect from comparing actual numbers (string comparison is character-by-character, not numeric).

This is a real, common source of bugs for people new to working with data files: code that *looks* correct, runs without crashing, and still produces wrong answers, because a value that should have been converted to a number never was. Watch for this as you implement `load_harvest_data`.

## Visible Tests vs. Hidden Tests: and Why Both Exist

The tests in `tests/test_functions.py` are visible to you, you can read them, run them locally, and use them to guide your implementation as you build. That's their job: fast, immediate feedback while you work.

But a function that passes every test *you* thought to write isn't necessarily correct, it's only correct for the cases *you* thought of. This is exactly what happens in real code review: a teammate or reviewer often thinks of an edge case the original author didn't. The hidden tests that run during grading play that role here. They're not trying to trick you, they're testing boundary conditions and edge cases implied by each function's docstring, the same way a careful reviewer would.

The practical takeaway: don't just make the visible tests pass and stop thinking. Read each docstring carefully and ask yourself, *what's the edge case here?* An empty list. A zero. A negative number. A value exactly on a threshold. If your function only handles the "obviously normal" case, it's incomplete, even if every visible test is green.

## Why Order of Implementation Matters

The lab has you implement `load_harvest_data` first, even though it's arguably the least interesting function. That's deliberate: every other function in this lab consumes the data that function produces. If it's wrong, every function built on top of it will fail in confusing ways that have nothing to do with the function you're actually debugging. Building bottom-up, verifying your foundation before building on it, is a habit worth keeping far beyond this lab.

---

## Worked Example: Read This Before You Open `functions.py`

`starter/functions.py` includes one function that's already fully written for you: `average_moisture`. It's not one of your five tasks, it exists purely so you have a working, correct example of the pattern to copy before you write your own.

Here's the same code, explained line by line:

```python
def average_moisture(records):
    total_moisture = 0.0                          # start a running total at zero

    for plot in records:                           # go through each plot's dict, one at a time
        total_moisture = total_moisture + plot["moisture_pct"]   # add this plot's value in

    average = total_moisture / len(records)         # total divided by count = average
    return average                                   # send the answer back
```

Every one of your five tasks follows a version of this same shape: **take the input you're given, loop over it if it's a list, pull out the field(s) you need, do one calculation, return the answer.** `yield_per_dunam` doesn't even need a loop, it's one division. `summarize_season` loops multiple times for different pieces of the summary. But the underlying pattern, access a value, calculate, return, is the same one shown above.

Open `starter/functions.py` now and try running `average_moisture` yourself using the command in the comment right below it, before writing anything. Seeing it actually work is worth more than reading about it.

## Worked Example: Reading a CSV File

`load_harvest_data` is your first task, and it's also the one with the least obvious starting point if you haven't read a CSV file in Python before. Here's a small, separate example, reading a *different*, simpler file than the one you'll actually work with, that shows the exact pattern:

Imagine a file `pets.csv` containing:
```
name,age
Simba,3
Luna,5
```

This code reads it into a list of dictionaries:

```python
import csv

with open("pets.csv", newline="") as f:
    reader = csv.DictReader(f)
    pets = []
    for row in reader:
        pets.append({
            "name": row["name"],
            "age": float(row["age"]),   # convert from string to a number
        })

print(pets)
# [{'name': 'Simba', 'age': 3.0}, {'name': 'Luna', 'age': 5.0}]
```

Three things to notice:
1. `csv.DictReader(f)` turns each row into a dictionary automatically, using the header row (`name,age`) as the keys.
2. `row["age"]` comes out as the *string* `"3"`, not the number `3`, every value from a CSV is a string by default, no matter what it looks like. Wrapping it in `float(...)` converts it to an actual number you can do math with.
3. We build a brand-new list (`pets`) by appending one dictionary per row, rather than trying to modify the CSV data in place.

`load_harvest_data` needs the same three ideas, `csv.DictReader`, converting the numeric columns with `float(...)`, and building a list of dictionaries, just with the harvest data's actual column names instead of `name` and `age`.

---

## Check Your Understanding

Think through these before opening `README.md`. Nothing here is submitted or graded.

1. Why is raising an error usually better than returning a fallback value like `0` or `None` when a function receives bad input?
2. You read a CSV column called `price` and try to do `total = total + row["price"]`, and Python raises a `TypeError`. What's the most likely cause?
3. A function passes all of your own tests, but fails a hidden test during grading. What does that most likely mean about your test coverage, not your code?
4. Why does it make sense to fully implement and trust `load_harvest_data` before writing any of the functions that use its output?

# Lesson, Why This Project Is Different From Modules 1 and 2

Read this before starting the project in `README.md`. This isn't graded, it's the thinking you need before the project makes sense.

## First, A Quick Check

This project assumes you're comfortable with everything from Module 1 (Git branching, commits, PRs) and Module 2 (writing Python functions, reading a CSV, raising errors). If either of those still feels shaky, go back and re-do the relevant module before starting this one, this project builds on both at once.

## Why This Project Has No Starter Code

Module 1 and Module 2 gave you exact functions to implement, with exact expected answers. This project doesn't, because you're choosing your own data. There's no "correct" total when the numbers come from your own life. That's intentional, this is your first taste of open-ended work: you decide what to build, and it gets judged on whether it's complete and well-made, not on whether it matches a hidden answer key.

You'll see this same pattern again later in the program (an "Open Test"), this project is a gentle, early introduction to it.

## Why This Matters For Your Portfolio

A recruiter or hiring manager looking at your GitHub doesn't care that you can follow instructions, dozens of other applicants can also follow instructions. What stands out is a small, complete, personal project, one where you clearly made real decisions: what to explore, what to measure, how to present it. This project is designed to be exactly that: small enough to finish in one sitting, personal enough to be genuinely yours, complete enough to link directly from your CV or LinkedIn.

## New Concept, A Simple Chart with matplotlib

Modules 1 and 2 never used a plotting library, everything was text and numbers. This project introduces exactly one new tool: `matplotlib`, specifically, one simple chart type.

**Step 1, Install it** (if you haven't already):
```bash
pip install matplotlib
```

**Step 2, The pattern you need, a bar chart:**

```python
import matplotlib.pyplot as plt

categories = ["Food", "Transport", "Entertainment"]
values = [450, 120, 80]

plt.bar(categories, values)
plt.title("My Spending by Category")   # state what the chart shows
plt.ylabel("Amount (JOD)")              # label your units
plt.tight_layout()                       # prevent labels from being cut off
plt.savefig("chart.png")                 # save it as a file, don't just plt.show()
```

That's the entire pattern: some labels, some numbers, `plt.bar()`, a title, an axis label, `tight_layout()`, then `savefig()` instead of `show()` (you want a file you can commit to your repo, not a window that pops up once and disappears).

**A line chart** (useful if your data has a time element, days of the week, weeks of the month):

```python
plt.plot(days, values, marker="o")
plt.title("My Study Hours This Week")
plt.ylabel("Hours")
plt.tight_layout()
plt.savefig("chart.png")
```

Pick whichever shape fits your data, bar charts compare categories, line charts show something changing over time. You only need one chart for this project, don't overbuild.

## What Makes a Docstring "Real," Not a Stub

The automated check for this project confirms your functions have docstrings, but a docstring that just repeats the function name isn't the point. Compare:

```python
def compute_summary(data):
    """Computes summary."""       # technically a docstring, tells you nothing
```

```python
def compute_summary(data):
    """Return the total, average, and highest single value from `data`."""  # actually useful
```

Write the second kind. Six months from now, a docstring like the second one means you don't have to re-read your own function to remember what it does, that's the entire point of writing one.

---

## Check Your Understanding

Nothing here is submitted, but think through these before opening `README.md`:

1. Why doesn't this project have exact "correct answers" the way Modules 1 and 2 did?
2. When would you use a bar chart instead of a line chart?
3. What's the difference between `plt.show()` and `plt.savefig()`, and why does this project need the second one?

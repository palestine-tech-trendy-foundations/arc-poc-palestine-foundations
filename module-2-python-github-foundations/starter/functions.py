"""
Module 2 — Python & GitHub Foundations
Scenario: Olive Harvest Analysis

You're helping a small olive-growing cooperative in Palestine analyze this
season's harvest data across several plots. Implement the four functions
below. Each one has a docstring explaining exactly what it must do.

Do not import any external libraries — everything here is solvable with
plain Python (loops, conditionals, dictionaries, basic arithmetic). This
mirrors real early-career work: most data problems don't need a heavy
library, they need clear logic.

Run your own tests locally before pushing:
    python -m pytest module-2-python-github-foundations/tests/
"""

import csv


# ============================================================
# WORKED EXAMPLE — already implemented. Read this before you
# touch anything below it. It's not one of your five tasks —
# it's here to show you the pattern you'll use for all of them.
# ============================================================

def average_moisture(records):
    """
    WORKED EXAMPLE (already done for you).

    Given `records` (a list of dicts shaped like the output of
    load_harvest_data), return the average moisture_pct across all plots,
    as a float.
    """
    # Step 1: `records` is a list of dictionaries — one dict per plot.
    # We need a running total to add each plot's moisture_pct into.
    total_moisture = 0.0

    # Step 2: loop over every plot's dictionary, one at a time.
    for plot in records:
        # Step 3: pull out just the "moisture_pct" value from this plot's
        # dict, and add it to our running total.
        total_moisture = total_moisture + plot["moisture_pct"]

    # Step 4: "average" means total divided by count. len(records) gives
    # us how many plots (dictionaries) are in the list.
    average = total_moisture / len(records)

    # Step 5: return the single number we calculated.
    return average


# Try it yourself before moving on: open a terminal in this folder and run
#   python3 -c "from functions import average_moisture; print(average_moisture([{'moisture_pct': 40.0}, {'moisture_pct': 44.0}, {'moisture_pct': 42.0}]))"
# You should see 42.0. Notice this works right now, before you've written
# any of the five functions below — average_moisture is already complete,
# and this call builds its own tiny sample data by hand instead of relying
# on load_harvest_data (which you haven't written yet). That's the exact
# pattern you'll repeat for every task below: take a list of dicts, loop
# over it, pull out one field, calculate, return.


# ============================================================
# YOUR TASKS — implement these five. Each docstring tells you
# exactly what's expected. Use the same pattern as the worked
# example above: loop over records, pull out the field you need,
# do the calculation, return the result.
# ============================================================

def load_harvest_data(filepath):
    """
    Read the harvest CSV at `filepath` and return a list of dictionaries,
    one per plot, with these keys and types:
        - "plot_id": str
        - "region": str
        - "dunams": float
        - "kg_harvested": float
        - "moisture_pct": float

    The CSV columns are: plot_id, region, dunams, kg_harvested, moisture_pct

    Hint: use csv.DictReader, then convert the numeric fields from strings
    to floats — CSV values are read as strings by default.
    """
    # TODO: implement this function
    raise NotImplementedError


def yield_per_dunam(kg_harvested, dunams):
    """
    Return the yield in kilograms per dunam, as a float.

    Raise a ValueError with any message if `dunams` is less than or equal
    to zero (you can't divide by zero or a negative area).
    """
    # TODO: implement this function
    raise NotImplementedError


def estimate_oil_liters(kg_harvested, extraction_rate=0.18):
    """
    Estimate the liters of olive oil produced from `kg_harvested` kilograms
    of olives, given an `extraction_rate` (default 0.18, i.e. 18% — a
    realistic average extraction rate).

    Formula: kg_harvested * extraction_rate

    Raise a ValueError if kg_harvested is negative.
    """
    # TODO: implement this function
    raise NotImplementedError


def flag_underperforming_plots(records, threshold_kg_per_dunam):
    """
    Given `records` (a list of dicts shaped like the output of
    load_harvest_data), return a list of plot_id strings for every plot
    whose yield-per-dunam is strictly below `threshold_kg_per_dunam`.

    The returned list should preserve the original order of `records`.
    Use your `yield_per_dunam` function inside this one — don't
    recalculate the formula again.
    """
    # TODO: implement this function
    raise NotImplementedError


def summarize_season(records):
    """
    Given `records` (a list of dicts shaped like the output of
    load_harvest_data), return a single dictionary summarizing the season:

        {
            "total_kg": float,             # sum of kg_harvested across all plots
            "total_dunams": float,         # sum of dunams across all plots
            "average_yield_per_dunam": float,  # total_kg / total_dunams
            "best_plot_id": str,           # plot_id with the highest yield per dunam
            "worst_plot_id": str,          # plot_id with the lowest yield per dunam
        }

    Raise a ValueError if `records` is empty — there's nothing to summarize.
    """
    # TODO: implement this function
    raise NotImplementedError

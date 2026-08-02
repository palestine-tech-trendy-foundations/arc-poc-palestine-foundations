"""
Visible tests for Module 2. Run these yourself as you build:
    python -m pytest module-2-python-github-foundations/tests/ -v

Passing all of these is a strong sign you're ready to push, but the
autograder in CI also runs one or two additional hidden checks on top of
these, the same way a real code review catches things your own tests
didn't think of.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "starter"))

import pytest
from functions import (
    average_moisture,
    load_harvest_data,
    yield_per_dunam,
    estimate_oil_liters,
    flag_underperforming_plots,
    summarize_season,
)

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "harvest_data.csv")


def test_worked_example_average_moisture():
    # This test should already pass, right out of the box: average_moisture
    # is the worked example in functions.py, not one of your five tasks.
    # It uses hand-built sample data, not load_harvest_data, on purpose:
    # you haven't implemented load_harvest_data yet at this point, and this
    # test should pass before you've written a single line of your own.
    # If this fails, something's wrong with your environment/setup, not
    # your code: check the Troubleshooting section in README.md.
    sample_records = [{"moisture_pct": 40.0}, {"moisture_pct": 44.0}, {"moisture_pct": 42.0}]
    assert average_moisture(sample_records) == pytest.approx(42.0)


def test_load_harvest_data_returns_correct_count():
    records = load_harvest_data(DATA_PATH)
    assert len(records) == 8


def test_load_harvest_data_types_are_numeric():
    records = load_harvest_data(DATA_PATH)
    first = records[0]
    assert isinstance(first["dunams"], float)
    assert isinstance(first["kg_harvested"], float)
    assert isinstance(first["moisture_pct"], float)
    assert isinstance(first["plot_id"], str)


def test_yield_per_dunam_basic():
    assert yield_per_dunam(950, 5) == pytest.approx(190.0)


def test_yield_per_dunam_rejects_zero_dunams():
    with pytest.raises(ValueError):
        yield_per_dunam(500, 0)


def test_yield_per_dunam_rejects_negative_dunams():
    with pytest.raises(ValueError):
        yield_per_dunam(500, -2)


def test_estimate_oil_liters_default_rate():
    assert estimate_oil_liters(1000) == pytest.approx(180.0)


def test_estimate_oil_liters_custom_rate():
    assert estimate_oil_liters(1000, extraction_rate=0.2) == pytest.approx(200.0)


def test_estimate_oil_liters_rejects_negative_kg():
    with pytest.raises(ValueError):
        estimate_oil_liters(-50)


def test_flag_underperforming_plots():
    records = load_harvest_data(DATA_PATH)
    flagged = flag_underperforming_plots(records, threshold_kg_per_dunam=150)
    assert flagged == ["P02", "P05", "P08"]


def test_flag_underperforming_plots_preserves_order():
    records = load_harvest_data(DATA_PATH)
    flagged = flag_underperforming_plots(records, threshold_kg_per_dunam=1000)
    # with a very high threshold, everything should be flagged, in original order
    assert flagged == [r["plot_id"] for r in records]


def test_summarize_season_totals():
    records = load_harvest_data(DATA_PATH)
    summary = summarize_season(records)
    assert summary["total_kg"] == pytest.approx(6355.0)
    assert summary["total_dunams"] == pytest.approx(38.0)


def test_summarize_season_best_and_worst():
    records = load_harvest_data(DATA_PATH)
    summary = summarize_season(records)
    assert summary["best_plot_id"] == "P03"
    assert summary["worst_plot_id"] == "P08"


def test_summarize_season_rejects_empty_records():
    with pytest.raises(ValueError):
        summarize_season([])

"""
Output-contract checks for the Module 3 portfolio project. There is no
answer key here, your data is your own, so these checks confirm your
submission is COMPLETE and REAL, not that any particular number is
correct.

Run locally as you work:
    python -m pytest module-3-portfolio-project/tests/ -v
"""

import ast
import csv
import os

PROJECT_DIR = os.path.join(os.path.dirname(__file__), "..")
DATA_PATH = os.path.join(PROJECT_DIR, "data", "my_data.csv")
PROJECT_PY_PATH = os.path.join(PROJECT_DIR, "project.py")
CHART_PATH = os.path.join(PROJECT_DIR, "chart.png")
PROJECT_MD_PATH = os.path.join(PROJECT_DIR, "PROJECT.md")

MIN_ROWS = 10
MIN_COLUMNS = 3  # at least 2 data columns beyond an id/date column
MIN_FUNCTIONS = 3
MIN_DOCSTRING_LENGTH = 15  # filters out stubs like "Computes summary."
REQUIRED_PROJECT_MD_SECTIONS = [
    "## About This Project",
    "## What I Found",
    "## Skills Used",
]


def test_data_csv_exists_with_enough_rows_and_columns():
    assert os.path.exists(DATA_PATH), (
        f"Expected {DATA_PATH} to exist. See Step 2 in README.md."
    )
    with open(DATA_PATH, newline="", encoding="utf-8") as f:
        reader = list(csv.reader(f))
    assert len(reader) >= 1, "my_data.csv appears to be empty."
    header, rows = reader[0], reader[1:]
    assert len(header) >= MIN_COLUMNS, (
        f"my_data.csv has {len(header)} column(s), expected at least {MIN_COLUMNS} "
        f"(an id/date column plus at least 2 data columns)."
    )
    assert len(rows) >= MIN_ROWS, (
        f"my_data.csv has {len(rows)} data row(s), expected at least {MIN_ROWS}."
    )


def test_project_py_has_enough_functions_with_real_docstrings():
    assert os.path.exists(PROJECT_PY_PATH), (
        f"Expected {PROJECT_PY_PATH} to exist. See Step 4 in README.md."
    )
    with open(PROJECT_PY_PATH, encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename="project.py")

    functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    assert len(functions) >= MIN_FUNCTIONS, (
        f"Found {len(functions)} function(s) in project.py, expected at least "
        f"{MIN_FUNCTIONS}. See Step 4 in README.md."
    )

    problems = []
    for fn in functions:
        docstring = ast.get_docstring(fn)
        if not docstring:
            problems.append(f"`{fn.name}` has no docstring")
        elif len(docstring.strip()) < MIN_DOCSTRING_LENGTH:
            problems.append(
                f"`{fn.name}`'s docstring is too short to be useful "
                f"(\"{docstring.strip()}\"), see 'What Makes a Docstring "
                f"Real' in LESSON.md"
            )
        # crude stub detector: a body of just `pass` or `...`
        real_statements = [
            stmt for stmt in fn.body
            if not (isinstance(stmt, ast.Expr) and isinstance(stmt.value, (ast.Constant,)))
        ]
        non_pass_statements = [s for s in real_statements if not isinstance(s, ast.Pass)]
        if len(non_pass_statements) == 0:
            problems.append(f"`{fn.name}` appears to be an empty stub (no real implementation)")

    assert not problems, "Issues found in project.py:\n    " + "\n    ".join(problems)


def test_chart_png_exists_and_is_a_valid_image():
    assert os.path.exists(CHART_PATH), (
        f"Expected {CHART_PATH} to exist. See Step 5 in README.md."
    )
    with open(CHART_PATH, "rb") as f:
        header = f.read(8)
    png_signature = b"\x89PNG\r\n\x1a\n"
    assert header == png_signature, (
        "chart.png does not appear to be a valid PNG file (bad file header). "
        "Make sure you saved it with plt.savefig(...), not renamed some other file."
    )


def test_project_md_has_required_sections():
    assert os.path.exists(PROJECT_MD_PATH), (
        f"Expected {PROJECT_MD_PATH} to exist. See Step 6 in README.md."
    )
    with open(PROJECT_MD_PATH, encoding="utf-8") as f:
        content = f.read()
    missing = [s for s in REQUIRED_PROJECT_MD_SECTIONS if s not in content]
    assert not missing, f"PROJECT.md is missing required section(s): {missing}"


def test_project_md_what_i_found_is_substantive():
    with open(PROJECT_MD_PATH, encoding="utf-8") as f:
        content = f.read()
    start = content.find("## What I Found")
    end = content.find("##", start + 1)
    section = content[start:end if end != -1 else None]
    word_count = len(section.split())
    assert word_count >= 15, (
        "The 'What I Found' section looks too short to contain 2 real "
        "findings with actual numbers from your data."
    )

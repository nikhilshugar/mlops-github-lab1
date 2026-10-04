# GitHub Lab 1 - Unit Testing and GitHub Actions

![Pytest](https://github.com/nikhilshugar/mlops-github-lab1/actions/workflows/pytest_action.yml/badge.svg)
![Unittest](https://github.com/nikhilshugar/mlops-github-lab1/actions/workflows/unittest_action.yml/badge.svg)

My version of GitHub Lab 1 from the MLOps course. The original lab has a small calculator module with pytest and unittest tests, and GitHub Actions workflows that run the tests on every push. I added more functions and tests, and fixed the workflows so they actually run on GitHub.

Original lab: [course repo](https://github.com/raminmohammadi/MLOps/tree/main/Labs/Github_Labs/Lab1)

## Changes from the original lab

- calculator.py: added fun5 (division, raises ZeroDivisionError when dividing by 0) and fun6 (power). fun4 now rejects non-number inputs like the other functions.
- test_pytest.py: added tests for the new functions and for invalid input, using pytest.mark.parametrize and pytest.raises (19 tests, up from 4).
- test_unittest.py: same new checks written with assertRaises and subTest (9 tests, up from 4).
- Moved the workflow files to .github/workflows so GitHub runs them.
- Fixed the pytest workflow: run-nam typo, and branches + branches-ignore can't be used together. Removed the label/issues triggers and added a pull_request trigger to both workflows.
- Updated the actions to current versions (upload-artifact@v2 no longer works) and replaced Python 3.8. The pytest workflow now runs on Python 3.12, 3.13 and 3.14 using a matrix, and the unittest workflow runs on 3.14.
- Pinned the pytest version in requirements.txt.

## How to run the tests locally

```
python -m venv .venv
.venv\Scripts\activate            (Mac/Linux: source .venv/bin/activate)
pip install -r requirements.txt
pytest
python -m unittest test.test_unittest
```

pytest runs both test files (28 tests). The unittest command runs only test_unittest.py (9 tests).

## GitHub Actions

Both workflows run on every push and pull request to main. Results are in the Actions tab, and the pytest workflow uploads a test report (pytest-report.xml) for each Python version as an artifact.
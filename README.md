# Web Blog Tests (Demo Project)

Minimal Python project for demonstrating unit/integration/e2e tests and code quality tools.

## Requirements
- Python 3.11.9
- Virtual environment (`venv`)

## Setup
```bash
python -m venv .venv
.\.venv\Scripts\activate     # Windows
source .venv/bin/activate    # Linux/macOS
pip install -r requirements.txt
```


## Run
# All tests (unittest)
python -m unittest discover -s tests -p "*test.py" -v

# ruff / pylint / mypy
python -m ruff check .
python -m pylint blog.py post.py app.py tests
python -m mypy .

## Coverage

# clearing previous data
python -m coverage erase

# running the tests with coverage (unittest + template "*_test.py")
python -m coverage run -m unittest discover -s tests -p "*_test.py" -v

# console report (also shows files with 100% coverage)
python -m coverage report -m

# HTML report (open htmlcov/index.html in a browser)
python -m coverage html

### Expected output (example):



```text
Name      Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------
app.py       48      2     18      0  93.9%   116-117
blog.py      14      0      2      0 100.0%
post.py       8      0      0      0 100.0%
-----------------------------------------------------
TOTAL        70      2     20      0  95.6%



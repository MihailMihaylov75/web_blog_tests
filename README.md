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

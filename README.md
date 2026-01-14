# Python TDD Workshop

Welcome to the TDD Workshop! We will be practicing Test-Driven Development using Python and `pytest`.

## Setup

1. Ensure you have `uv` installed.
2. Clone this repository.
3. Run `uv sync` to install dependencies and create a virtual environment.

## Running Tests

To run all tests:
```bash
uv run pytest
```

To run tests for a specific kata:
```bash
uv run pytest fizzbuzz/
# or
uv run pytest string_calculator/
```

## The TDD Cycle
1. **Red**: Write a failing test.
2. **Green**: Write the minimum code to make the test pass.
3. **Refactor**: Clean up the code while keeping tests green.

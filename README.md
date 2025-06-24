# learning-python

Project to explore Python's possibilities:

1. Writing functions to try out different Python's language feature, and write associated tests
2. Try out the tooling that exists in the Python ecosystem:
   - How to create a project from scratch
   - Experiment with the linters, formatters, unit testing tools, mutation tests, etc

## Project requirements

### Install uv globally

Install uv globally on the system, following uv's official doc.

For Manjaro, it can be handled by the package manager:

```
    sudo pacman -S python-uv
```

### Install dependencies from lockfile

Run

```
    uv sync
```

### Running the tests

There is no feature per se in this project, only a list of language features with associated unit tests to try out different possibilities:

Run the tests with:

```
    uv run pytest
```

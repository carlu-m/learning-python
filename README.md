# learning-python

Project to explore Python's possibilities:

## Overview of the project and goals

### Language features

Learn & try out the pure language features:

- Writing functions to try out different Python's language features (basic primitives & basic syntax, pattern matching, destructuration, functions' signatures, etc)
- Write the associated unit tests to experiment and have a reference for later (instead of doing everything in the REPL) and see what works / does not work visually

### Ecosystem tooling

Learn about the ecosystem's tooling & experiment with it

Things that have been tested for now / list of ideas for later:

- [X] Learn about the several tools that exist in Python (scaffolding, dependency management, etc)
- [X] Learn about the basic architecture & files expected in a project, the different types of projects, etc
- [X] Learn about the different ways to manage dependencies and their caveats
- [X] Creating the project from scratch (here uv was chosen to handle a lot of things)
- [X] Add a linter
- [X] Add a formatter
- [X] Add a pre-commit linting & formatting hook
- [X] Create unit tests
- [X] Configure test coverage
- [ ] Setup & configure mutation testing

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

### Running the unit tests using pytest

There is no feature per se in this project, only a list of language features with associated unit tests to try out different possibilities:

Run the tests with:

```
    uv run pytest
```

### Running the mutation tests using cosmic-ray

In order to run the mutation tests, a two-step process is needed.
For now, the tests are not parallelized.

Needed improvements for a real use case:
[ ] Use workers even locally to avoir mutating the original code
[ ] Parallelize the tests in an automated fashion (i.e. not having to start the servers manually)
[ ] Get the code directly from github (for tests run from a CI for example)

#### Prepare a database to persist the session's results

First we need to start a session to store the results. In our case, we'll do it everytime we run the tests:

```
    uvx cosmic-ray init pyproject.toml mutation-tests.sqlite
```

#### Run the mutations

As per the official documentation and if running the tests in a local dev environment, **commit your code**
It shouldn't happen but technically, mutations can fail to be reverted since the real code is being mutated.

Then, run the tests themselves with:

```
    uvx cosmic-ray exec pyproject.toml mutation-tests.sqlite
```

#### Check / persist the report

Finally, once the exec has finished running (or even while it is running), check the results / progress with

```
    uv run cr-report mutation-tests.sqlite --show-pending
```

Or if you want to keep the results / want a report that's a bit more readable:

```
    uv run cr-html mutation-tests.sqlite > mutation-tests-report.html
```
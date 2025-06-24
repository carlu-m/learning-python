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

### Running the tests

There is no feature per se in this project, only a list of language features with associated unit tests to try out different possibilities:

Run the tests with:

```
    uv run pytest
```

# learning-python

![badge-for-mutation-testing-score](./mutation-testing-badge.svg)

Project to explore Python's possibilities:

## Overview of the project and goals

### Language features

Learn & try out the pure language features:

- Writing functions to try out different Python's language features (basic primitives & basic syntax, pattern matching, destructuration, functions' signatures, etc)
- Write the associated unit tests to experiment and have a logged / shareable reference for later (instead of doing everything in the REPL) and see what works / does not work visually

### Ecosystem tooling

Learn about the ecosystem's tooling & experiment with it.

NB: the test coverage & mutation tests are only based on a single module, which exists only for these reports, as a proof of concept.
The rest of Python's features which are being tried out are directly in the test files, since it would be annoying / redundant to have to create functions for really simple cases (e.g. create a function just to test an operator, f-strings, etc), and these won't generate coverage results (since there is no module).

Things that have been tested for now / list of ideas for later:

- [X] Learn about the several tools that exist in Python (scaffolding, dependency management, etc)
- [X] Learn about the basic architecture & files expected in a project, the different types of projects, etc
- [X] Learn about the different ways to manage dependencies and their caveats
- [X] Creating the project from scratch (here uv was chosen to handle a lot of things)
- [X] Add a linter
- [X] Add a formatter
- [X] Configure ruff to implement PEP 8 conventions
- [X] Configure ruff to implement additionally chosen rules
- [X] Add a pre-commit linting & formatting hook
- [ ] Doctest to run your code against your documentation
- [X] Create unit tests
- [X] Configure test coverage
- [ ] Read pytest's doc to know about its features beyond the basic ones
- [X] Compare mutation testing libraries
- [X] Setup & configure mutation testing with the chosen lib (cosmic-rays)
- [X] Read cosmic-ray's doc to know about its features beyond the basic ones

## Limitations & potential improvements

- Linting rules exclude test files (which represent most of this project), so, apart from reading about them and adding them, I didn't really experiment with them
- Mutation tests in a CI job / step would have to be adapted to take the parallelization into account, and we would need to manually ready the last line of the report to check for the score if we want to automatically succeed / fail the step.

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

In order to run the mutation tests, a three-step process is needed.
For now, the tests are not parallelized.

#### Start the workers to parallelize the tests

By default, running the tests locally will mutate your original code instead of a copy, and the tests won't be run in parallel.
To avoid that, the config we use will start servers to parallelize the tests over multiple workers, by using this command:

```
    uv run cr-http-workers pyproject.toml .
```

To get the code to copy for each worker from github, replace `.` at the end of the command with your repo's URL.
Here we copy the local code to the workers' directories.

For now there are two workers in the config, but you can add more as needed.

#### Prepare a database to persist the session's results

Then, we need to start a session to store the results. In our case, we'll do it everytime we run the tests:

```
    uvx cosmic-ray init --force pyproject.toml mutation-tests.sqlite
```

#### Run the mutations

Then, in another terminal, run the tests themselves with:

```
    uvx cosmic-ray exec pyproject.toml mutation-tests.sqlite
```

Since the config uses the `http` mode instead of `local`, ait will use the workers we've defined in the config and parallelize the tests on them automatically.
You will see logs on the terminal with the servers as the tests are being processed.

#### Check / persist the report

Finally, once the exec has finished running, export the results with:

```
    uv run cr-html mutation-tests.sqlite > mutation-tests-report.html
```

This file should be commited before merging each branch as proof that the mutation tests have been run.
Because of the parallelized nature of the mutation tests, there is no way to "fail" them, unlike when running the coverage command, and unlike other mutation tools in other languages, so this is the next best thing for now.

If you're done with the workers, you can kill the processes in the relevant terminal.
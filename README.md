# learning-python

![badge-for-mutation-testing-score](./mutation-testing-badge.svg)

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
- [ ] Configure ruff to implement PEP 8 conventions
- [ ] Configure ruff to implement the chosen rules
- [X] Add a pre-commit linting & formatting hook
- [X] Create unit tests
- [X] Configure test coverage
- [X] Setup & configure mutation testing

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

Needed improvements for a real use case:
[ ] Parallelize the tests in an automated fashion (i.e. not having to start the servers manually)
[ ] Make badge generation automatic so that the badge always reflects the latest score (instead of the score of the latest committed svg)

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

Finally, once the exec has finished running (or even while it is running), check the results / progress with

```
    uv run cr-report mutation-tests.sqlite --show-pending
```

Or if you want to keep the results / want a report that's a bit more readable:

```
    uv run cr-html mutation-tests.sqlite > mutation-tests-report.html
```

If you're done with the workers, you can kill the processes in the relevant terminal.

#### Generate the badge

There is currently no option to "fail" the mutation step like for test coverage.
So, instead, what we can do is generate a badge to at least make it visible:

```
    uv run cr-badge pyproject.toml mutation-testing-badge mutation-tests.sqlite
```

It does have some caveat in the current version though, we need to run the tests locally, generate the badge, and commit the svg, so a lot of manual steps are involved (and rely on a developper's good-will / remembering the steps)
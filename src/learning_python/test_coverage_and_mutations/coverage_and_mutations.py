"""Module created only for the sake of test coverage & mutation reports.

Note: the modules here only exist to generate coverage & mutation results.
For the language experiments, have a look at the tests folder directly
"""


def simple_pattern_matching(param: str) -> str:
    """Small function to generate coverage & mutation reports.

    This function is merely here to create a module that will allow the
    generation of a unit test coverage report, as well as mutation tests report
    """
    match param:
        case "OK":
            return "OK"

        case "KO" | "Unknown":
            return "KO"

        case _:
            return "default"

# References:
# https://docs.python.org/3/tutorial/controlflow.html
# https://peps.python.org/pep-0636/


def simple_pattern_matching(param):
    """Small function to generate coverage & mutation reports

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

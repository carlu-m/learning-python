# References:
# https://docs.python.org/3/tutorial/controlflow.html
# https://peps.python.org/pep-0636/


def simple_pattern_matching(param):
    """Small function to test pattern matching for simple cases"""
    match param:
        case "OK":
            return "OK"

        case "KO":
            return "KO"

        case "1":
            return "string 1"

        case 1:
            return "integer 1"

        # Multiple options on one line
        case "inlineOne" | "inlineTwo":
            return "inline conditions"

        # Works in JS, does not work in Python
        # case "successiveOne":
        # case "successiveTwo":
        #     return "successive"

        # Multiple potentially complex conditions over multiple lines:
        case (
            "thisIsAnExtremelyLongSuccessiveOne"
            | "thisIsAnExtremelyLongSuccessiveTwo"
        ):
            return "successive conditions"

        case _:
            return "default case"


def tuple_pattern_matching(tup):
    """Small function to test pattern matching for tuples"""
    match tup:
        case (0, 0):
            return "explicitely got two 0"

        case (0, _y):
            return "got explicit 0 and any other value"

        case (_x, 0):
            return "got any value and an explicit 0"

        case (_x, _y):
            return "got any two values which are not 0"

        case (_x, _y, *_):
            return "got any tuple with 2+ items: does not get caught by previous cases"

        case _:
            return "default case"


def array_pattern_matching(arr):
    """Small function to test pattern matching for arrays"""
    match arr:
        case []:
            return "explicit empty array"

        case [0, 0]:
            return "explicitely two 0"

        case [0, _x]:
            return "got explicit 0 and any other value"

        case [0, *_]:
            return "array starting with 0 and with 2+ items"

        case [*_]:
            return "catch all non-previously covered cases of arrays with undetermined lengths"

        case _:
            return "default case"


def object_pattern_matching(obj):
    """Small function to test pattern matching for objects"""
    match obj:
        # NB: Would catch all objects, _not_ empty objects
        # case {}:
        #     return "empty object"

        # Need to use a guard to check emptiness
        case {**properties} if not properties:
            return "empty object"

        case {"test": "OK"}:
            return "got test property with OK value"

        case {"test": "KO"}:
            return "got test property with KO value"

        case {"test": _}:
            return "got test property with any value other than OK or KO"

        case _:
            return "default case"

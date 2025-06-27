# References:
# https://docs.python.org/3/tutorial/controlflow.html
# https://peps.python.org/pep-0636/


class TestSimplePatternMatching:
    def test_two_simple_string_cases(self):
        """Test basic pattern matching cases"""

        def private_pattern_matching(param):
            match param:
                case "OK":
                    return "OK"

                case "KO":
                    return "KO"

                case _:
                    return "default"

        assert private_pattern_matching("OK") == "OK"
        assert private_pattern_matching("KO") == "KO"
        assert private_pattern_matching("test") == "default"

    def test_unknown_case(self):
        """Test default case"""

        def private_pattern_matching(param):
            match param:
                case "OK":
                    return "OK"

                case _:
                    return "default"

        assert private_pattern_matching("OK") == "OK"
        assert private_pattern_matching("KO") == "default"
        assert private_pattern_matching("test") == "default"
        assert private_pattern_matching("") == "default"
        assert private_pattern_matching("unknownCase") == "default"

    def test_difference_between_string_and_integer(self):
        """Test string and integer being different cases"""

        def private_pattern_matching(param):
            match param:
                case "1":
                    return "string"

                case 1:
                    return "integer"

                case _:
                    return

        assert private_pattern_matching("1") == "string"
        assert private_pattern_matching(1) == "integer"

    def test_multiple_inline_conditions(self):
        """Test multiple different conditions in one case"""

        def private_pattern_matching(param):
            match param:
                case "inlineOne" | "inlineTwo":
                    return "inline conditions"

                case _:
                    return

        assert private_pattern_matching("inlineOne") == "inline conditions"
        assert private_pattern_matching("inlineTwo") == "inline conditions"

    def test_multiple_conditions_over_separate_lines(self):
        """Test syntax for multiple complex / long conditions in one case"""

        def private_pattern_matching(param):
            match param:
                case (
                    "thisIsAnExtremelyLongSuccessiveOne"
                    | "thisIsAnExtremelyLongSuccessiveTwo"
                ):
                    return "successive conditions"

                case _:
                    return

        assert (
            private_pattern_matching("thisIsAnExtremelyLongSuccessiveOne")
            == "successive conditions"
        )
        assert (
            private_pattern_matching("thisIsAnExtremelyLongSuccessiveTwo")
            == "successive conditions"
        )


class TestTuplePatternMatching:
    def test_two_items_tuple_permutations(self):
        """Test basic pattern matching on tuples"""

        def private_pattern_matching(tup):
            match tup:
                case (0, 0):
                    return "explicitely got two 0"

                case (0, _y):
                    return "got explicit 0 and any other value"

                case (_x, 0):
                    return "got any value and an explicit 0"

                case (_x, _y):
                    return "got any two values which are not 0"

                case _:
                    return "default"

        assert private_pattern_matching((0, 0)) == "explicitely got two 0"
        assert (
            private_pattern_matching((0, 1))
            == "got explicit 0 and any other value"
        )
        assert (
            private_pattern_matching((1, 0))
            == "got any value and an explicit 0"
        )
        assert (
            private_pattern_matching((1, 1))
            == "got any two values which are not 0"
        )
        assert private_pattern_matching((0)) == "default"
        assert private_pattern_matching((0, 0, 0)) == "default"

    def test_tuple_matching_exact_length(self):
        """Test case with x items not matching case with x-1 items"""

        def private_pattern_matching(tup):
            match tup:
                case (0, 0):
                    return "explicitely got two 0"

                case _:
                    return "not caught since not exact match"

        assert (
            private_pattern_matching((0, 0, 0))
            == "not caught since not exact match"
        )

    def test_any_type_for_dynamic_values(self):
        """Test dynamic matches matching anything"""

        def private_pattern_matching(tup):
            match tup:
                case (0, _y):
                    return "got explicit 0 and any other value"

                case (_x, 0):
                    return "got any value and an explicit 0"

                case _:
                    return "default"

        assert (
            private_pattern_matching((0, "a"))
            == "got explicit 0 and any other value"
        )
        assert (
            private_pattern_matching(([], 0))
            == "got any value and an explicit 0"
        )
        assert private_pattern_matching((1, 1)) == "default"

    def test_tuple_with_more_than_two_items(self):
        """Test dynamic size case"""

        def private_pattern_matching(tup):
            match tup:
                case (_x, _y, *_):
                    return "got any tuple with 2+ items"

                case _:
                    return "default"

        assert (
            private_pattern_matching((1, 2)) == "got any tuple with 2+ items"
        )
        assert (
            private_pattern_matching((1, 2, 3))
            == "got any tuple with 2+ items"
        )
        assert (
            private_pattern_matching((1, 2, 3, 4))
            == "got any tuple with 2+ items"
        )


class TestArrayPatternMatching:
    def test_array_pattern_matching(self):
        def private_pattern_matching(arr):
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
                    return "catch all other arrays"

                case _:
                    return "default"

        assert private_pattern_matching([]) == "explicit empty array"
        assert private_pattern_matching([0, 0]) == "explicitely two 0"
        assert (
            private_pattern_matching([0, 10])
            == "got explicit 0 and any other value"
        )
        assert (
            private_pattern_matching([0, 10, 99])
            == "array starting with 0 and with 2+ items"
        )
        assert (
            private_pattern_matching([1, 10, 99]) == "catch all other arrays"
        )
        assert private_pattern_matching("unknown") == "default"


class TestObjectPatternMatching:
    def test_empty_bracket_catching_eveything(self):
        """Empty brackets {} will catch all objects"""

        def private_pattern_matching(obj):
            match obj:
                case {}:
                    return "any object"

                case _:
                    return "non object"

        assert private_pattern_matching({}) == "any object"
        assert private_pattern_matching({"hello": "world"}) == "any object"
        assert private_pattern_matching("string") == "non object"

    def test_empty_object(self):
        """Need a guard to catch empty objects"""

        def private_pattern_matching(obj):
            match obj:
                # Need to use a guard to check emptiness
                case {**properties} if not properties:
                    return "empty object"

                case _:
                    return "default"

        assert private_pattern_matching({}) == "empty object"
        assert private_pattern_matching({"hello": "world"}) == "default"

    def test_property_values(self):
        """Pattern matching on specific properties' values"""

        def private_pattern_matching(obj):
            match obj:
                case {"status": "OK"}:
                    return "OK status"

                case {"status": "KO"}:
                    return "KO status"

                case {"status": _}:
                    return "Unknown status"

                case _:
                    return

        assert private_pattern_matching({"status": "OK"}) == "OK status"
        assert private_pattern_matching({"status": "KO"}) == "KO status"
        assert (
            private_pattern_matching({"status": "I'm a teapot"})
            == "Unknown status"
        )

    def test_no_matching_property(self):
        """Not matching a listed property"""

        def private_pattern_matching(obj):
            match obj:
                case {"status": _}:
                    return "Object with any status"

                case _:
                    return "Object with no status"

        assert (
            private_pattern_matching({"status": "whatever"})
            == "Object with any status"
        )
        assert (
            private_pattern_matching({"not_status": "whatever"})
            == "Object with no status"
        )

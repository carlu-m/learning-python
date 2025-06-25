import unittest

from learning_python.pattern_matching.pattern_matching import (
    simple_pattern_matching,
    tuple_pattern_matching,
    array_pattern_matching,
    object_pattern_matching,
)


class TestSimplePatternMatching(unittest.TestCase):
    def test_two_simple_string_cases(self):
        assert simple_pattern_matching("OK") == "OK"
        assert simple_pattern_matching("KO") == "KO"

    def test_difference_between_string_and_integer(self):
        assert simple_pattern_matching("1") == "string 1"
        assert simple_pattern_matching(1) == "integer 1"

    def test_multiple_inline_conditions(self):
        assert simple_pattern_matching("inlineOne") == "inline conditions"
        assert simple_pattern_matching("inlineTwo") == "inline conditions"

    def test_multiple_conditions_over_separate_lines(self):
        assert (
            simple_pattern_matching("thisIsAnExtremelyLongSuccessiveOne")
            == "successive conditions"
        )
        assert (
            simple_pattern_matching("thisIsAnExtremelyLongSuccessiveTwo")
            == "successive conditions"
        )

    def test_unknown_case(self):
        assert simple_pattern_matching("test") == "default case"
        assert simple_pattern_matching("") == "default case"
        assert simple_pattern_matching("unknownCase") == "default case"


class TestTuplePatternMatching(unittest.TestCase):
    def test_two_items_tuple_permutations(self):
        assert tuple_pattern_matching((0, 0)) == "explicitely got two 0"
        assert tuple_pattern_matching((0, 1)) == "got explicit 0 and any other value"
        assert tuple_pattern_matching((1, 0)) == "got any value and an explicit 0"
        assert tuple_pattern_matching((1, 1)) == "got any two values which are not 0"

    def test_any_type_for_dynamic_values(self):
        assert tuple_pattern_matching((0, "a")) == "got explicit 0 and any other value"
        assert tuple_pattern_matching(([], 0)) == "got any value and an explicit 0"

    def test_tuple_with_more_than_two_items(self):
        assert (
            tuple_pattern_matching((1, 2, 3, 4))
            == "got any tuple with 2+ items: does not get caught by previous cases"
        )

    def test_tuple_with_three_zeroes_is_not_caught_by_double_zero_case(self):
        assert (
            tuple_pattern_matching((0, 0, 0))
            == "got any tuple with 2+ items: does not get caught by previous cases"
        )

    def test_not_a_tuple(self):
        assert tuple_pattern_matching("test") == "default case"


class TestArrayPatternMatching(unittest.TestCase):
    def test_array_pattern_matching(self):
        assert array_pattern_matching([]) == "explicit empty array"
        assert array_pattern_matching([0, 0]) == "explicitely two 0"
        assert array_pattern_matching([0, 10]) == "got explicit 0 and any other value"
        assert (
            array_pattern_matching([0, 10, 99])
            == "array starting with 0 and with 2+ items"
        )
        assert (
            array_pattern_matching([1, 10, 99])
            == "catch all non-previously covered cases of arrays with undetermined lengths"
        )
        assert array_pattern_matching("unknown") == "default case"


class TestObjectPatternMatching(unittest.TestCase):
    def test_empty_object(self):
        assert object_pattern_matching({}) == "empty object"

    def test_test_property_values(self):
        assert (
            object_pattern_matching({"test": "OK"}) == "got test property with OK value"
        )
        assert (
            object_pattern_matching({"test": "KO"}) == "got test property with KO value"
        )
        assert (
            object_pattern_matching({"test": "Hello"})
            == "got test property with any value other than OK or KO"
        )

    def test_no_test_property(self):
        assert object_pattern_matching({"notTest": "whatever"}) == "default case"


if __name__ == "__main__":
    unittest.main()

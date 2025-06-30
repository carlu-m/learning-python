class TestSetCreation:
    def test_create_empty_set(self):
        """Specific syntax to create empty set"""
        assert isinstance({}, set) == False
        assert isinstance({}, object) == True
        assert isinstance(set(), set) == True

    def test_create_set(self):
        assert isinstance({}, set) == False
        assert isinstance({1}, set) == True
        assert isinstance(set([1]), set) == True
        assert isinstance({"apple"}, set) == True
        assert isinstance(set(["apple"]), set) == True

    def test_creation_with_func_and_single_string_uses_characters(
        self,
    ):
        assert set("hello") == {"h", "e", "l", "o"}
        assert set("hello") != {"hello"}

    def test_creation_with_braces_and_single_string_uses_string(self):
        assert {"hello"} == {"hello"}
        assert {"hello"} != {"h", "e", "l", "o"}


class TestSetInKeyword:
    def test_set_in_keyword(self):
        assert ("apple" in {"apple"}) == True
        assert ("apple" not in {"apple"}) == False


class TestSetItemUniqueness:
    def test_set_item_uniqueness(self):
        test_set = {"apple", "pear", "apple"}

        assert test_set == {"apple", "pear"}
        # Native ordering is random, so also sorting
        assert f"{sorted(test_set)}" == "['apple', 'pear']"


class TestSetEqualityWithoutOrdering:
    def test_set_ordering_importance(self):
        test_set = {"apple", "pear"}

        assert test_set == {"apple", "pear"}
        assert test_set == {"pear", "apple"}


class TestSetMathematicalOperations:
    def test_set_mathematical_union(self):
        """All elements from either sets"""
        assert {"apple", "pear"} | {"tomato"} == {"apple", "pear", "tomato"}

    def test_set_mathematical_intersection(self):
        """Elements in all sets"""
        assert {"apple", "pear"} & {"banana", "apple"} == {"apple"}

    def test_set_mathematical_difference(self):
        """Elements of the set on the left which are not in the others"""
        assert {"apple", "pear"} - {"pear"} == {"apple"}

    def test_set_mathematical_symmetric_difference(self):
        """Elements in either set but not both"""
        assert {"apple", "pear"} ^ {"pear", "tomato"} == {"apple", "tomato"}

    def test_loose_subset_operator(self):
        """Elements of left set are all in the set on the right

        Includes equality
        """
        assert ({"apple", "pear"} <= {"apple", "pear", "tomato"}) == True
        assert ({"apple", "pear"} <= {"apple", "pear"}) == True
        assert ({"apple", "pear"} <= {"apple", "banana"}) == False

    def test_strict_subset_operator(self):
        """Elements of left set are all in the set on the right

        Excludes equality
        """
        assert ({"apple", "pear"} < {"apple", "pear", "tomato"}) == True
        assert ({"apple", "pear"} < {"apple", "pear"}) == False
        assert ({"apple", "pear"} <= {"apple", "banana"}) == False

    def test_loose_superset_operators(self):
        """Elements of left set includes the whole set on the right

        Includes equality
        """
        assert ({"apple", "pear", "tomato"} >= {"apple", "pear"}) == True
        assert ({"apple", "pear"} >= {"apple", "pear"}) == True
        assert ({"apple", "banana"} >= {"apple", "pear"}) == False

    def test_strict_superset_operators(self):
        """Elements of left set includes the whole set on the right

        Excludes equality
        """
        assert ({"apple", "pear", "tomato"} > {"apple", "pear"}) == True
        assert ({"apple", "pear"} > {"apple", "pear"}) == False
        assert ({"apple", "banana"} > {"apple", "pear"}) == False


class TestSetComprehensions:
    def test_set_comprehensions(self):
        """Comprehensions for sets"""
        assert {letter for letter in "hello" if letter not in "h"} == {
            "e",
            "l",
            "o",
        }

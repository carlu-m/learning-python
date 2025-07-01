"""Experiments with lists-related features

References:
https://docs.python.org/3/tutorial/introduction.html#lists
"""

import pytest


class TestCreateListAndAccessItems:
    def test_list_creation_and_indexes(self):
        """Creation of a list and accessing items"""

        reference = ["a", "b", "c", "d"]

        assert reference[0] == "a"
        assert reference[1] == "b"
        assert reference[2] == "c"
        assert reference[3] == "d"


class TestIndexes:
    def test_negative_indexes(self):
        """Using negative indexes goes from the end"""

        reference = ["a", "b", "c", "d"]

        assert reference[-1] == "d"
        assert reference[-2] == "c"
        assert reference[-3] == "b"
        assert reference[-4] == "a"

    def test_getting_the_length(self):
        """Getting the length"""

        reference = ["a", "b", "c"]

        assert len(reference) == 3

    def test_index_beyond_length_is_error(self):
        """Creation of a list and accessing items"""

        reference = ["a", "b"]

        with pytest.raises(IndexError):
            reference[len(reference) + 1]

    def test_colon_syntax(self):
        """Using colon syntax"""

        reference = ["a", "b", "c", "d"]

        assert reference[:] == reference
        assert reference[0 : len(reference)] == reference
        assert reference[0:] == reference
        assert reference[: len(reference)] == reference

        assert reference[:3] == ["a", "b", "c"]
        assert reference[1:] == ["b", "c", "d"]
        assert reference[1:3] == ["b", "c"]

    def test_colon_syntax_does_not_throw(self):
        """Unlike accessing indexes directly, colon syntax does not throw"""

        reference = ["a", "b", "c", "d"]

        assert reference[-999:999] == reference


class TestConcatenation:
    def test_concatenation(self):
        """Concatenating lists"""

        assert (["a", "b", "c", "d"] + ["z"]) == ["a", "b", "c", "d", "z"]


class TestMutability:
    def test_mutability(self):
        """Lists are mutable"""

        reference = ["a", "b", "c"]
        reference[0] = "z"

        assert reference == ["z", "b", "c"]

        reference[1:2] = []

        assert reference == ["z", "c"]

    def test_append(self):
        """Lists are mutable"""

        reference = ["a", "b", "c"]
        reference.append("z")

        assert reference == ["a", "b", "c", "z"]


class TestNesting:
    def test_nesting(self):
        """Lists can be nested"""

        reference = [["a", "b"], ["c"]]

        assert reference[0] == ["a", "b"]
        assert reference[1] == ["c"]
        assert reference[0][1] == "b"

"""Experiments with string-related features

References:
https://docs.python.org/3/tutorial/introduction.html#text
https://docs.python.org/3/tutorial/inputoutput.html
"""


class TestStringWithBothQuotes:
    def test_string_creation_with_both_quotes(self):
        """Creation of strings using both single and double quotes

        NB: comments are to disable the formatter / linter,
        otherwise double quotes are pushed, per convention
        """

        # fmt: off
        assert "Python" == "Python"
        # fmt: on


class TestStringConcatenation:
    def test_side_by_side_string_concatenation(self):
        """Can concatenate side by side strings

        Frowned upon, don't use, need to disable the linter / formatter
        """

        # fmt: off
        assert "Py" "thon" == "Python"
        # fmt: on

    def test_concatenation_with_plus(self):
        """Can concatenate strings using + operator"""

        assert "Py" + "thon" == "Python"

    def test_breaking_long_strings(self):
        """Can break multipart strings with parenthesis

        This allows us to break them over multiple lines if needed
        Ex: linting rules preventing lines with too many characters
        """

        assert ("long" + " " + "string") == "long string"


class TestStringEscape:
    def test_escape_strings(self):
        """Can escape characters"""

        # fmt: off
        assert "quotes to escape\"" == 'quotes to escape"'
        # fmt: on

    def test_raw_strings(self):
        """Can use r'' syntax to not interpret characters"""

        assert r"no\nnew\nline" == "no\\nnew\\nline"


class TestStringMultiplication:
    def test_string_multiplication(self):
        """Can use * operator to replicate string patterns"""

        assert "He" * 3 == "HeHeHe"


class TestStringInterpolationWithFormat:
    def test_interpolation_with_format(self):
        """Can use .format for format strings

        Old way, not longer the prefered way, see string literals below
        """

        string_to_interpolate = "world"

        assert (
            "hello {}{}".format(string_to_interpolate, "!") == "hello world!"
        )


class TestStringInterpolationWithLiterals:
    def test_interpolation_with_f_string(self):
        """Can use f'{...}' syntax to interpolate strings

        Favored solution
        """

        string_to_interpolate = "world"

        assert f"hello {string_to_interpolate}" == "hello world"


class TestStringMultiline:
    def test_multiline(self):
        """Break strings over multiple lines

        Beware, indentation is kept, and there is a leading \\n
        Also works with single quotes
        """

        multiline_string = """
        multiple
        """

        indentation = 8 * " "

        string_with_indentation = (
            "\n" + indentation + "multiple\n" + indentation
        )

        assert multiline_string != "multiple"
        assert multiline_string != ("\n" + "mutliple" + "\n")
        assert multiline_string == string_with_indentation

    def test_multiline_without_newlines(self):
        """Prevent multiline syntax from adding newlines

        Can use backslash to prevent default behaviour
        of adding newlines to the string
        """

        multiline_string = """\
        multiple\
        """

        indentation = 8 * " "

        string_with_indentation = indentation + "multiple" + indentation

        assert multiline_string == string_with_indentation


class TestMultilineInterpolation:
    def test_multiline_interpolation(self):
        """Interpolation also works with multiline strings"""

        string_to_interpolate = "world"

        multiline_interpolation = f"""
        Hello
        {string_to_interpolate}
        """

        expected = """
        Hello
        world
        """

        assert multiline_interpolation == expected


class TestStringsAreSequences:
    def test_strings_are_lists(self):
        """Strings are sequences under the hood"""

        reference = "Hello world"

        assert reference[0] == "H"
        assert reference[1] == "e"
        assert reference[len(reference) - 1] == "d"
        assert reference[:3] == "Hel"

    def test_no_character_primitive(self):
        """There is no character type / primitive, just a string of length 1"""

        assert isinstance("H", str) == True

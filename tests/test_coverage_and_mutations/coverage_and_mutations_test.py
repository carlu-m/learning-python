from learning_python.test_coverage_and_mutations.coverage_and_mutations import (  # noqa: E501
    simple_pattern_matching,
)


class TestSimplePatternMatching:
    def test_two_simple_string_cases(self):
        assert simple_pattern_matching("OK") == "OK"
        assert simple_pattern_matching("KO") == "KO"
        assert simple_pattern_matching("Unknown") == "KO"

    def test_default_case(self):
        assert simple_pattern_matching("test") == "default"
        assert simple_pattern_matching("") == "default"
        assert simple_pattern_matching("unknownCase") == "default"
        assert simple_pattern_matching("1") == "default"
        assert simple_pattern_matching(1) == "default"

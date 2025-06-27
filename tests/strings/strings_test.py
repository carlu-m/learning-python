class TestStrings:
    def test_string_interpolation_with_f_string(self):
        string_to_interpolate = "world"

        assert f"hello {string_to_interpolate}" == "hello world"

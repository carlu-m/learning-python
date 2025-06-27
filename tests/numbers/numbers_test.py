class TestNumbersEquality:
    def test_integer_and_float_equality(self):
        assert 2.0 == 2


class TestAdditions:
    def test_integer_additions(self):
        assert 1 + 1 == 2

    def test_integer_and_float_additions(self):
        assert 1.0 + 1 == 2.0
        assert 1.0 + 1 == 2


class TestDivisions:
    def test_divisions(self):
        assert 10 / 2 == 5
        assert 10 / 4 == 2.5

    def test_default_division_rounding(self):
        assert 10 / 3 == 3.3333333333333335

    def test_non_fractionnal_divisions(self):
        assert 10 // 2 == 5
        assert 10 // 3 == 3
        assert 10 // 4 == 2

    def test_divisions_remainders(self):
        assert 10 % 2 == 0
        assert 10 % 3 == 1
        assert 10 % 4 == 2
        assert 10 % 5 == 0


class TestPowers:
    def test_powers(self):
        assert 2**2 == 4
        assert 2**3 == 8

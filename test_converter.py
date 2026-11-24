import unittest

from converter import convert_length, convert_weight, convert_temperature


class TestConverter(unittest.TestCase):
    def test_km_to_miles(self):
        self.assertAlmostEqual(convert_length(1, "km", "mi"), 0.621371, places=5)

    def test_kg_to_lbs(self):
        self.assertAlmostEqual(convert_weight(1, "kg", "lb"), 2.204623, places=5)

    def test_c_to_f(self):
        self.assertAlmostEqual(convert_temperature(100, "c", "f"), 212)

    def test_f_to_c(self):
        self.assertAlmostEqual(convert_temperature(32, "f", "c"), 0)

    def test_c_to_k(self):
        self.assertAlmostEqual(convert_temperature(0, "c", "k"), 273.15)


if __name__ == "__main__":
    unittest.main()

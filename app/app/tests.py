"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Tesdt the calc module."""

    def test_add_number(self):
        """Test adding number."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting number."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)

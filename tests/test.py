import unittest
from pathlib import Path

from src.replagex import Replagex
from src.replagex.pattern import Pattern


class TestReplagex(unittest.TestCase):
    def test_replagex_init(self):
        """
        Test Replagex constructor
        """
        rg = Replagex()
        self.assertIsInstance(rg, Replagex)

    def test_replagex_init_json(self):
        """
        Test Replagex constructor with JSON file
        """
        json_file = Path(Path('tests/fixtures/test.json'))

        rg = Replagex(json_file)
        self.assertIsInstance(rg, Replagex)

    def test_add_pattern(self):
        """
        Test Replagex add_pattern method.
        """
        rg = Replagex()

        rg.add_pattern(
            Pattern(
                '.*(Hello).*',
                'Replaced Text: $1'
            )
        )

    def test_add_wrong_pattern(self):
        """
        Test Replagex add_pattern method with wrong value.
        """
        rg = Replagex()

        with self.assertRaises(Exception):
            rg.add_pattern('.*(Hello).*')


if __name__ == '__main__':
    unittest.main()

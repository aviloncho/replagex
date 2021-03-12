import unittest
from pathlib import Path

from src.core import Replagex


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


if __name__ == '__main__':
    unittest.main()

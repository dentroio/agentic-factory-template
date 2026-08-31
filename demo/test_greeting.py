from pathlib import Path
import unittest

INDEX = Path(__file__).resolve().parent / "public" / "index.html"


class GreetingTest(unittest.TestCase):
    def test_greeting_present(self):
        text = INDEX.read_text(encoding="utf-8")
        self.assertIn("Hello, factory", text)


if __name__ == "__main__":
    unittest.main()

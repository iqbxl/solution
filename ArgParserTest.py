import unittest
import argparse

class TestArgParser(unittest.TestCase):
  # Test command-line argument parser
  def test_parser(self):
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args(["test.txt"])
    self.assertEqual(args.input, "test.txt")

if __name__ == "__main__":
  unittest.main()
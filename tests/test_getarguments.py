import unittest

from getarguments import get_arguments, validate_arguments


class TestGetArguments(unittest.TestCase):
    def testValidation(self):
        self.assertEqual(
            get_arguments(1, 1, 2, 5),
            "Arguments given: (1, 1, 2, 5), Validation passed",
        )
        self.assertEqual(
            get_arguments(1, 1, 13, 5),
            "Arguments given: (1, 1, 13, 5), Validation passed",
        )

    def test_assertion_raises(self):
        with self.assertRaises(ValueError) as context:
            validate_arguments(get_arguments(1, 1, -8, 5))
            self.assertTrue("Validation not passed!" in str(context.exception))
        with self.assertRaises(ValueError) as context:
            validate_arguments(get_arguments(0, 1, 0, 5))
            self.assertTrue("Validation not passed!" in str(context.exception))


if __name__ == "__main__":
    unittest.main()

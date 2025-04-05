import unittest
from library import Book, Reader


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("1984", "George Orwell", 328, "123-456-789")
        self.reader = Reader("Alice")

    def test_reserve_book(self):
        result = self.book.reserve(self.reader)
        self.assertTrue(result)
        self.assertEqual(self.book.reserved_by, self.reader)

    def test_reserve_book_already_reserved(self):
        self.book.reserve(self.reader)
        another_reader = Reader("Bob")
        result = self.book.reserve(another_reader)
        self.assertFalse(result)
        self.assertEqual(self.book.reserved_by, self.reader)

    def test_cancel_reserve(self):
        self.book.reserve(self.reader)
        result = self.book.cancel_reserve(self.reader)
        self.assertTrue(result)
        self.assertIsNone(self.book.reserved_by)

    def test_cancel_reserve_not_reserved(self):
        another_reader = Reader("Bob")
        result = self.book.cancel_reserve(another_reader)
        self.assertFalse(result)
        self.assertIsNone(self.book.reserved_by)

    def test_get_book(self):
        self.book.reserve(self.reader)
        result = self.book.get_book(self.reader)
        self.assertTrue(result)
        self.assertIsNone(self.book.reserved_by)
        self.assertEqual(self.book.checked_out_by, self.reader)

    def test_get_book_not_reserved_by_reader(self):
        another_reader = Reader("Bob")
        self.book.reserve(another_reader)
        result = self.book.get_book(self.reader)
        self.assertFalse(result)
        self.assertEqual(self.book.reserved_by, another_reader)
        self.assertIsNone(self.book.checked_out_by)

    def test_return_book(self):
        self.book.reserve(self.reader)
        self.book.get_book(self.reader)
        result = self.book.return_book(self.reader)
        self.assertTrue(result)
        self.assertIsNone(self.book.checked_out_by)

    def test_return_book_not_checked_out_by_reader(self):
        another_reader = Reader("Bob")
        self.book.reserve(self.reader)
        self.book.get_book(self.reader)
        result = self.book.return_book(another_reader)
        self.assertFalse(result)
        self.assertEqual(self.book.checked_out_by, self.reader)


class TestReader(unittest.TestCase):
    def setUp(self):
        self.book = Book("1984", "George Orwell", 328, "123-456-789")
        self.reader = Reader("Alice")

    def test_reserve_book(self):
        with self.assertLogs() as log:
            self.reader.reserve_book(self.book)
        self.assertIn("Alice reserved 1984.", log.output[0])

    def test_cancel_reserve(self):
        self.book.reserve(self.reader)
        with self.assertLogs(level="INFO") as log:
            self.reader.cancel_reserve(self.book)
        self.assertIn("Alice canceled reservation for 1984.", log.output[0])

    def test_get_book(self):
        self.book.reserve(self.reader)
        with self.assertLogs() as log:
            self.reader.get_book(self.book)
        self.assertIn("Alice checked out 1984.", log.output[0])

    def test_return_book(self):
        self.book.reserve(self.reader)
        self.book.get_book(self.reader)
        with self.assertLogs() as log:
            self.reader.return_book(self.book)
        self.assertIn("Alice returned 1984.", log.output[0])


if __name__ == "__main__":
    unittest.main()

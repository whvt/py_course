import pytest
import logging
from library import Book, Reader

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@pytest.fixture
def book():
    return Book("1984", "George Orwell", 328, "123-456-789")


@pytest.fixture
def reader():
    return Reader("Alice")


def test_reserve_book(book, reader):
    result = book.reserve(reader)
    logger.info(
        f"Attempted to reserve the book '1984' for reader {reader.name}. Result: {result}"
    )
    assert result is True
    assert book.reserved_by == reader


def test_reserve_book_already_reserved(book, reader):
    book.reserve(reader)
    another_reader = Reader("Bob")
    result = book.reserve(another_reader)
    logger.info(
        f"Attempted to reserve the book '1984' for reader"
        f" {another_reader.name}. Result: {result}"
    )
    assert result is False
    assert book.reserved_by == reader


def test_cancel_reserve(book, reader):
    book.reserve(reader)
    result = book.cancel_reserve(reader)
    logger.info(
        f"Attempted to cancel reservation of the book '1984' for reader"
        f" {reader.name}. Result: {result}"
    )
    assert result is True
    assert book.reserved_by is None


def test_cancel_reserve_not_reserved(book):
    another_reader = Reader("Bob")
    result = book.cancel_reserve(another_reader)
    logger.warning(
        f"Attempted to cancel reservation of the book '1984' by reader"
        f" {another_reader.name}, but the book was not reserved. Result: {result}"
    )
    assert result is False
    assert book.reserved_by is None


def test_get_book(book, reader):
    book.reserve(reader)
    result = book.get_book(reader)
    logger.info(f"Reader {reader.name} checked out the book '1984'. Result: {result}")
    assert result is True
    assert book.reserved_by is None
    assert book.checked_out_by == reader


def test_get_book_not_reserved_by_reader(book, reader):
    another_reader = Reader("Bob")
    book.reserve(another_reader)
    result = book.get_book(reader)
    logger.warning(
        f"Reader {reader.name} attempted to check out the book '1984', but it was reserved by"
        f" {another_reader.name}. Result: {result}"
    )
    assert result is False
    assert book.reserved_by == another_reader
    assert book.checked_out_by is None


def test_return_book(book, reader):
    book.reserve(reader)
    book.get_book(reader)
    result = book.return_book(reader)
    logger.info(f"Reader {reader.name} returned the book '1984'. Result: {result}")
    assert result is True
    assert book.checked_out_by is None


def test_return_book_not_checked_out_by_reader(book, reader):
    another_reader = Reader("Bob")
    book.reserve(reader)
    book.get_book(reader)
    result = book.return_book(another_reader)
    logger.warning(
        f"Reader {another_reader.name} attempted to return the book '1984', but it was"
        f" checked out by {reader.name}. Result: {result}"
    )
    assert result is False
    assert book.checked_out_by == reader


def test_reader_reserve_book(book, reader):
    reader.reserve_book(book)
    logger.info(f"Reader {reader.name} reserved the book '1984'.")
    assert book.reserved_by == reader


def test_reader_cancel_reserve(book, reader):
    book.reserve(reader)
    reader.cancel_reserve(book)
    logger.info(f"Reader {reader.name} canceled reservation for the book '1984'.")
    assert book.reserved_by is None


def test_reader_get_book(book, reader):
    book.reserve(reader)
    reader.get_book(book)
    logger.info(f"Reader {reader.name} checked out the book '1984'.")
    assert book.checked_out_by == reader


def test_reader_return_book(book, reader):
    book.reserve(reader)
    book.get_book(reader)
    reader.return_book(book)
    logger.info(f"Reader {reader.name} returned the book '1984'.")
    assert book.checked_out_by is None

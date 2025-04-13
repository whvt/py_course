import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()


class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved_by = None
        self.checked_out_by = None

    def reserve(self, reader):
        if self.reserved_by is None and self.checked_out_by is None:
            self.reserved_by = reader
            return True
        return False

    def cancel_reserve(self, reader):
        if self.reserved_by == reader:
            self.reserved_by = None
            return True
        return False

    def get_book(self, reader):
        if self.reserved_by == reader and self.checked_out_by is None:
            self.reserved_by = None
            self.checked_out_by = reader
            return True
        return False

    def return_book(self, reader):
        if self.checked_out_by == reader:
            self.checked_out_by = None
            return True
        return False


class Reader:
    def __init__(self, name):
        self.name = name

    def reserve_book(self, book):
        if book.reserve(self):
            logger.info("%s reserved %s.", self.name, book.book_name)
        else:
            logger.info("%s cannot reserve %s.", self.name, book.book_name)

    def cancel_reserve(self, book):
        if book.cancel_reserve(self):
            logger.info("%s canceled reservation for %s.", self.name, book.book_name)
        else:
            logger.info(
                "%s cannot cancel reservation for %s.", self.name, book.book_name
            )

    def get_book(self, book):
        if book.get_book(self):
            logger.info("%s checked out %s.", self.name, book.book_name)
        else:
            logger.info("%s cannot check out %s.", self.name, book.book_name)

    def return_book(self, book):
        if book.return_book(self):
            logger.info("%s returned %s.", self.name, book.book_name)
        else:
            logger.info("%s cannot return %s.", self.name, book.book_name)

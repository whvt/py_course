import yaml


def read_books(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
            if data is None:
                return {"books": []}
            return data
    except FileNotFoundError:
        return {"books": []}


def write_books(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        yaml.dump(data, file, allow_unicode=True, sort_keys=False)


def add_book(data, title, author, year):
    new_book = {"title": title, "author": author, "year": year}
    data["books"].append(new_book)


def main():
    filename = "books.yaml"

    books_data = read_books(filename)

    print("Current books:")
    for book in books_data["books"]:
        print(f"- {book['title']} by {book['author']} ({book['year']})")

    title = input("\nInput new title: ")
    author = input("Input new author: ")
    year = int(input("Input new year: "))

    add_book(books_data, title, author, year)

    write_books(filename, books_data)

    print("\nNew book addded")


if __name__ == "__main__":
    main()

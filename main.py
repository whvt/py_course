import os

os.system("clear")


# Напишите программу, которая добавляет ‘ing’ к словам
# вторая реализация будет ниже
def gerund(word):
    if word.endswith("ing"):
        return word
    else:
        return word + "ing"


words = ["sing", "clean", "concatinating", "jump"]
ing_words = [gerund(word) for word in words]

print(ing_words)


def hw():
    # Напишите программу, которая добавляет ‘ing’ к словам
    line1 = "jump"
    print(f"{line1} => {line1 + 'ing'}")

    # Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
    str_task1 = "www.my_site.com#about"
    print(str_task1.replace("#", "/"))

    # В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
    str_task3 = "Ivanou Ivan"
    print(" ".join(str_task3.split()[::-1]))

    # Напишите программу которая удаляет пробел в начале, в конце строки
    str_task3 = " Given text was with spaces on both ends "
    print("'", str_task3.strip(), "'", sep="")  # Чтобы было видно стрип в консоли

    # Имена собственные всегда начинаются с заглавной буквы,
    # за которой следуют строчные буквы. Исправьте данное имя собственное так,
    # чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris"

    str_task4 = "pARiS"
    print(str_task4.capitalize())

    # "I love arrays they are my favorite"  =>
    # => ["I", "love", "arrays", "they", "are", "my", "favorite"]
    str_task5 = "I love arrays they are my favorite"
    print(str_task5.split(" "))

    # Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus напечатайте текст:
    # “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
    namesurname = ["Ivan", "Ivanou"]
    city = "Minsk"
    country = "Belarus"

    print(
        "Привет, {} {}! Добро пожаловать в {}, {}".format(
            namesurname[0], namesurname[1], city, country
        )
    )

    # Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
    #  сделайте из него строку
    # => "I love arrays they are my favorite"

    task6 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
    print(" ".join(task6))

    # Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
    task6 = "Robin Singh"
    print(task6.split())

    # Создайте список из 10 элементов,
    # вставьте на 3-ю позицию новое значение,
    # удалите элемент из списка под индексом 6

    task7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    new_value = 100
    task7.insert(2, new_value)

    del task7[6]

    print(task7)


if __name__ == "__main__":
    hw()

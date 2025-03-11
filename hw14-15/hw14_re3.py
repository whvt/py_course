import re

text = """Довольно распространённая ошибка ошибка — это лишний повтор
повтор слова слова. Смешно, не не правда ли? Не нужно портить хор хоровод."""


pattern = r"\b(\w+)\b(?=\s+\b\1|\s+\b\w*\1\w*\b)"


corrected_text = re.sub(pattern, r"", text, flags=re.IGNORECASE).strip()

print("Changed to:")
print(corrected_text)

import re

passwords = ["Password123", "letmein!", "qwerty2025", "12345678", "Pa$$w0rd!"]

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{4,}$"

for password in passwords:
    if re.match(pattern, password):
        print(f"{password} - Valid password")
    else:
        print(f"{password} - Invalid password")

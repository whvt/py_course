import re


file_path = "date_samples.txt"
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()


date_pattern = r"\b\d{2}\.\d{2}\.\d{4}\b"


dates = []


for line in lines:
    found_dates = re.findall(date_pattern, line)
    dates.extend(found_dates)


print("Found dates:")
for date in dates:
    print(date)

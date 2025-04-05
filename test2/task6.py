def process_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        line_count = content.count("\n") + (1 if content else 0)
        word_count = len(content.split())
        char_count = len(content)

        stats = (
            f"\n\n--- STATS ---\n"
            f"Lines: {line_count}\n"
            f"Words: {word_count}\n"
            f"Chars: {char_count}\n"
        )

        print(stats)

        with open(file_path, "a", encoding="utf-8") as file:
            file.write(stats)
    except FileNotFoundError:
        print(f"Error: file '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")


file_name = "example.txt"
process_file(file_name)


# Write and append favorite quotes to a file

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
data_dir = BASE_DIR / "data"
data_dir.mkdir(parents=True, exist_ok=True)

file_path = data_dir / "quotes.txt"

print("Enter your three favorite quotes:")

quotes = []

for i in range(1, 4):
    quote = input(f"Quote {i}: ")
    quotes.append(quote)

try:
    with open(file_path, "a", encoding="utf-8") as file:
        for quote in quotes:
            file.write(quote + "\n")

    print("\nQuotes saved successfully!")
    print("File location:", file_path)

except OSError as error:
    print("Error while writing to the file:", error)

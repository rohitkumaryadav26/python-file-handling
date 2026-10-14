
# Read a text file and count its words

from pathlib import Path

# Locate input.txt relative to the project folder
BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "input.txt"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    words = content.split()
    print("File read successfully!")
    print("Total number of words:", len(words))

except FileNotFoundError:
    print("Error: input.txt was not found.")
    print("Please create the file inside the data folder.")

except OSError as error:
    print("Error while reading the file:", error)
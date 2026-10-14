# Python File Handling 

## Overview
This project demonstrates file handling in Python through reading text files, counting words, handling file errors, and writing and appending user data.

## Objectives
- Read text from external files.
- Count words using Python string methods.
- Handle missing files using `try-except`.
- Write and append user-provided quotes.
- Understand the `r`, `w`, and `a` file modes.

## Project Structure

```text
python-file-handling/
├── README.md
├── .gitignore
├── src/
│   ├── read_file.py
│   └── write_file.py
├── data/
│   ├── input.txt
│   └── quotes.txt
├── docs/
│   └── file_modes.md
└── assets/
    └── screenshots/
```

## Requirements
- Python 3
- VS Code or another Python editor

## How to Run

Run the following commands from the project root:

```bash
python src/read_file.py
python src/write_file.py
```

The first program reads `data/input.txt` and counts words. The second program asks for three quotes and appends them to `data/quotes.txt`.

## Concepts Learned
- File opening and closing
- Reading file contents
- Writing and appending text
- Word counting using `split()`
- Exception handling
- Persistent data storage

## Documentation
See `docs/file_modes.md` for an explanation of Python file modes.

## Execution Evidence
Screenshots of successful program execution and the generated files are stored in `assets/screenshots/`.

## Conclusion
This task provided practical experience in Python file handling, error management, and data persistence.

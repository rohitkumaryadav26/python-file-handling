# Python File Handling: File Modes

## 1. Introduction

File handling allows Python programs to read information from files and save information for future use. Unlike temporary variables, data saved in a file can remain available after a program ends.

Python uses the built-in `open()` function to access files.

## 2. File Modes

### Read Mode (`r`)

- Opens an existing file for reading.
- Raises `FileNotFoundError` if the file does not exist.
- Does not modify the existing content.

Example:

```python
with open("input.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

**Use it when:** You need to view, analyze, or process existing file data.

### Write Mode (`w`)

- Creates a file if it does not exist.
- Overwrites the contents if the file already exists.
- Removes the previous content when opening an existing file in this mode.

Example:

```python
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello, Python!")
```

**Use it when:** You want to create a new file or replace its existing content.

### Append Mode (`a`)

- Creates a file if it does not exist.
- Adds new content at the end of the file.
- Preserves the existing content.

Example:

```python
with open("output.txt", "a", encoding="utf-8") as file:
    file.write("New information\n")
```

**Use it when:** You want to add records, logs, or quotes without deleting previous data.

## 3. Comparison Table

| Feature                                             | `r` | `w` | `a` |

| Read data                                           | Yes | No | No |
| Write data                                          | No | Yes | Yes |
| Creates missing file                                | No | Yes | Yes |
| Preserves existing content                          | Yes | No | Yes |
| Main purpose                                       | Read | Replace | Add |

## 4. Why Use `with open()`?

The `with` statement automatically closes a file when the block finishes, including when an error occurs.

## 5. Error Handling

Use `try-except` to handle problems such as a missing file.

```python
try:
    with open("input.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
```

## 6. Conclusion

Python file handling makes it possible to store, retrieve, and process data. Understanding read, write, and append modes is important when developing applications that require persistent storage.

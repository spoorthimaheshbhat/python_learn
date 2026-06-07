# Lesson 10 - File Handling

## Overview

File handling allows programs to:

- Save data permanently
- Read previously stored data
- Update information
- Create logs
- Build real applications

Unlike variables, file data remains available after the program closes.

---

# Opening Files

## Write Mode

```python
with open("file.txt", "w") as file:
    file.write("Hello")
```

### Important

`"w"` creates the file if it doesn't exist.

If the file already exists:

```text
ALL previous content is erased.
```

---

## Read Mode

```python
with open("file.txt", "r") as file:
    content = file.read()
```

Used for reading existing files.

---

## Append Mode

```python
with open("file.txt", "a") as file:
    file.write("New line")
```

Appends content to the end of the file.

Does NOT erase existing content.

---

# The with Statement

Preferred way to work with files.

```python
with open("file.txt", "r") as file:
    data = file.read()
```

Benefits:

- Automatically closes file
- Cleaner code
- Safer resource handling

---

# Reading File Content

## Read Entire File

```python
content = file.read()
```

Returns a string.

---

## Read Lines

```python
lines = file.read().splitlines()
```

Returns:

```python
[
    "Line 1",
    "Line 2",
    "Line 3"
]
```

Useful for:

- Counting lines
- Processing records
- Reading usernames
- Reading expenses

---

# Writing Content

```python
file.write("Hello Python")
```

Writes text into file.

---

# Writing Multiple Lines

```python
file.write("\nPython")
```

`\n` creates a new line.

Example:

```text
Hello
Python
```

---

# Exception Handling with Files

## FileNotFoundError

Occurs when file does not exist.

```python
try:
    with open("missing.txt", "r") as file:
        data = file.read()

except FileNotFoundError:
    print("File not found")
```

Used extensively in Lesson 10.

---

# Counting Lines

```python
with open("languages.txt", "r") as file:
    lines = file.read().splitlines()

print(len(lines))
```

---

# Counting Words

```python
with open("passage.txt", "r") as file:
    words = file.read().split()

print(len(words))
```

### split()

Separates text by whitespace.

Example:

```python
"hello world".split()
```

Result:

```python
["hello", "world"]
```

---

# Real World Concepts Introduced

## Data Persistence

Data remains available after program closes.

Examples:

- Notes App
- Expense Tracker
- Login Audit Log

---

## Audit Logs

Record application activity.

Example:

```text
SUCCESS: admin
FAILED: test
FAILED: tester
```

Purpose:

- Security tracking
- Debugging
- History

---

## Configuration/Data Files

Credentials stored in:

```text
username,password
```

Example:

```text
admin,pwd@123
user1,password1
```

Converted into dictionary:

```python
{
    "admin": "pwd@123",
    "user1": "password1"
}
```

---

# String Processing While Reading Files

## Removing Whitespace

```python
line = line.strip()
```

Removes:

- Spaces
- Tabs
- Newlines

Example:

```python
" admin "
```

becomes

```python
"admin"
```

---

## Splitting Values

```python
username, password = line.split(",")
```

Example:

```text
admin,pwd123
```

becomes

```python
username = "admin"
password = "pwd123"
```

---

# Lesson 10 Real Projects

## Language Tracker

Features:

- Add languages
- Save to file
- Multiple entries
- Input validation

Concepts used:

- Append mode
- Loops
- Functions
- File handling

---

## Notes App

Features:

- Add notes
- View notes
- Clear notes
- Exit

Concepts used:

- Functions
- Menus
- File persistence
- Loops
- Validation

Operations supported:

| Operation | Status |
|------------|---------|
| Create | Yes |
| Read | Yes |
| Update | No |
| Delete | Yes |

---

## Expense Tracker

Features:

- Add expenses
- Validate input
- Store expenses
- Calculate total

Concepts used:

- File handling
- Lists
- Loops
- Integer conversion
- Accumulator pattern

Example:

```python
total += expense
```

---

## Login Audit System

Features:

- Username/password validation
- Credential storage
- Login attempts
- Audit logging
- Account lock after 3 failures

Concepts used:

- Dictionaries
- File parsing
- Functions
- Loops
- Logging

---

# Important Design Lessons

## Bad Design

Separate files:

```text
usernames.txt
passwords.txt
```

Problem:

Usernames and passwords are not linked.

---

## Better Design

```text
username,password
```

Example:

```text
admin,pwd123
john,test123
```

Converted into:

```python
{
    "admin": "pwd123",
    "john": "test123"
}
```

This is much safer.

---

# Common Mistakes Discovered

## Mistake 1

Using:

```python
with open("notes.txt", "w")
```

at program startup.

Effect:

Every run erases previous notes.

---

## Mistake 2

Using:

```python
with open("expenses.txt", "w")
```

at startup.

Effect:

All previous expenses disappear.

---

## Better Approach

Only create file when needed.

Avoid rewriting data unnecessarily.

---

# Key Takeaways

By Lesson 10 you have learned:

- Reading files
- Writing files
- Appending files
- Handling missing files
- Counting lines
- Counting words
- Logging actions
- Persisting application data
- Parsing structured file data
- Building small real-world applications

Lesson 10 marks the transition from learning syntax to building actual software.
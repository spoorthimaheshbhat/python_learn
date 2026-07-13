# Lesson 17 — JSON

---

# What is JSON?

JSON stands for **JavaScript Object Notation**.

It is a lightweight text format used to store and exchange structured data.

Although it originated from JavaScript, JSON is language-independent and is supported by Python and almost every modern programming language.

Example:

```json
{
    "name": "Alice",
    "age": 24,
    "department": "QA"
}
```

---

# Why JSON?

JSON is widely used because it is:

- Human readable
- Lightweight
- Easy for machines to parse
- Language independent

Almost every modern application uses JSON:

- REST APIs
- Mobile applications
- Configuration files
- Automation frameworks
- AI systems
- Cloud services

---

# Python Objects vs JSON

| Python | JSON |
|---------|------|
| dict | object |
| list | array |
| tuple | array |
| str | string |
| int | number |
| float | number |
| bool | true / false |
| None | null |

---

# json Module

Python provides the built-in module:

```python
import json
```

---

# json.dumps()

Converts a Python object into a JSON string.

Example:

```python
employee = {
    "name":"Alice",
    "age":24
}

text = json.dumps(employee)
```

Returns:

```text
{"name":"Alice","age":24}
```

Notice:

The return type is

```python
str
```

Memory Trick:

**dumpS → String**

---

# json.loads()

Converts a JSON string into a Python object.

Example:

```python
text = '{"name":"Alice"}'

employee = json.loads(text)
```

Returns

```python
dict
```

Memory Trick:

**loadS ← String**

---

# json.dump()

Writes a Python object directly into a file.

```python
with open("employee.json","w") as file:
    json.dump(employee,file,indent=4)
```

---

# json.load()

Reads JSON data from a file.

```python
with open("employee.json","r") as file:
    employee = json.load(file)
```

Returns

```python
dict
```

or

```python
list
```

depending on the JSON.

---

# dump vs dumps

dump()

- writes to file

dumps()

- returns JSON string

---

# load vs loads

load()

- reads from file

loads()

- reads from string

---

# JSON Files

Single object

```json
{
    "name":"Alice"
}
```

Multiple records

```json
[
    {
        "name":"Alice"
    },
    {
        "name":"Bob"
    }
]
```

Never store

```json
{}
{}
```

This causes

```
JSONDecodeError: Extra data
```

---

# Updating JSON

Correct workflow

```
Read

↓

Modify

↓

seek(0)

↓

dump()

↓

truncate()
```

Example

```python
with open("employee.json","r+") as file:

    employees = json.load(file)

    ...

    file.seek(0)

    json.dump(
        employees,
        file,
        indent=4
    )

    file.truncate()
```

---

# seek()

Moves the file pointer.

Example

```python
file.seek(0)
```

Moves cursor to beginning of file.

---

# truncate()

Removes everything after the current file pointer.

Why?

Suppose original file contains

```
Hello Josephine
```

You overwrite

```
Hello Joe
```

Without truncate()

```
Hello Joephine
```

With truncate()

```
Hello Joe
```

Always use

```python
seek()

↓

dump()

↓

truncate()
```

when updating JSON files.

---

# JSONDecodeError

Occurs when JSON is invalid.

Common reasons

- Empty file
- Malformed JSON
- Multiple JSON objects
- Reading from end of file

Handle using

```python
from json import JSONDecodeError
```

---

# CRUD with JSON

Typical workflow

Create

Read

Update

Delete

Example

Employee database

QA test reports

Attendance logs

Configuration files

---

# Real-world Applications

Employee database

Store employee records.

QA Automation

Store test execution reports.

API Testing

Validate JSON responses.

Configuration

Store application settings.

AI Systems

Exchange structured prompts and responses.

---

# Lesson Summary

You learned

- JSON fundamentals
- json module
- dumps()
- dump()
- loads()
- load()
- Reading JSON
- Writing JSON
- Updating JSON
- File pointers
- seek()
- truncate()
- JSONDecodeError
- CRUD operations
- JSON data modelling
- Real-world JSON applications
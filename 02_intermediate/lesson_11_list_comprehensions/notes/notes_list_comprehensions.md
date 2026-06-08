# Lesson 11 — List Comprehensions

## Overview

List comprehensions provide a concise way to create lists.

Instead of writing:

```python
numbers = []

for i in range(1, 6):
    numbers.append(i)
```

You can write:

```python
numbers = [i for i in range(1, 6)]
```

Result:

```python
[1, 2, 3, 4, 5]
```

---

# General Syntax

```python
new_list = [expression for item in iterable]
```

Example:

```python
squares = [x * x for x in range(1, 6)]
```

Output:

```python
[1, 4, 9, 16, 25]
```

---

# List Comprehension With Conditions

Syntax:

```python
new_list = [expression for item in iterable if condition]
```

Example:

```python
evens = [x for x in range(1, 11) if x % 2 == 0]
```

Output:

```python
[2, 4, 6, 8, 10]
```

---

# Converting Existing Lists

Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]
```

Output:

```python
[1, 4, 9, 16, 25]
```

---

# String Processing

Example:

```python
word = "python"

letters = [char.upper() for char in word]
```

Output:

```python
['P', 'Y', 'T', 'H', 'O', 'N']
```

---

# Filtering Data

Example:

```python
numbers = [10, 15, 20, 25, 30]

greater_than_20 = [num for num in numbers if num > 20]
```

Output:

```python
[25, 30]
```

---

# Conditional Expressions

Syntax:

```python
result = [
    value_if_true
    if condition
    else value_if_false
    for item in iterable
]
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

labels = [
    "Even" if num % 2 == 0 else "Odd"
    for num in numbers
]
```

Output:

```python
['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

---

# Nested Comprehensions

Example:

```python
matrix = [
    [1, 2],
    [3, 4]
]

flat = [item for row in matrix for item in row]
```

Output:

```python
[1, 2, 3, 4]
```

---

# Real-World Uses

## Cleaning User Input

```python
names = [" Alice ", " Bob ", " Charlie "]

cleaned = [name.strip() for name in names]
```

Output:

```python
['Alice', 'Bob', 'Charlie']
```

---

## Extracting Email Domains

```python
emails = [
    "john@gmail.com",
    "sam@yahoo.com",
    "alice@outlook.com"
]

domains = [
    email.split("@")[1]
    for email in emails
]
```

Output:

```python
['gmail.com', 'yahoo.com', 'outlook.com']
```

---

# Advantages

- Shorter code
- Easier list creation
- Often more readable
- Commonly used in professional Python code

---

# When Not To Use

Avoid list comprehensions when:

- Logic becomes difficult to read
- Multiple nested conditions are required
- The comprehension spans many lines

In those situations, a normal loop is usually better.

---

# Key Concepts Learned

- Basic list comprehensions
- Filtering with conditions
- Transforming values
- Working with strings
- Conditional expressions
- Nested comprehensions
- Real-world data cleaning

---

# Coach's Notes

List comprehensions are one of the most common Python features used in professional codebases.

The goal is not merely to shorten code.

The real benefit is expressing:

> "Create a new list from this existing data."

in a clear and Pythonic way.

As you progress into data processing, automation, APIs, testing, and backend development, list comprehensions will appear everywhere.
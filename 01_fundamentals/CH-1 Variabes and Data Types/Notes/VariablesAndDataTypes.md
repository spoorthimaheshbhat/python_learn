# Lesson 1 — Code Review Notes

## Exercise 1 Review

### Original Code

```python
name = "Sam"
age = 35
height = 181
learning_python = "Yes"

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Are you learning Python?", learning_python)
```

---

## Feedback

### 1. Use Boolean for True/False Values

Instead of:

```python
learning_python = "Yes"
```

Prefer:

```python
learning_python = True
```

Reason:

* Boolean values (`True`/`False`) are more appropriate for logical states.
* Useful later for conditions, APIs, databases, and validations.

---

### 2. Height Data Type

```python
height = 160
```

* Acceptable if height is in centimeters.
* Use float if height is represented in meters.

Example:

```python
height = 1.60
```

---

# Exercise 2 Review

## Strong Points

* Correctly created all major data types.
* Used meaningful variable names.
* Correct usage of `type()`.

### Example of Good Variable Naming

```python
difficulty_level
exercises_done
topics
```

---

## Important Observation About Sets

```python
status = {"Completed", "two", "exercises"}
```

This creates a **set**, not a dictionary.

### Difference

Dictionary:

```python
{"key": "value"}
```

Set:

```python
{"a", "b", "c"}
```

---

## Suggested Improvement

Instead of:

```python
print(type(greeting))
```

Prefer:

```python
print(f"greeting: {type(greeting)}")
```

Reason:

* Better readability
* Easier debugging in larger systems

---

# Exercise 3 Review

## Original Swapping Logic

```python
x = x + y
y = x - y
x = x - y
```

This is logically correct.

---

## Pythonic Way to Swap Variables

Preferred approach:

```python
x, y = y, x
```

Reason:

* Cleaner
* More readable
* Safer
* Preferred in professional Python code

---

## Why Arithmetic Swapping Is Less Preferred

Potential issues:

* Harder to read
* Harder to debug
* Overflow concerns in some programming languages

---

## Expert Insight

```python
x, y = y, x
```

Uses tuple unpacking internally.


---

# Exercise 4 Review

## Code

```python
x = 10
y = x
x = 20

print(y)
```

Output:

```python
10
```

---

## Explanation

Initially:

```python
x = 10
y = x
```

Both `x` and `y` reference the integer object `10`.

Then:

```python
x = 20
```

`x` now references a new integer object `20`.

`y` still references `10`.

Therefore:

```python
print(y)
```

Outputs:

```python
10
```

---

# Important Concept

Variables do NOT directly store values.

Variables reference objects in memory.

This becomes important later for:

* mutability
* copying
* lists
* dictionaries
* memory behavior
* debugging

---

# Additional Q&A Notes

## Single Quotes vs Double Quotes

Both are valid for strings:

```python
greeting = 'Hello'
message = "Hello"
```

---

## Escaping Quotes

Incorrect:

```python
text = 'It's good'
```

Correct:

```python
text = "It's good"
```

OR

```python
text = 'It\'s good'
```

`\` is called an escape character.

---

## Triple Quotes

Useful for multi-line strings:

```python
paragraph = """This is
a multi-line
string."""
```

---

# Important Notes to Remember

* Python is dynamically typed.
* Use meaningful variable names.
* Prefer booleans for logical states.
* Strings can use single or double quotes.
* Variables reference objects in memory.
* Pythonic code prioritizes readability.
* Prefer tuple unpacking for swapping.
* `type()` helps inspect object types.
* Sets and dictionaries use similar braces but different structures.

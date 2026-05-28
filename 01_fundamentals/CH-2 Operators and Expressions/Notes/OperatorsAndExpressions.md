# Lesson 2 — Operators and Expressions

# Concepts Covered

* Arithmetic Operators
* Comparison Operators
* Logical Operators
* Assignment Operators
* Membership Operators
* Identity Operators
* Operator Precedence
* Boolean Values
* Input Handling
* Type Conversion
* `is` vs `==`

---

# What Are Operators?

Operators perform operations on values.

Example:

```python
x = 10
y = 5

print(x + y)
```

Output:

```python
15
```

Here:

* `+` is the operator
* `x` and `y` are operands

---

# Types of Operators in Python

| Type       | Example           |
| ---------- | ----------------- |
| Arithmetic | `+ - * / % // **` |
| Comparison | `== != > < >= <=` |
| Logical    | `and or not`      |
| Assignment | `= += -= *=`      |
| Membership | `in`, `not in`    |
| Identity   | `is`, `is not`    |

---

# Arithmetic Operators

Used for mathematical operations.

| Operator | Meaning        |
| -------- | -------------- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |
| `//`     | Floor Division |
| `%`      | Modulus        |
| `**`     | Exponent       |

Example:

```python
a = 15
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

# Division vs Floor Division

## Normal Division

```python
10 / 3
```

Output:

```python
3.3333333333333335
```

---

## Floor Division

```python
10 // 3
```

Output:

```python
3
```

Removes decimal part.

---

# Modulus Operator

Returns remainder.

```python
10 % 3
```

Output:

```python
1
```

Used for:

* even/odd checks
* cyclic logic
* patterns
* indexing

---

# Exponent Operator

```python
15 ** 4
```

Means:

15^4=50625

---

# Comparison Operators

Comparison operators return boolean values.

Example:

```python
print(10 > 5)
```

Output:

```python
True
```

---

| Operator | Meaning               |
| -------- | --------------------- |
| `==`     | Equal                 |
| `!=`     | Not Equal             |
| `>`      | Greater Than          |
| `<`      | Less Than             |
| `>=`     | Greater Than or Equal |
| `<=`     | Less Than or Equal    |

---

# Important Difference — `=` vs `==`

## Assignment

```python
x = 10
```

Assigns value.

---

## Comparison

```python
x == 10
```

Checks equality.

---

# Logical Operators

Used to combine conditions.

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| `and`    | Both conditions must be true        |
| `or`     | At least one condition must be true |
| `not`    | Reverses boolean                    |

Example:

```python
age = 20

print(age > 18 and age < 30)
```

Output:

```python
True
```

---

# Assignment Operators

Shortcut assignment operations.

Example:

```python
x = 5
x += 2
```

Equivalent to:

```python
x = x + 2
```

---

# Membership Operators

Check whether a value exists inside another object.

Example:

```python
"th" in "python"
```

Output:

```python
True
```

Membership operators work with:

* strings
* lists
* tuples
* sets
* dictionaries

---

# Identity Operators

Identity operators check whether variables reference the same object in memory.

Example:

```python
a = [1, 2]
b = a

print(a is b)
```

Output:

```python
True
```

---

# Important Difference — `is` vs `==`

## `is`

Checks object identity.

Example:

```python
a is b
```

Checks:

* Are both variables referencing the same object?

---

## `==`

Checks value equality.

Example:

```python
a == c
```

Checks:

* Do both variables contain equal values?

---

# Example

```python
a = "Hello"
b = a
c = "Hello"

print(a is b)
print(a is c)
print(a == c)
```

Output:

```python
True
False
True
```

Explanation:

* `a` and `b` reference the same object in memory
* `b = a` does not create a new object; it points to the same object as `a`
* `c` creates a completely new object with the same value
* `a is b` returns `True` because both variables reference the same object
* `a is c` returns `False` because they are different objects in memory
* `a == c` returns `True` because the values inside both variables are equal

Visual representation:

```text
        Memory
a ---> |"Hello"| <--- b
       |       |
c ---> |"Hello"|
```

Even though the contents look identical, `c` is stored separately in memory.

---

# Important Best Practice

Avoid using `is` for normal value comparison.

Bad:

```python
x is 10
```

Good:

```python
x == 10
```

Use `is` mainly for:

* `None`
* identity checks

Example:

```python
if value is None:
```

---

# Operator Precedence

Python follows mathematical precedence rules.

Example:

```python
print(2 + 3 * 4)
```

Output:

```python
14
```

Equivalent to:

2+3\times4=14

Multiplication happens before addition.

---

# Exercise 1 — Arithmetic Practice

```python
a = 15
b = 4

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponent: {a ** b}")
```

---

# Exercise 2 — Even or Odd

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
```

---

# Important Concept — `input()`

`input()` always returns a string.

Example:

```python
type(input())
```

Output:

```python
<class 'str'>
```

Use type conversion when mathematical operations are needed.

Example:

```python
int(input())
```

---

# Exercise 3 — Comparison Operators

```python
x = 10
y = 20

print("Is x equal to y?", x == y)
print("Is x not equal to y?", x != y)
print("Is x greater than y?", x > y)
print("Is x less than y?", x < y)
print("Is x greater than or equal to y?", x >= y)
print("Is x less than or equal to y?", x <= y)
```

---

# Exercise 4 — Logical Operators

Original logic:

```python
if has_ticket == "y" and age >= 18:
    print("You are eligible to enter the theater")
elif has_ticket == "n":
    print("You are not eligible to enter the theater")
elif has_ticket == "y" and age < 18:
    print("You are not eligible to enter the theater")
else:
    print("Invalid Input")
```

---

# Cleaner Version

```python
if has_ticket == "y" and age >= 18:
    print("You are eligible to enter the theater")
else:
    print("You are not eligible to enter the theater")
```

---

# Better Boolean Approach

```python
has_ticket = input("Do you have the ticket? y/n: ").lower() == "y"
```

Now `has_ticket` becomes:

```python
True
False
```

instead of a string.

---

# Exercise 5 — Membership Operators

```python
print(f"Does 'python' contain 'th'? {'th' in 'python'}")
print(f"Does 'java' contain 'p'? {'p' in 'java'}")
```

---

# Exercise 6 — Identity Operators

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a == c)
```

Output:

```python
True
False
True
```

Explanation:

* `a` and `b` point to the same list object in memory
* assigning `b = a` does not copy the list
* `c` creates a new list object with identical values
* `is` checks whether two variables reference the exact same object
* `==` checks whether the values inside the objects are equal

Step-by-step:

```python
a = [1, 2, 3]
```

Creates a list object in memory.

```python
b = a
```

`b` now references the same object as `a`.

```python
c = [1, 2, 3]
```

Creates a new list object with the same values.

Therefore:

```python
a is b
```

returns `True` because both variables reference the same object.

```python
a is c
```

returns `False` because `c` is a different object in memory.

```python
a == c
```

returns `True` because both lists contain equal values.

---

# Important Learnings

* Arithmetic operators perform mathematical operations.
* `%` returns remainder.
* `//` performs floor division.
* `**` performs exponentiation.
* Comparison operators return booleans.
* `=` is assignment.
* `==` checks value equality.
* `is` checks object identity.
* Logical operators combine conditions.
* Membership operators check existence.
* Python follows operator precedence.
* `input()` always returns strings.
* Use type conversion for numerical operations.
* Pythonic code prioritizes readability and simplicity.
* Avoid unnecessary conditional branches.

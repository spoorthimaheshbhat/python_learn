# Lesson 6 — Conditional Statements

## Concepts Covered

* if
* elif
* else
* nested conditions
* logical operators
* truthy and falsy values
* condition evaluation order
* chained comparisons
* input validation
* decision making

---

# What Are Conditional Statements?

Conditional statements allow a program to make decisions.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

Output:

```text
Adult
```

A condition always evaluates to:

```python
True
```

or

```python
False
```

---

# if Statement

Syntax:

```python
if condition:
    statement
```

Example:

```python
temperature = 35

if temperature > 30:
    print("Hot day")
```

---

# if-else Statement

Choose between two possible paths.

Example:

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output:

```text
Minor
```

---

# if-elif-else Statement

Used when multiple outcomes are possible.

Example:

```python
score = 82

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

Output:

```text
B
```

---

# Important Rule: Evaluation Stops at First Match

Example:

```python
x = 15

if x > 10:
    print("A")

elif x > 12:
    print("B")

else:
    print("C")
```

Output:

```text
A
```

Reason:

* `x > 10` is True
* Python prints A
* Entire chain ends
* `elif` is never evaluated

---

# Difference Between if-if-if and if-elif-else

## Independent if Statements

```python
x = 15

if x > 10:
    print("A")

if x > 12:
    print("B")
```

Output:

```text
A
B
```

Both conditions are checked independently.

---

## if-elif-else Chain

```python
x = 15

if x > 10:
    print("A")

elif x > 12:
    print("B")
```

Output:

```text
A
```

Python stops after the first successful condition.

---

# Nested Conditions

Example:

```python
age = 25
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Allowed")
```

Output:

```text
Allowed
```

---

# Logical Operators

## AND

Both conditions must be True.

```python
age >= 18 and has_ticket
```

---

## OR

At least one condition must be True.

```python
is_student or is_employee
```

---

## NOT

Reverses a boolean value.

```python
not True
```

Output:

```python
False
```

---

# Truthy and Falsy Values

Python automatically treats some values as False.

Falsy values:

```python
False
0
0.0
""
[]
{}
set()
None
```

Everything else is generally Truthy.

Examples:

```python
x = ""
```

Evaluates as:

```python
False
```

---

```python
x = [1]
```

Evaluates as:

```python
True
```

because the list is not empty.

---

```python
x = 0
```

Evaluates as:

```python
False
```

---

# Chained Comparisons

Python supports:

```python
5 <= age <= 17
```

which means:

```python
age >= 5 and age <= 17
```

---

# Common Pitfall

Example:

```python
0 <= age > 110
```

This means:

```python
(age >= 0) and (age > 110)
```

It does NOT mean:

```python
0 <= age <= 110
```

For validation:

```python
if age < 0 or age > 110:
```

or

```python
if not (0 <= age <= 110):
```

are better approaches.

---

# Input Validation

Programs should validate input before processing.

Example:

```python
if marks < 0 or marks > 100:
    print("Invalid Marks")
```

---

# Triangle Validation

Triangle sides must satisfy:

```python
a + b > c
a + c > b
b + c > a
```

Additional validation:

```python
a > 0
b > 0
c > 0
```

to reject invalid side lengths.

Example:

```python
if a <= 0 or b <= 0 or c <= 0:
    print("Invalid input")
```

---

# Boundary Testing

Important edge cases tested during exercises:

## Grade Calculator

```text
-1
0
60
70
80
90
100
101
```

---

## ATM

```text
-1
0
1
800
10000
10001
```

---

## Ticket Pricing

```text
-2
0
4
5
17
18
59
60
110
```

Boundary testing helps uncover bugs and is a key QA mindset.

---

# Largest of Three Numbers — Hidden Bug

Original solution:

```python
if a > b and a > c:
```

fails when values are equal.

Example:

```text
5
5
4
```

Incorrect result:

```text
4
```

Better solution:

```python
if a >= b and a >= c:
```

Using `>=` correctly handles ties.

---

# Login System

Expected variables:

```python
correct_username = "admin"
correct_password = "python123"
```

Possible outcomes:

* Login successful
* Invalid username
* Invalid password
* Invalid username and password

---

# Key Learnings

* Conditions evaluate to True or False.
* `if` executes when a condition is True.
* `else` executes when all previous conditions fail.
* `elif` allows multiple decision paths.
* Python stops at the first matching `if/elif` condition.
* Multiple `if` statements are evaluated independently.
* Truthy and falsy values influence condition evaluation.
* Chained comparisons can simplify conditions.
* Input validation prevents invalid program states.
* Edge-case testing is essential for finding bugs.
* Real-world programming requires thinking about unusual inputs, not just ideal inputs.

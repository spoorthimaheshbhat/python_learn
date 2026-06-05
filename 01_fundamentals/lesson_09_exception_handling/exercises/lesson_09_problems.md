# Lesson 9 - Exception Handling - Problems

## Exercise 1 - Handle Invalid Integer Input

Write a program that:

1. Asks the user for an integer.
2. Prints the number.
3. Handles invalid input without crashing.

Example:

```text
abc
Invalid integer entered.
```

---

## Exercise 2 - Safe Division

Ask the user for:

- numerator
- denominator

Print the result.

Handle:

- ValueError
- ZeroDivisionError

Example:

```text
10
0
```

Output:

```text
Cannot divide by zero.
```

---

## Exercise 3 - Safe List Access

Given:

```python
numbers = [10, 20, 30, 40, 50]
```

Ask the user for an index.

Print the value.

Handle:

- IndexError
- ValueError

---

## Exercise 4 - Dictionary Lookup

Given:

```python
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}
```

Ask the user for a key.

Print the value.

Handle:

- KeyError

---

## Exercise 5 - Calculator With Exception Handling

Upgrade your calculator project.

Requirements:

- Use functions
- Handle invalid numbers
- Handle division by zero
- Handle invalid actions
- Program should not crash

---

## Exercise 6 - Predict Output

Predict before running:

```python
try:
    print(10 / 2)

except ZeroDivisionError:
    print("A")

else:
    print("B")

finally:
    print("C")
```

Explain carefully.

---

## Exercise 7 - Predict Output

Predict before running:

```python
try:
    print(int("abc"))

except ValueError:
    print("A")

finally:
    print("B")
```

Explain carefully.

---

## Exercise 8 - Repeated Input Until Valid

Keep asking:

```text
Enter an integer:
```

until a valid integer is entered.

Example:

```text
abc
Invalid input

xyz
Invalid input

10
Accepted
```

Use:

- while
- try
- except

---

## Exercise 9 - Sum of Two Integers

Create:

```python
def safe_add():
```

Requirements:

- Ask for two integers
- Return their sum
- Handle invalid input
- Return None if input is invalid

---

## Exercise 10 - Positive Integer Validator

Create:

```python
def get_positive_integer():
```

Requirements:

- Keep asking until user enters:
  - valid integer
  - greater than zero

Example:

```text
abc
Invalid input

0
Must be positive

-5
Must be positive

10
Accepted
```

Return the valid integer.
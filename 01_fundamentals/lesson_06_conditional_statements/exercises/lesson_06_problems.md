# Lesson 6 — Conditional Statements — Exercise Problems

## Exercise 1 — Positive, Negative, or Zero

Take a number from the user.

Print:

* Positive
* Negative
* Zero

depending on the value entered.

---

## Exercise 2 — Leap Year Checker

Take a year from the user.

A leap year is:

* divisible by 400, OR
* divisible by 4 but not by 100

Examples:

* 2000 → Leap Year
* 1900 → Not Leap Year
* 2024 → Leap Year
* 2023 → Not Leap Year

---

## Exercise 3 — Grade Calculator

Take marks as input.

Assign grades:

| Marks    | Grade |
| -------- | ----- |
| 90+      | A     |
| 80-89    | B     |
| 70-79    | C     |
| 60-69    | D     |
| Below 60 | F     |

Also handle invalid marks:

* Marks < 0
* Marks > 100

---

## Exercise 4 — Largest of Three Numbers

Take three numbers from the user.

Print the largest number.

Constraint:

* Do NOT use `max()`

---

## Exercise 5 — Login System

Create:

```python
correct_username = "admin"
correct_password = "python123"
```

Ask the user for:

* username
* password

Print:

* Invalid username
* Invalid password
* Login successful

based on the input.

---

## Exercise 6 — Truthy/Falsy Investigation

Predict output BEFORE running.

### A

```python
x = ""

if x:
    print("A")
else:
    print("B")
```

---

### B

```python
x = [1]

if x:
    print("A")
else:
    print("B")
```

---

### C

```python
x = 0

if x:
    print("A")
else:
    print("B")
```

Explain each output.

---

## Exercise 7 — Movie Ticket Pricing

Take age as input.

Pricing Rules:

| Age         | Ticket Price |
| ----------- | ------------ |
| Less than 5 | Free         |
| 5 - 17      | ₹100         |
| 18 - 59     | ₹200         |
| 60+         | ₹150         |

Handle invalid ages.

---

## Exercise 8 — Triangle Validator

Take three side lengths as input.

A valid triangle must satisfy:

```text
a + b > c
a + c > b
b + c > a
```

Print:

* Valid Triangle
* Invalid Triangle

Bonus:

Reject side lengths less than or equal to zero.

---

## Exercise 9 — Mini ATM Challenge

Given:

```python
balance = 10000
```

Ask the user for a withdrawal amount.

Cases:

* Amount <= 0 → Invalid amount
* Amount > balance → Insufficient funds
* Otherwise deduct and display remaining balance

Example:

```text
Withdraw: 2500
Remaining balance: 7500
```

---

## Exercise 10 — Prediction Challenge

Predict output BEFORE running:

```python
x = 10

if x > 5:
    print("A")

if x > 8:
    print("B")

if x > 12:
    print("C")
else:
    print("D")
```

Explain carefully why the output occurs.

---

## Extra Challenge

Predict output BEFORE running:

```python
x = 15

if x > 10:
    print("A")

elif x > 12:
    print("B")

else:
    print("C")
```

Explain why the output differs from using multiple independent `if` statements.

# Lesson 12 - Lambda Functions
# Exercises

---

## Exercise 1

Given:

```python
numbers = [1,2,3,4,5]
```

Use map() and a lambda function to create a list of squares.

Expected:

```text
[1, 4, 9, 16, 25]
```

---

## Exercise 2

Create a lambda function that adds two numbers.

Example:

```python
add = lambda a, b: a + b
```

Test with multiple inputs.

---

## Exercise 3

Create a lambda function that checks whether a number is even.

Examples:

```text
8 → True
7 → False
0 → True
```

---

## Exercise 4

Use a lambda function to return the length of a string.

Example:

```python
"Python"
```

Output:

```text
6
```

Bonus:

Ignore spaces before counting.

---

## Exercise 5

Given:

```python
names = [
    "alice",
    "bob",
    "charlie"
]
```

Convert all names to uppercase using map().

Then sort them in reverse alphabetical order.

Expected:

```text
['CHARLIE', 'BOB', 'ALICE']
```

---

## Exercise 6

Given:

```python
numbers = [1,2,3,4,5,6,7,8,9,10]
```

Use filter() to create:

### Part A

Even numbers list.

Expected:

```text
[2,4,6,8,10]
```

### Part B

Odd numbers list.

Expected:

```text
[1,3,5,7,9]
```

---

## Exercise 7

Given:

```python
numbers = [5,10,15,20,25,30]
```

Use filter() to return only numbers greater than 15.

Expected:

```text
[20,25,30]
```

Bonus:

Given:

```python
negative_numbers = [
    -8,-4,-9,-10,-23
]
```

Use map() to convert them to positive values.

Expected:

```text
[8,4,9,10,23]
```

---

## Exercise 8

Given:

```python
products = [
    ("Laptop", 50000),
    ("Mouse", 500),
    ("Keyboard", 1500),
    ("Monitor", 12000)
]
```

Sort products by price using a lambda function.

---

## Exercise 9

Given:

```python
students = [
    ("Alice", 90),
    ("Bob", 75),
    ("Charlie", 85),
    ("David", 95)
]
```

Sort students by marks:

### Part A

Ascending

### Part B

Descending

---

## Exercise 10

Predict output before running:

```python
add = lambda a, b: a + b

print(add(10, 5))
```

Explain carefully.

---

## Exercise 11

Given:

```python
employees = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 75000},
    {"name": "Charlie", "salary": 45000}
]
```

Sort employees by salary using a lambda function.

---

## Exercise 12

Given:

```python
logins = [
    ("alice", 5),
    ("bob", 15),
    ("charlie", 2),
    ("admin", 25)
]
```

Use filter() to find users with more than 10 logins.

Expected:

```text
[
 ('bob', 15),
 ('admin', 25)
]
```

---

## Exercise 13 (Use Case)

Transaction Analysis

Given:

```python
transactions = [
    ("TXN001", 500),
    ("TXN002", 2500),
    ("TXN003", 150),
    ("TXN004", 4000),
    ("TXN005", 750)
]
```

Tasks:

1. Use filter() to find transactions above 1000.
2. Sort the filtered transactions by amount descending.
3. Print the final result.

Expected:

```text
Transactions above 1000:
[
 ('TXN002', 2500),
 ('TXN004', 4000)
]

Transactions high-to-low:
[
 ('TXN004', 4000),
 ('TXN002', 2500)
]
```

---

# Lesson 12 Summary

Concepts practiced:

- Lambda functions
- Anonymous functions
- map()
- filter()
- sorted()
- key=
- reverse=
- String processing
- Tuple sorting
- Dictionary sorting
- Functional programming
- Data processing pipelines
- Real-world transaction analysis
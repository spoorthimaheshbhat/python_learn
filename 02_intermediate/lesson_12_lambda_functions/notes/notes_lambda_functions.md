# Lesson 12 - Lambda Functions

## What is a Lambda Function?

A lambda function is a small anonymous function that can have any number of arguments but only one expression.

Syntax:

```python
lambda arguments: expression
```

Example:

```python
square = lambda x: x ** 2

print(square(5))
```

Output:

```text
25
```

---

# Why Use Lambda Functions?

Useful when:

- A function is needed only once
- Passing a function into map()
- Passing a function into filter()
- Using custom sorting with sorted()

Example:

```python
add = lambda a, b: a + b

print(add(10, 5))
```

Output:

```text
15
```

---

# map()

map() applies a function to every item in an iterable.

Syntax:

```python
map(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4]

squares = list(
    map(lambda x: x ** 2, numbers)
)

print(squares)
```

Output:

```text
[1, 4, 9, 16]
```

---

# filter()

filter() keeps only elements where the condition returns True.

Syntax:

```python
filter(function, iterable)
```

Example:

```python
numbers = [1,2,3,4,5,6]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(even_numbers)
```

Output:

```text
[2, 4, 6]
```

---

# map() vs filter()

map()

- Transforms every item
- Output length remains the same

Example:

```python
numbers = [1,2,3]

result = list(
    map(lambda x: x * 10, numbers)
)
```

Output:

```text
[10, 20, 30]
```

filter()

- Removes items that don't match a condition
- Output length may change

Example:

```python
numbers = [1,2,3,4]

result = list(
    filter(lambda x: x % 2 == 0, numbers)
)
```

Output:

```text
[2, 4]
```

---

# Using Lambda with Strings

Example:

```python
text = "Python"

length = lambda x: len(x)

print(length(text))
```

Output:

```text
6
```

---

# Cleaning Strings Before Counting Characters

Example:

```python
text = " the wheels on the bus "

count = lambda x: len(
    x.strip().replace(" ", "")
)

print(count(text))
```

Output:

```text
19
```

Methods used:

- strip() removes leading/trailing spaces
- replace() removes internal spaces

---

# Using Lambda with sorted()

sorted() can sort using a custom key.

Example:

```python
students = [
    ("Alice", 90),
    ("Bob", 75),
    ("Charlie", 85)
]

sorted_students = sorted(
    students,
    key=lambda x: x[1]
)

print(sorted_students)
```

Output:

```text
[('Bob', 75), ('Charlie', 85), ('Alice', 90)]
```

---

# Sorting Descending

```python
sorted_students = sorted(
    students,
    key=lambda x: x[1],
    reverse=True
)
```

Output:

```text
[('Alice', 90), ('Charlie', 85), ('Bob', 75)]
```

---

# Sorting Tuples

Example:

```python
products = [
    ("Laptop", 50000),
    ("Mouse", 500),
    ("Keyboard", 1500)
]

sorted_products = sorted(
    products,
    key=lambda x: x[1]
)
```

Lambda accesses tuple indexes:

```python
x[0] -> name
x[1] -> price
```

---

# Sorting Dictionaries

Example:

```python
employees = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 75000}
]

sorted_employees = sorted(
    employees,
    key=lambda emp: emp["salary"]
)
```

Output:

```text
[
 {'name': 'Alice', 'salary': 50000},
 {'name': 'Bob', 'salary': 75000}
]
```

---

# Functional Data Processing Pipeline

Real-world pattern:

```text
Raw Data
    ↓
Filter
    ↓
Sort
    ↓
Output
```

Example:

```python
transactions
    ↓
filter(amount > 1000)
    ↓
sort(high to low)
    ↓
report
```

---

# Transaction Example

Filter high-value transactions:

```python
high_transactions = list(
    filter(
        lambda x: x[1] > 1000,
        transactions
    )
)
```

Sort descending:

```python
sorted_transactions = sorted(
    high_transactions,
    key=lambda x: x[1],
    reverse=True
)
```

Output:

```text
[
 ('TXN004', 4000),
 ('TXN002', 2500)
]
```

---

# Key Takeaways

## Lambda

```python
lambda x: expression
```

Creates small anonymous functions.

## map()

```python
map(lambda x: ..., iterable)
```

Transforms every element.

## filter()

```python
filter(lambda x: condition, iterable)
```

Keeps matching elements.

## sorted()

```python
sorted(
    iterable,
    key=lambda x: ...,
    reverse=True
)
```

Provides custom sorting logic.

## Professional Skill Developed

You practiced:

- Functional programming basics
- Data transformation
- Data filtering
- Custom sorting
- Processing collections in stages
- Real-world reporting workflows
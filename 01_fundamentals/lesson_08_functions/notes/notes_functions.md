# Lesson 8 - Functions

## What is a Function?

A function is a reusable block of code that performs a specific task.

Example:

```python
def say_hello():
    print("Hello Python")

say_hello()
```

Benefits:
- Reusability
- Cleaner code
- Better organization
- Easier testing and maintenance

---

## Defining and Calling Functions

Function definition:

```python
def greet():
    print("Hello")
```

Function call:

```python
greet()
```

---

## Parameters and Arguments

Parameters are variables defined in the function.

```python
def greet(name):
    print(f"Hello {name}")
```

Arguments are values passed when calling the function.

```python
greet("Sam")
```

---

## Return Values

Functions can return data using `return`.

```python
def add(a, b):
    return a + b

result = add(10, 20)
```

### Why Return Instead of Print?

Prefer:

```python
def add(a, b):
    return a + b
```

over:

```python
def add(a, b):
    print(a + b)
```

Because returned values can be:
- Stored
- Reused
- Compared
- Passed to other functions

---

## Multiple Return Values

Python can return multiple values.

```python
def calculate(a, b):
    return a + b, a - b, a * b
```

Receiving values:

```python
sum_val, diff_val, product_val = calculate(10, 5)
```

---

## Boolean Functions

Functions often return `True` or `False`.

Example:

```python
def validate_login(username, password):
    return username == "admin" and password == "python123"
```

---

## Returning Conditions Directly

Instead of:

```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
```

Prefer:

```python
def is_even(number):
    return number % 2 == 0
```

The condition itself already evaluates to `True` or `False`.

---

## Local and Global Variables

Global variable:

```python
x = 100
```

Local variable:

```python
def test():
    x = 50
```

Example:

```python
x = 100

def test():
    x = 50
    print(x)

test()
print(x)
```

Output:

```text
50
100
```

Local variables exist only inside the function.

---

## Default Parameters

Functions can define default values.

```python
def greet(name="Guest"):
    print(f"Hello {name}")
```

Usage:

```python
greet("Sam")
greet()
```

Output:

```text
Hello Sam
Hello Guest
```

---

## Keyword Arguments

Arguments can be passed by name.

```python
def introduce(name, age, city):
    print(name, age, city)

introduce(
    city="London",
    age=12,
    name="Harry"
)
```

Order no longer matters.

---

## Function Design Principles

### Separation of Concerns

Good:

```python
def input_nums():
    ...

def calculator():
    ...
```

Each function has one responsibility.

---

### Avoid Duplicate Logic

Bad:

```python
if action == "add":
    ...
```

inside both the function and caller.

Prefer handling the decision in one place.

---

### Compute and Return

Utility functions should generally:

```text
Receive data
↓
Process data
↓
Return data
```

instead of printing directly.

---

## Calculator Project Learnings

### Initial Design

Calculated all operations at once:

```python
return a+b, a-b, a*b, a/b
```

Worked but was inefficient.

---

### Improved Design

Calculate only requested operation:

```python
def calculator(a, b, action):
```

More scalable.

---

### Division by Zero

Handled using:

```python
if b == 0:
    print("Cannot perform division.")
    exit()
```

Current solution is acceptable.

Future lessons will introduce:

```python
try:
    ...
except ZeroDivisionError:
    ...
```

---

### Returning Results

Final version:

```python
result = calculator(x, y, action)
print(result)
```

This is preferred over printing directly inside the function.

---

## Useful Python Conventions

### Check for None

Prefer:

```python
if result is None:
```

instead of:

```python
if result == None:
```

---

### Store Function Results

Avoid:

```python
if is_prime(num) is None:
```

followed by another:

```python
elif is_prime(num):
```

This recalculates the result.

Prefer:

```python
result = is_prime(num)

if result is None:
    ...
elif result:
    ...
```

---

## Strengths Demonstrated in Lesson 8

- Good function design
- Proper use of return values
- Multiple return values
- Strong handling of edge cases
- Input validation
- Reusable code
- Separation of responsibilities
- Understanding of local vs global scope
- Comfortable with parameters and arguments

---

## Key Takeaway

A good function should:

1. Have a single responsibility.
2. Accept required inputs.
3. Perform a task.
4. Return useful results.
5. Be reusable in multiple places.

Think:

```text
Input
↓
Function
↓
Return Value
↓
Caller decides what to do
```
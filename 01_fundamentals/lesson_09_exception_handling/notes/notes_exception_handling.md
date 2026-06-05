# Lesson 9 - Exception Handling

## What is an Exception?

An exception is a runtime error that occurs while a program is running.

Examples:

### ValueError

```python
int("abc")
```

### ZeroDivisionError

```python
10 / 0
```

### IndexError

```python
numbers = [1, 2, 3]
print(numbers[10])
```

### KeyError

```python
student = {"name": "John"}
print(student["age"])
```

---

## Why Exception Handling?

Without exception handling:

```python
number = int(input("Enter number: "))
```

Input:

```text
abc
```

Program crashes with:

```text
ValueError
```

With exception handling:

```python
try:
    number = int(input("Enter number: "))
except ValueError:
    print("Please enter a valid integer.")
```

Program continues safely.

---

## try / except Syntax

```python
try:
    risky_code
except ErrorType:
    handling_code
```

Example:

```python
try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
```

---

## Handling Multiple Exceptions

```python
try:
    num1 = int(input())
    num2 = int(input())

    print(num1 / num2)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## Handling Multiple Exceptions Together

```python
except (ValueError, ZeroDivisionError):
    print("Invalid input")
```

---

## else Block

Runs only when no exception occurs.

```python
try:
    number = int(input())

except ValueError:
    print("Invalid input")

else:
    print("Success")
```

Execution order:

```text
try
↓
else
```

---

## finally Block

Runs whether an exception occurs or not.

```python
try:
    number = int(input())

except ValueError:
    print("Invalid input")

finally:
    print("Program finished")
```

Execution order:

```text
try/except
↓
finally
```

---

## Negative Indexing

Lists support negative indexes.

```python
numbers = [10, 20, 30, 40, 50]
```

Examples:

```python
numbers[-1]
```

Output:

```text
50
```

```python
numbers[-2]
```

Output:

```text
40
```

Negative indexes do not raise IndexError if they refer to a valid position.

---

## Case-Insensitive Dictionary Lookup

Example:

```python
student = {
    "name": "Alice",
    "age": 20
}

key = input("Enter key: ")
print(student[key.lower()])
```

Input:

```text
NAME
```

Output:

```text
Alice
```

---

## Unreachable Code After return

Example:

```python
return value
break
```

The `break` is never executed.

Reason:

```python
return
```

immediately exits the function.

---

## Exception Handling vs Manual Validation

Using exceptions:

```python
try:
    return numerator / denominator
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Using validation:

```python
if denominator == 0:
    return None

return numerator / denominator
```

Both approaches are valid.

---

## Loop + Exception Pattern

Common pattern:

```python
while True:
    try:
        value = int(input("Enter value: "))
        return value

    except ValueError:
        print("Invalid input")
```

Used frequently in real applications.

---

## Reusable Input Functions

Instead of repeating code:

```python
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                print("Must be positive.")
            else:
                return value

        except ValueError:
            print("Invalid input.")
```

Usage:

```python
age = get_positive_integer("Enter age: ")
quantity = get_positive_integer("Enter quantity: ")
```

Benefits:

- Reusable
- Cleaner code
- Easier maintenance

---

## Professional Programming Habit

Beginner mindset:

```python
number = int(input())
```

Assumes perfect input.

Better mindset:

```python
try:
    number = int(input())
except ValueError:
    ...
```

Always consider:

- Invalid input
- Division by zero
- Missing keys
- Invalid indexes

Robust programs handle errors gracefully instead of crashing.
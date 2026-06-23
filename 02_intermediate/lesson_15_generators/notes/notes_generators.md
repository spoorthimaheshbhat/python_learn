# Lesson 15 — Generators

## What Problem Do Generators Solve?

Normally, Python stores all values in memory at once.

Example:

```python
numbers = [1, 2, 3, 4, 5]
```

This is fine for small datasets.

However, for very large datasets (millions of records), loading everything into memory can be inefficient.

Generators solve this problem by producing values one at a time only when needed.

---

## Generator Mental Model

### return

```python
def test():
    return 10
```

Behavior:

1. Function executes.
2. Value is returned.
3. Function ends permanently.

---

### yield

```python
def test():
    yield 10
```

Behavior:

1. Function execution pauses.
2. Value is returned temporarily.
3. Function remembers its position.
4. Execution resumes later.

---

## Generator Functions

A function becomes a generator when it contains the keyword:

```python
yield
```

Example:

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

Calling:

```python
numbers()
```

does NOT execute the function.

Instead it returns:

```text
<generator object numbers at ...>
```

---

## Consuming Generators

### Using next()

```python
g = numbers()

print(next(g))
print(next(g))
print(next(g))
```

Output:

```text
1
2
3
```

---

### Using a for loop

```python
for num in numbers():
    print(num)
```

Output:

```text
1
2
3
```

---

## Common Beginner Mistake

```python
print(next(numbers()))
print(next(numbers()))
print(next(numbers()))
```

Output:

```text
1
1
1
```

Why?

Each call to:

```python
numbers()
```

creates a brand-new generator.

Correct:

```python
g = numbers()

print(next(g))
print(next(g))
print(next(g))
```

Output:

```text
1
2
3
```

---

## StopIteration

When a generator has no more values:

```python
next(generator)
```

raises:

```python
StopIteration
```

Example:

```python
try:
    print(next(g))
except StopIteration:
    print("End Reached")
```

---

## Generator Expressions

List Comprehension:

```python
squares = [x * x for x in range(5)]
```

Output:

```python
[0, 1, 4, 9, 16]
```

Type:

```python
<class 'list'>
```

---

Generator Expression:

```python
squares = (x * x for x in range(5))
```

Type:

```python
<class 'generator'>
```

Output:

```python
<generator object ...>
```

Values are produced only when consumed.

---

## Iterators vs Generators

Iterator:

```python
iterator = iter([1, 2, 3])
```

Generator:

```python
def numbers():
    yield 1
    yield 2
```

Both support:

```python
next()
```

Difference:

Generators create iterators automatically.

---

## Real-World Use Cases

### Attendance Stream Reader

Instead of loading all attendance records:

```python
yield name, status
```

one record is produced at a time.

Benefits:

* Lower memory usage
* Continuous processing
* Suitable for large files

---

### Transaction Processor

Generator streams transactions:

```python
yield "Processed Transaction"
yield "Failed Transaction"
yield "Invalid Transaction"
```

Benefits:

* Handles large transaction logs
* Supports user-controlled viewing
* Processes records incrementally

---

## Key Takeaways

### return

```text
Return value
Function ends
```

### yield

```text
Return value
Pause function
Resume later
```

### Generator

```text
Produces data on demand
Remembers position
Consumes less memory
```

### Common Consumption Methods

```python
next(generator)
```

```python
for item in generator:
```

```python
list(generator)
```

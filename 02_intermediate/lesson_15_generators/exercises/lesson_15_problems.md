# Lesson 15 — Generators — Problems

## Exercise 1 — Simple Generator

Create a generator function:

```python
def fruits():
```

Yield:

```text
apple
banana
mango
```

Print all values using:

```python
next()
```

---

## Exercise 2 — Generator in a For Loop

Create:

```python
def numbers():
```

Yield:

```text
10
20
30
```

Print values using a:

```python
for
```

loop.

---

## Exercise 3 — Countdown Generator

Create:

```python
def countdown(n):
```

Input:

```python
countdown(5)
```

Output:

```text
5
4
3
2
1
```

Add appropriate input validation.

---

## Exercise 4 — Even Number Generator

Create:

```python
def get_evens(top):
```

Generate:

```text
2
4
6
8
10
```

Add user input validation.

---

## Exercise 5 — Manual Generator Consumption

Create:

```python
def letters():
```

Yield:

```text
A
B
C
```

Consume manually using:

```python
next()
```

Handle:

```python
StopIteration
```

properly.

---

## Exercise 6 — Generator Expressions

Given:

```python
[x*x for x in range(5)]
```

and:

```python
(x*x for x in range(5))
```

Tasks:

1. Print their types.
2. Observe outputs.
3. Consume generator values.
4. Explain differences.

---

## Exercise 7 — Prediction Exercise

Predict output before running:

```python
def test():
    yield 1
    yield 2

g = test()

print(next(g))
print(next(g))
```

Explain carefully.

---

# Use Case 1 — Attendance Stream Reader

Requirements:

* Read attendance records from file.
* Produce records one at a time using:

```python
yield
```

* Display records only when requested by user.
* Handle invalid inputs.
* Handle end of records using:

```python
StopIteration
```

### Enhancement Completed

Added:

```python
except StopIteration:
    print("End of Records! Thank you.")
```

---

# Use Case 2 — Transaction Stream Processor

Requirements:

* Read transaction file.
* Stream one transaction at a time.
* Classify:

```text
Processed Transaction
Failed Transaction
```

* Handle:

```python
ValueError
FileNotFoundError
```

* Allow user-controlled viewing of records.

### Enhancement Completed

Added handling for:

```python
Invalid Transaction Encountered
```

while continuing stream processing.

---

# Challenge — Employee ID Generator

Create an Employee ID generation system.

Requirements:

Generate:

```text
EMP001
EMP002
EMP003
...
```

Store generated IDs for employees.

Handle:

* User input
* Multiple employees
* Invalid requests

### Exploration Outcome

Used generators to create employee IDs dynamically and observed where generators are useful versus where a simple return statement may be more appropriate.

---

# Additional Concepts Explored During Lesson

## Generator vs Return

Observed that:

```python
yield
```

and

```python
return
```

can sometimes produce the same final output when converted into lists.

Example:

```python
list(generator)
```

versus

```python
list(tuple_return)
```

Important realization:

The output may look identical, but the underlying execution model is completely different.

---

## Generator State

Observed:

```python
next(numbers())
```

creates a fresh generator every time.

Output:

```text
1
1
1
```

while:

```python
g = numbers()
```

followed by:

```python
next(g)
```

advances generator state:

```text
1
2
3
```

---

## Lesson Summary

This lesson introduced:

* Generator Functions
* yield
* Generator Objects
* next()
* StopIteration
* Generator Expressions
* Lazy Evaluation
* Streaming Data Processing
* Real-world File Streaming Use Cases

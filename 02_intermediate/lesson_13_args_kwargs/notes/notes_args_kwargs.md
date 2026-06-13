# Lesson 13 — *args and **kwargs

## Goal

Learn how Python accepts variable numbers of arguments.

---

# 1. Variable Length Arguments

Sometimes we do not know beforehand how many inputs a function should receive.

Example:

* add numbers
* checkout items
* register users
* generate reports

Python provides:

```python
*args
**kwargs
```

---

# 2. *args — Variable Positional Arguments

Collects multiple positional arguments.

```python
def show(*args):
    print(args)

show(1,2,3)
```

Output:

```text
(1, 2, 3)
```

Why tuple?

Python packs positional arguments into tuples.

---

Example:

```python
def add_all(*args):
    return sum(args)

print(add_all(10,20,30))
```

Output:

```text
60
```

---

# 3. Unpacking Lists with *

Example:

```python
numbers=[10,20,30]

add_all(*numbers)
```

Process:

```text
[10,20,30]
↓

10,20,30
↓

args=(10,20,30)
```

---

# 4. **kwargs — Variable Keyword Arguments

Collects named arguments.

Example:

```python
def profile(**kwargs):
    print(kwargs)

profile(
    name="Alice",
    age=20
)
```

Output:

```text
{
 "name":"Alice",
 "age":20
}
```

kwargs becomes a dictionary.

---

# 5. Access kwargs

```python
for key,value in kwargs.items():
    print(key,value)
```

---

# 6. Mixing Parameters

Order:

```python
def example(
    required,
    *args,
    **kwargs
):
```

Order matters.

---

# 7. Packing vs Unpacking

Packing:

```python
def f(*args):
```

Unpacking:

```python
f(*numbers)
```

---

Dictionary unpack:

```python
print_summary(**summary)
```

Equivalent:

```python
print_summary(
 Alice={...},
 Bob={...}
)
```

---

# 8. Your Attendance Summary Exploration

Pipeline:

```text
File
↓

Tuple List

↓

Unique Employees

↓

Summary Dictionary

↓

kwargs Unpacking

↓

Formatted Output
```

Example:

Alice:
Present=5
Absent=1

---

# 9. Why tuple output contains comma?

Example:

```python
(5,)
```

Single-element tuples require commas.

---

# 10. Can keyword arguments become *args?

No.

This fails:

```python
f(*{"name":"Alice"})
```

because * expands keys.

Correct:

```python
f(**{
"name":"Alice"
})
```

---

# 11. Real-world Patterns

Checkout:

```python
checkout(
 "Alice",
 "Laptop",
 "Mouse"
)
```

Registration:

```python
register(
 "user",
 email="..."
)
```

Reports:

```python
report(
 "Python",
 80,
 90,
 trainer="John"
)
```

---

# Key Takeaways

✔ *args → tuple

✔ **kwargs → dictionary

✔ * → unpack positional

✔ ** → unpack named

✔ Flexible APIs

✔ Cleaner reusable functions

# Lesson 16 — Decorators

---

# What is a Decorator?

A decorator is a function that **receives another function**, adds extra behavior, and returns an enhanced version of that function **without modifying the original function itself**.

Think of it as wrapping an existing function with additional functionality.

```
Function
    │
    ▼
Decorator
    │
    ▼
Enhanced Function
```

---

# Why Decorators?

Without decorators:

```python
def login():
    print("Logging started")
    print("User logged in")
```

Every function would need repeated logging, timing, authentication, auditing, etc.

Decorators allow us to write that extra code **once** and reuse it everywhere.

---

# Functions are Objects

Functions can be:

- stored in variables
- passed to other functions
- returned from other functions

Example:

```python
def greet():
    print("Hello")

say_hi = greet

say_hi()
```

Output:

```
Hello
```

---

# Passing Functions

```python
def greet():
    print("Hello")

def execute(func):
    func()

execute(greet)
```

Notice:

```
execute(greet)
```

NOT

```
execute(greet())
```

The function itself is being passed.

---

# Basic Decorator Structure

```python
def decorator(func):

    def inner():

        # extra work

        func()

        # extra work

    return inner
```

The wrapper (`inner`) runs instead of the original function.

---

# Using @ Syntax

Instead of

```python
greet = decorator(greet)
```

Python provides shorthand:

```python
@decorator
def greet():
    print("Hello")
```

---

# Execution Flow

When

```python
greet()
```

is called,

Python actually executes

```
inner()
```

which then executes

```
func()
```

(the original function).

---

# Decorator with Arguments

Functions with parameters require the wrapper to accept them too.

Example:

```python
def decorator(func):

    def inner(name):
        print("Before")

        func(name)

        print("After")

    return inner
```

---

# Generic Decorators

A reusable decorator should accept any arguments.

Use:

```python
def inner(*args, **kwargs):
```

This allows the decorator to wrap any function.

Example:

```python
def log(func):

    def inner(*args, **kwargs):

        result = func(*args, **kwargs)

        return result

    return inner
```

This is considered the professional approach.

---

# Returning Values

If the original function returns something, the decorator should return it too.

Example:

```python
result = func(*args, **kwargs)

return result
```

Otherwise the caller loses the returned value.

---

# Decorators Used This Lesson

## Registration Logger

Added

```
Registration Log Updated!
```

without changing registration logic.

---

## Audit Logger

Added

```
Audit Entry Created
```

after successful login attempts.

---

## Generic Audit Decorator

One decorator wrapped:

- Login
- Registration
- Logout

using

```python
*args
**kwargs
```

---

## Attendance Report Logger

Decorator displayed

```
Generating Attendance Report...
```

before generating reports.

---

## Transaction Audit

Decorator handled

```
Transaction Audit Started...

Transaction Audit Completed
```

around transaction processing.

---

## Execution Counter

Decorator displayed

```
Function called X time(s)
```

before function execution.

---

# Real-world Uses

Decorators are heavily used for:

- Logging
- Auditing
- Authentication
- Authorization
- Performance Timing
- Retry Logic
- Permission Checks
- API Monitoring
- Database Transactions
- Caching

---

# Important Concepts

A decorator

- accepts a function
- creates an inner wrapper
- performs extra work
- executes the original function
- optionally returns its result
- returns the wrapper

---

# Common Mistakes

### Forgetting to call the original function

```python
func()
```

---

### Forgetting

```python
return inner
```

---

### Forgetting to return the original result

```python
result = func()

return result
```

---

### Not accepting arguments

Instead of

```python
def inner():
```

prefer

```python
def inner(*args, **kwargs):
```

for reusable decorators.

---

# Decorators vs Normal Functions

Normal Function

- Performs work directly.

Decorator

- Adds behavior before or after another function.

---

# Decorator Flow

```
Function Call

↓

Decorator Wrapper Starts

↓

Extra Code

↓

Original Function

↓

Extra Code

↓

Return Result
```

---

# Lesson Summary

You learned:

- Functions are first-class objects.
- Functions can be passed into other functions.
- Decorators wrap existing functions.
- `@decorator` is shorthand syntax.
- Decorators help eliminate duplicate code.
- `*args` and `**kwargs` make decorators reusable.
- Decorators are widely used in production software for logging, auditing, authentication, monitoring, and timing.

---

# Key Takeaways

✓ A decorator enhances a function without modifying it.

✓ Always return the wrapper.

✓ Reusable decorators should use `*args` and `**kwargs`.

✓ Return the wrapped function's result whenever appropriate.

✓ Decorators promote clean, reusable, maintainable code.
# Lesson 16 — Decorators — Problems

---

## Exercise 1 — First Decorator

Create a decorator:

```
announce()
```

It should print

```
Starting...
```

before executing the decorated function.

Decorate:

```
say_hello()
```

Expected Output:

```
Starting...
Hello
```

---

## Exercise 2 — Before and After

Create a decorator

```
surround()
```

It should print

```
Before
```

before the function and

```
After
```

after the function.

Decorate

```
greet()
```

---

## Exercise 3 — Login Audit

### Part 1

Create a user registration program.

Requirements:

- Store usernames/passwords in a file.
- Reject duplicate usernames.
- Allow three attempts.
- Use a decorator to display

```
Registration Log Updated!
```

after registration.

---

### Part 2

Create a login program.

Requirements:

- Read registered users.
- Validate username/password.
- Record login attempts.
- Maintain an audit log file.
- Decorate the login function with

```
Audit Entry Created
```

after execution.

---

## Exercise 4 — One Decorator, Multiple Functions

Create one reusable decorator.

Use it with:

- Registration
- Login
- Logout

Requirements:

- Accept any function arguments.
- Print

```
Log Updated Successfully
```

after successful execution.

---

## Exercise 5 — Predict Output

Predict before running:

```python
def decorator(func):

    def inner():
        print("A")
        func()
        print("B")

    return inner

@decorator
def test():
    print("C")

test()
```

Explain carefully.

---

# Use Case 1 — Attendance Report Logger

Build an attendance report system.

Requirements:

- Collect employee details.
- Record punch in/out.
- Generate report.txt.
- Decorate the report generator.

Decorator should display

```
Generating Attendance Report...
```

before report generation.

Additional cases tested:

- Successful punch in/out
- Missed punch in
- Missed punch out
- Invalid employee number
- Invalid punch symbols

---

# Use Case 2 — Transaction Audit System

Build a transaction processor.

Requirements:

- Accept credit entries.
- Accept debit entries.
- Store transactions.
- Generate transaction log.
- Decorate transaction reporting.

Decorator prints:

```
Transaction Audit Started...

Transaction Audit Completed
```

Additional cases tested:

- Multiple credits
- Multiple debits
- Decimal values
- Invalid amount
- Invalid menu option
- Exit workflow

---

# Challenge — Execution Counter

Create a decorator:

```
execution_counter()
```

Each function call should display

```
Function called 1 time(s)
Function called 2 time(s)
Function called 3 time(s)
...
```

Requirements:

- Allow repeated execution.
- Maintain call count.
- Exit gracefully.

---

# Concepts Practiced

- Basic decorators
- Wrapper functions
- Passing functions
- Returning wrapper functions
- Decorator syntax (`@`)
- Decorators with parameters
- Returning function results
- Generic decorators using `*args`
- Generic decorators using `**kwargs`
- Login systems
- Registration systems
- Audit logging
- Report generation
- Transaction logging
- File handling
- Exception handling
- Reusable software components
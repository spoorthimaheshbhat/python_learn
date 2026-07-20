# Lesson 18 - Object-Oriented Programming (Part 1)

## Overview

Object-Oriented Programming (OOP) is a programming paradigm that models real-world entities as objects. Instead of storing related data in dictionaries or lists, OOP groups both data (attributes) and behavior (methods) into a single unit called a class.

---

## Topics Covered

- Classes
- Objects
- Constructors (`__init__`)
- Instance Variables
- Instance Methods
- The `self` keyword
- Creating Multiple Objects
- Updating Object Attributes

---

## Key Concepts

### Class

A class is a blueprint used to create objects.

Example:

```python
class Employee:
    pass
```

---

### Object

An object is an instance of a class.

```python
john = Employee()
mary = Employee()
```

Each object represents a separate real-world entity.

---

### Constructor

The constructor (`__init__`) automatically executes whenever a new object is created.

```python
class Employee:

    def __init__(self, name):
        self.name = name
```

---

### self

`self` refers to the current object.

```python
self.name = name
```

Each object stores its own copy of the data.

---

### Instance Variables

Variables attached to individual objects.

```python
self.name
self.department
self.status
```

Every object has independent values.

---

### Instance Methods

Functions that belong to a class.

```python
def greet(self):
    print(f"Hello {self.name}")
```

Called using

```python
employee.greet()
```

---

### Updating Attributes

Object attributes can be modified after creation.

```python
employee.department = "Automation QA"
```

---

## Real-world Analogy

Think of a company.

The Employee class is a blank employee form.

Every employee object is a completed form containing different information.

```
Employee Form

Name:
Department:
Status:
```

↓

```
John
QA
ACTIVE
```

↓

```
Mary
HR
INACTIVE
```

The form (class) never changes.

Only the values (objects) change.

---

## Important Takeaway

One object should represent one real-world entity.

Correct:

```python
john = Employee(...)
mary = Employee(...)
```

Incorrect:

```python
Employee("John", "Mary", "Alice")
```

One employee object should never represent multiple employees.

---

## OOP and Automation Testing

Automation frameworks like Selenium and Playwright use OOP extensively.

Example:

```python
login_page = LoginPage()

login_page.enter_username()
login_page.enter_password()
login_page.click_login()
```

The Page Object Model (POM) is built entirely around classes and objects.

---

## Lesson Summary

After this lesson you should understand:

- What a class is
- What an object is
- Why constructors exist
- Why `self` is required
- How objects store their own data
- How methods represent object behavior
- Why OOP is essential for automation frameworks
# Lesson 18 - OOP Part 1 Exercises

## Exercise 1

Create an empty class named `Student`.

Create one object.

Print:

- the object
- its type

---

## Exercise 2

Create a `Car` class.

The constructor should initialize the car.

Create multiple car objects.

Display:

```
<Car Name> -> Car Created
```

---

## Exercise 3

Create a `Book` class.

Store:

- title
- author

Create multiple books.

Display a release announcement for each.

---

## Exercise 4

Create an `Employee` class.

Store:

- Employee Name
- Employee ID
- Department
- Status

Implement:

- create employee record
- view all employees
- search employee by ID

Store records inside a JSON file.

---

## Exercise 5

Create a `Student` class.

Store:

- Student Name
- Marks
- Result

Read student information from JSON.

Search by Student ID.

Display:

```
<Name> has scored <Marks>

Result -> PASS / FAIL
```

Handle:

- FileNotFoundError
- JSONDecodeError

---

## Exercise 6

Predict the output.

```python
class Dog:

    def __init__(self):
        print("Dog Created")

dog = Dog()
```

Explain why the output occurs.

---

## Exercise 7

Create a `Rectangle` class.

Store:

- length
- width

Create a method:

```python
area()
```

Return the area.

---

## Exercise 8

Create a `Circle` class.

Store:

- radius

Create a method:

```python
circumference()
```

Use:

```
π = 3.14
```

---

# Use Case 1

## Employee Management System

Build an Employee class.

Store:

- Employee Name
- Employee ID
- Department
- Status

Implement:

- Create Employee
- View All Employees
- Search by Employee ID

### Enhancement

Add:

- View Active Employees
- View Inactive Employees

Persist data in JSON.

---

# Use Case 2

## QA Test Case Manager

Create a TestCase class.

Store:

- Test ID
- Feature
- Priority
- Status

Implement methods:

- display_record()
- mark_pass()
- mark_fail()

Allow the user to modify test status repeatedly.

---

# Challenge

## Library Management System

Create a Book class.

Store:

- Book ID
- Title
- Author
- Availability

Implement:

- Add Book
- Search Book
- Borrow Book
- Return Book

Persist the catalogue using JSON.

### Requirements

- Prevent borrowing unavailable books.
- Prevent returning already available books.
- Handle missing JSON files.
- Handle invalid JSON data.
- Maintain catalogue consistency after updates.
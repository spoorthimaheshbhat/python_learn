# Lesson 17 — Problems

---

## Exercise 1

Convert a Python dictionary into a JSON string using `json.dumps()`.

---

## Exercise 2

Convert the following JSON string into a Python dictionary.

```python
'{"city":"London","country":"UK"}'
```

---

## Exercise 3

Write multiple student records into `student.json`.

Requirements

- Use `json.dump()`
- Format with `indent=4`
- Use a decorator to display write status

---

## Exercise 4

Read `student.json`.

Print

- Entire list
- Student name
- Student marks

Use a decorator.

---

## Exercise 5

Update JSON records.

Requirement

If

```
course == "Python"
```

set

```
city = "NY"
```

Else

```
city = "LA"
```

Save changes correctly.

---

## Exercise 6

Predict output

```python
data = {
    "x":10
}

text = json.dumps(data)

print(type(text))
print(text)
```

Explain carefully.

---

# Use Case 1

## Employee Database

Build a JSON employee management system.

Features

- Add employee
- View employees
- Employee count
- Handle empty JSON
- Automatically create JSON file

Enhancements

- Active employee count
- Inactive employee count
- Search employee by ID
- Exception handling
- Persistent storage

---

# Use Case 2

## QA Test Report Generator

Create a test execution reporting system.

Store

- Test ID
- Feature
- Status
- Execution time
- Tester

Requirements

- Append reports
- Store in JSON
- Handle empty file
- Decorator for execution message

---

# Challenge

Extend Employee Database

Implement

- Add Employee
- View Employees
- Count Active Employees
- Count Inactive Employees
- Search by Employee ID

Store all information inside JSON.

---

# Extra Concepts Explored

- Difference between dump() and dumps()
- Difference between load() and loads()
- JSON arrays
- List of dictionaries
- Updating JSON records
- File pointer behaviour
- seek()
- truncate()
- JSONDecodeError
- CRUD workflow
- Using decorators with JSON operations
- Building reusable JSON mini-applications
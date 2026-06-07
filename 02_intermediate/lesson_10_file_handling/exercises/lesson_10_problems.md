# Lesson 10 - File Handling
## Exercise Problems Only

### Exercise 1

Create a file called:

```text
greeting.txt
```

Write:

```text
Hello Python
```

Then read the file and display its contents.

Handle:

```python
FileNotFoundError
```

---

### Exercise 2

Ask user for a message.

Save it into:

```text
message.txt
```

using write mode.

Run multiple times and observe what happens to previous content.

Explain why.

---

### Exercise 3

Create:

```text
log.txt
```

Write a program that:

- Attempts to read a file
- Records success or failure
- Appends results into log.txt

Example:

```text
Read Success
Read Fail
Read Success
```

Extra cases explored:

- Logging multiple runs
- Reading existing files repeatedly
- Automated success logging

---

### Exercise 4

Create:

```text
languages.txt
```

Count total lines inside the file.

Display:

```text
Total lines
```

Extra challenge explored:

Subtract header line to determine:

```text
Total known languages
```

Example:

```text
Known Languages:
Python
Java
C++
```

Output:

```text
Total lines: 4
Total known languages: 3
```

---

### Exercise 5

Create:

```text
passage.txt
```

Count total number of words.

Display:

```text
Total words
```

Use:

```python
split()
```

---

# Real World Challenge 1

## Language Tracker

Build an application that:

- Creates languages.txt
- Accepts language input
- Saves entries
- Allows multiple additions
- Stops when user enters N

Requirements:

- Functions
- Loops
- File append mode
- Input validation

Extra cases explored:

- Invalid Y/N responses
- Multiple runs
- File overwrite behaviour
- Large language lists

---

# Real World Challenge 2

## Notes App

Build a note-taking application.

Menu:

```text
1. Add Note
2. View Notes
3. Clear All Notes
4. Exit
```

Requirements:

- Store notes in file
- View existing notes
- Clear notes
- Exit application

Extra cases explored:

- Multiple notes
- Invalid requests
- Clearing notes
- Viewing empty notes

---

# Real World Challenge 3

## Expense Tracker

Create an expense tracking application.

Menu:

```text
add
show total
exit
```

Requirements:

- Store expenses in file
- Validate input
- Allow only positive integers
- Calculate total expenses

Extra cases explored:

- Invalid text input
- Negative values
- Zero expense
- Empty expense file
- Multiple additions

---

# Real World Challenge 4

## Login Audit System

Files:

```text
credentials.txt
login_log.txt
```

Requirements:

- Read credentials from file
- Convert credentials into dictionary
- Validate login
- Allow 3 attempts
- Lock account after failures
- Record all attempts

Log format:

```text
SUCCESS: username
FAILED: username
```

Extra cases explored:

- Successful logins
- Failed logins
- Account lock
- Historical log persistence
- Whitespace cleanup using strip()
- Parsing CSV-style credential records

---

# Concept Checks

### Predict Output 1

```python
with open("data.txt", "w") as file:
    file.write("Hello")
```

What happens if data.txt already exists?

Explain.

---

### Predict Output 2

```python
with open("data.txt", "a") as file:
    file.write("World")
```

How is append mode different from write mode?

Explain.

---

### Predict Output 3

```python
line = "admin,password"
username, password = line.split(",")
```

What values are stored in:

```python
username
password
```

---

### Predict Output 4

```python
line = " admin "
print(line.strip())
```

Explain the output.

---

### Predict Output 5

```python
with open("missing.txt", "r") as file:
    data = file.read()
```

What exception occurs?

How should it be handled?
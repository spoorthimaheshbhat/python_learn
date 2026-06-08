# Lesson 11 — List Comprehensions
## Exercise Problems Only

---

## Exercise 1 — Basic List Comprehension

Create a list containing numbers from 1 to 10 using a list comprehension.

Expected output:

```python
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

## Exercise 2 — Squares

Create a list of squares for numbers 1 through 10.

Expected output:

```python
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

---

## Exercise 3 — Even Numbers

Create a list containing only even numbers from 1 to 20.

Expected output:

```python
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

---

## Exercise 4 — Odd Numbers

Create a list containing only odd numbers from 1 to 20.

Expected output:

```python
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

---

## Exercise 5 — Convert To Uppercase

Given:

```python
words = ["python", "java", "c++"]
```

Create a new list with all words converted to uppercase.

Expected output:

```python
['PYTHON', 'JAVA', 'C++']
```

---

## Exercise 6 — Word Lengths

Given:

```python
words = ["apple", "banana", "kiwi", "mango"]
```

Create a list containing the length of each word.

Expected output:

```python
[5, 6, 4, 5]
```

---

## Exercise 7 — Numbers Greater Than 50

Given:

```python
numbers = [12, 60, 43, 78, 90, 15]
```

Create a list containing only numbers greater than 50.

Expected output:

```python
[60, 78, 90]
```

---

## Exercise 8 — Vowel Extraction

Given:

```python
word = "programming"
```

Create a list containing only vowels.

Expected output:

```python
['o', 'a', 'i']
```

---

## Exercise 9 — Even/Odd Labels

Given:

```python
numbers = [1, 2, 3, 4, 5]
```

Create:

```python
['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

using a list comprehension.

---

## Exercise 10 — Flatten a Matrix

Given:

```python
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
```

Convert it into:

```python
[1, 2, 3, 4, 5, 6]
```

using a list comprehension.

---

## Exercise 11 — Real-World: Clean Usernames

Given:

```python
usernames = [
    " Alice ",
    " Bob ",
    " Charlie ",
    " David "
]
```

Create a cleaned list without leading or trailing spaces.

Expected output:

```python
['Alice', 'Bob', 'Charlie', 'David']
```

---

## Exercise 12 — Real-World: Extract Email Domains

Given:

```python
emails = [
    "john@gmail.com",
    "sam@yahoo.com",
    "alice@outlook.com",
    "admin@company.com"
]
```

Create a list containing only domains.

Expected output:

```python
[
    'gmail.com',
    'yahoo.com',
    'outlook.com',
    'company.com'
]
```

---

# Bonus Challenges

## Bonus 1

Given:

```python
numbers = [1, 2, 3, 4, 5]
```

Create:

```python
[10, 20, 30, 40, 50]
```

using a single list comprehension.

---

## Bonus 2

Given:

```python
words = ["python", "java", "go", "rust"]
```

Create a list containing only words longer than 3 characters.

Expected output:

```python
['python', 'java', 'rust']
```

---

## Bonus 3

Given:

```python
sentence = "Python Is Awesome"
```

Create a list containing every character converted to lowercase.

---

## Bonus 4

Given:

```python
numbers = [1, 2, 3, 4, 5, 6]
```

Create:

```python
['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']
```

using a single comprehension.

---

## Bonus 5 — Real World

Given:

```python
employees = [
    {
        "name": "Alice",
        "salary": 50000
    },
    {
        "name": "Bob",
        "salary": 70000
    },
    {
        "name": "Charlie",
        "salary": 45000
    }
]
```

Create a list containing names of employees whose salary is greater than 50,000.

Expected output:

```python
['Bob']
```

---

# Stretch Challenge

Create a mini report from:

```python
students = [
    ("Alice", 85),
    ("Bob", 45),
    ("Charlie", 92),
    ("David", 60)
]
```

Generate:

```python
[
    "Alice - Pass",
    "Bob - Fail",
    "Charlie - Pass",
    "David - Pass"
]
```

using a single list comprehension.
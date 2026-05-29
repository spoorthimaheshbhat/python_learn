# Lesson 3 — Strings

# Concepts Covered

* String creation
* String immutability
* String indexing
* Negative indexing
* String slicing
* Step slicing
* String reversal
* String methods
* String concatenation
* String repetition
* f-strings
* Escape characters
* `split()`
* String transformations

---

# What Is a String?

A string is a sequence of characters.

Example:

```python id="0i56df"
name = "Jodii"
```

Strings can contain:

* letters
* numbers
* symbols
* spaces

Example:

```python id="6ysxpw"
message = "Python 3.12 is awesome!"
```

---

# String Creation

Strings can use:

* single quotes
* double quotes
* triple quotes

Examples:

```python id="9njlwm"
a = 'Hello'
b = "Hello"
c = """Multi-line
string"""
```

---

# Strings Are Immutable

Strings cannot be changed directly after creation.

Example:

```python id="hr97m9"
word = "Python"
```

This is NOT allowed:

```python id="c9c49i"
word[0] = "J"
```

This causes:

```python id="n9jlwm"
TypeError
```

because strings are immutable.

---

# String Indexing

Each character has an index position.

Example:

```python id="r53lm9"
word = "Python"
```

| Character | P | y | t | h | o | n |
| --------- | - | - | - | - | - | - |
| Index     | 0 | 1 | 2 | 3 | 4 | 5 |

---

# Access Characters

```python id="twp0ti"
word = "Python"

print(word[0])
print(word[3])
```

Output:

```python id="tf9jlwm"
P
h
```

---

# Negative Indexing

Python supports reverse indexing.

| Character      | P  | y  | t  | h  | o  | n  |
| -------------- | -- | -- | -- | -- | -- | -- |
| Negative Index | -6 | -5 | -4 | -3 | -2 | -1 |

Example:

```python id="kwjlwm"
print(word[-1])
```

Output:

```python id="rjlwm8"
n
```

Negative indexing is useful because:

* avoids needing `len()`
* cleaner syntax
* common in parsing logic

---

# String Slicing

Extract parts of a string.

Syntax:

```python id="v7s3bt"
string[start:end]
```

Important:

* start index included
* end index excluded

Example:

```python id="l9jlwm"
word = "Python"

print(word[0:2])
```

Output:

```python id="0jlwmx"
Py
```

---

# Common Slicing Patterns

## First 3 characters

```python id="cjlwm7"
word[:3]
```

---

## Last 3 characters

```python id="xjlwm6"
word[-3:]
```

---

## Full copy

```python id="1jlwm5"
word[:]
```

---

## Reverse string

```python id="8jlwm4"
word[::-1]
```

Example:

```python id="yjlwm3"
"Python"[::-1]
```

Output:

```python id="pjlwm2"
nohtyP
```

---

# Step Slicing

General slicing format:

```python id="hjlwm1"
[start:end:step]
```

Example:

```python id="4jlwm0"
[::-1]
```

means:

* start from end
* move backward
* step = -1

---

# String Length

Use `len()`.

Example:

```python id="zjlwm9"
word = "Python"

print(len(word))
```

Output:

```python id="jjlwm8"
6
```

---

# String Methods

Methods are built-in functions attached to objects.

---

# Common String Methods

| Method          | Purpose           |
| --------------- | ----------------- |
| `.lower()`      | lowercase         |
| `.upper()`      | uppercase         |
| `.title()`      | title case        |
| `.strip()`      | remove spaces     |
| `.replace()`    | replace text      |
| `.find()`       | find index        |
| `.count()`      | count occurrences |
| `.startswith()` | starts with       |
| `.endswith()`   | ends with         |
| `.split()`      | split into list   |

---

# `.lower()` and `.upper()`

```python id="6jlwm7"
text = "Python"

print(text.lower())
print(text.upper())
```

Output:

```python id="mjlwm6"
python
PYTHON
```

---

# `.strip()`

Removes extra spaces.

```python id="8jlwm5"
text = "   hello   "

print(text.strip())
```

Output:

```python id="2jlwm4"
hello
```

Important:

* methods like `strip()` return NEW strings
* original string is unchanged unless reassigned

Correct usage:

```python id="tjlwm3"
text = text.strip()
```

---

# `.replace()`

```python id="ujlwm2"
text = "I like Java"

print(text.replace("Java", "Python"))
```

Output:

```python id="ejlwm1"
I like Python
```

---

# `.find()`

Returns index.

```python id="kjlwm0"
text = "Python"

print(text.find("t"))
```

Output:

```python id="3jlwm9"
2
```

If not found:

```python id="sjlwm8"
print(text.find("z"))
```

Output:

```python id="ljlwm7"
-1
```

---

# `.count()`

```python id="5jlwm6"
text = "banana"

print(text.count("a"))
```

Output:

```python id="gjlwm5"
3
```

---

# `.split()`

Converts strings into lists.

```python id="cjlwm4"
text = "apple,banana,mango"

print(text.split(","))
```

Output:

```python id="fjlwm3"
['apple', 'banana', 'mango']
```

Real-world usage:

* CSV parsing
* log parsing
* command parsing
* API responses
* automation inputs

Example:

```python id="yjlwm2"
"GET /users/123".split("/")
```

---

# String Concatenation

Joining strings.

```python id="djlwm1"
first = "Hello"
second = "World"

print(first + " " + second)
```

Output:

```python id="wjlwm0"
Hello World
```

---

# String Repetition

```python id="rjlwm9"
print("ha" * 3)
```

Output:

```python id="qjlwm8"
hahaha
```

---

# f-Strings

Modern string formatting.

Example:

```python id="zjlwm7"
name = "Sam"
age = 50

print(f"My name is {name} and I am {age} years old.")
```

f-strings are heavily used in:

* logging
* automation
* APIs
* debugging
* reports
* AI prompts

---

# Escape Characters

| Escape | Meaning      |
| ------ | ------------ |
| `\n`   | new line     |
| `\t`   | tab          |
| `\"`   | double quote |
| `\'`   | single quote |

Example:

```python id="4jlwm6"
print("Hello\nWorld")
```

Output:

```python id="njlwm5"
Hello
World
```

---

# Exercise 1 — String Indexing

```python id="hjlwm4"
language = "Python"

print(f"""first character: {language[0]}
last character: {language[-1]}
third character: {language[2]}""")
```

Output:

```python id="vjlwm3"
first character: P
last character: n
third character: t
```

---

# Exercise 2 — String Slicing

```python id="0jlwm2"
word = "Programming"

print(f"""First 4 characters are: {word[0:4]}
Last 4 characters are: {word[-4:]}
Reversed string is: {word[::-1]}""")
```

Output:

```python id="7jlwm1"
First 4 characters are: Prog
Last 4 characters are: ming
Reversed string is: gnimmargorP
```

---

# Exercise 3 — String Methods

```python id="3jlwm0"
text = "   python programming   "

text = text.strip()

print(text)
print(text.upper())
print(text.replace("python", "Java"))
print(text.count("m"))
```

Output:

```python id="xjlwm9"
python programming
PYTHON PROGRAMMING
Java programming
2
```

---

# Exercise 4 — String Concatenation

```python id="9jlwm8"
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(first_name + " " + last_name)
```

Alternative using f-strings:

```python id="zjlwm7"
print(f"{first_name} {last_name}")
```

---

# Exercise 5 — f-Strings

```python id="4jlwm6"
name = input("Enter your name: ")
age = input("Enter your age: ")
fav_language = input("Enter your favorite language: ")

print(f"My name is {name}, I am {age} years old, and my favorite language is {fav_language}.")
```

---

# Exercise 6 — split()

```python id="1jlwm5"
fruits = "apple,mango,banana,grapes"

list_fruits = fruits.split(",")

print(f"Full list is: {list_fruits}")
print(f"First fruit is: {list_fruits[0]}")
print(f"Last fruit is: {list_fruits[-1]}")
```

Output:

```python id="yjlwm4"
Full list is: ['apple', 'mango', 'banana', 'grapes']
First fruit is: apple
Last fruit is: grapes
```

---

# Exercise 7 — String Immutability

```python id="rjlwm3"
text = "Python"
text[0] = "J"

print(text)
```

This causes:

```python id="mjlwm2"
TypeError
```

Reason:

* strings are immutable
* characters cannot be modified directly

Correct approach:

```python id="j’wini1"
text = "J" + text[1:]
```

Output:

```python id="5jlwm0"
Jython
```

---

# Important Learnings

* Strings are sequences of characters.
* Strings are immutable.
* Strings support indexing and slicing.
* Negative indexing accesses characters from the end.
* Slicing excludes the ending index.
* `[::-1]` reverses strings.
* String methods return new strings.
* `split()` converts strings into lists.
* `replace()` replaces text.
* `find()` returns index or `-1`.
* `count()` counts occurrences.
* f-strings provide clean formatting.
* Escape characters add formatting behavior.
* Immutable objects require reassignment for transformations.

# Lesson 7 - Loops

## What is a Loop?

A loop repeats a block of code multiple times.

Loops are used to:

- Process collections of data
- Automate repetitive tasks
- Search through data
- Count occurrences
- Validate input
- Build algorithms

---

# for Loop

Used when iterating over a collection or a known range of values.

Example:

```python
for number in [10, 20, 30]:
    print(number)
```

Output:

```
10
20
30
```

---

# Iterating Through Strings

Strings are iterable.

```python
word = "Python"

for char in word:
    print(char)
```

Output:

```
P
y
t
h
o
n
```

---

# range()

Used to generate sequences of numbers.

## range(stop)

```python
range(5)
```

Produces:

```
0, 1, 2, 3, 4
```

Note:
- Starts at 0
- Excludes stop value

---

## range(start, stop)

```python
range(3, 8)
```

Produces:

```
3, 4, 5, 6, 7
```

---

## range(start, stop, step)

```python
range(0, 11, 2)
```

Produces:

```
0, 2, 4, 6, 8, 10
```

---

# while Loop

Used when the number of repetitions is unknown.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```
1
2
3
4
5
```

---

# Infinite Loops

Example:

```python
while True:
    print("Hello")
```

This loop never ends unless interrupted.

---

# break

Terminates a loop immediately.

Example:

```python
for i in range(10):
    if i == 5:
        break

    print(i)
```

Output:

```
0
1
2
3
4
```

---

# continue

Skips the current iteration and proceeds to the next.

Example:

```python
for i in range(5):
    if i == 2:
        continue

    print(i)
```

Output:

```
0
1
3
4
```

---

# enumerate()

Provides both index and value.

Example:

```python
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output:

```
0 apple
1 banana
2 mango
```

---

# Counting Pattern

Common use of loops.

Example:

```python
count = 0

for char in "programming":
    if char == "m":
        count += 1

print(count)
```

Output:

```
2
```

---

# Searching Pattern

Example:

```python
numbers = [10, 20, 30, 40]

found = False

for num in numbers:
    if num == 30:
        found = True
        break

print(found)
```

Output:

```
True
```

---

# Important Concepts Learned During Exercises

## Boolean Flag Pattern

Instead of:

```python
count = 0
```

Use:

```python
found = False
```

When searching for something.

Example:

```python
found = False

for num in numbers:
    if num == 30:
        found = True
        break
```

Benefits:

- More readable
- Clearly communicates intent

---

## Case-Insensitive Comparisons

Convert characters to lowercase before comparison.

Example:

```python
if char.lower() in "aeiou":
```

Allows:

```text
PROGRAMMING
```

to be processed correctly.

---

## Nested Loops

Outer loop controls rows.

Inner loop controls items within each row.

Example:

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end="")

    print()
```

Output:

```
*
**
***
****
*****
```

---

## Building Strings with Loops

Instead of printing characters individually:

```python
print(word[i])
```

Build a new string:

```python
reverse_word += word[i]
```

Example:

```python
word = "Python"
reverse_word = ""

i = -1

while i != -(len(word) + 1):
    reverse_word += word[i]
    i -= 1

print(reverse_word)
```

Output:

```
nohtyP
```

---

# Truthy and Falsy Values

Python treats some values as False automatically.

Falsy values:

```python
0
0.0
""
[]
{}
set()
None
False
```

Everything else is generally considered True.

Examples:

```python
if "":
```

Evaluates to False.

```python
if [1]:
```

Evaluates to True.

---
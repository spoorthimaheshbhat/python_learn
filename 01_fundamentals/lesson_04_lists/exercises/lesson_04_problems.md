# Lesson 4 — Lists — Exercise Problems

## Exercise 1 — List Creation and Indexing

Create:

```python
colors = ["red", "blue", "green", "yellow"]
```

Print:

* first color
* last color
* second color

using indexing.

---

## Exercise 2 — List Slicing

Using:

```python
numbers = [10, 20, 30, 40, 50, 60]
```

Print:

* first 3 numbers
* last 2 numbers
* reversed list

using slicing.

---

## Exercise 3 — List Methods

Create:

```python
fruits = ["apple", "banana"]
```

Perform:

* append `"mango"`
* insert `"orange"` at index 1
* remove `"banana"`
* print final list

---

## Exercise 4 — Sorting

Create:

```python
numbers = [4, 1, 8, 3, 2]
```

Print:

* sorted ascending
* sorted descending

---

## Exercise 5 — Copying Lists

Predict output BEFORE running:

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)
```

Explain WHY output occurs.

Then create a proper independent copy.

---

## Exercise 6 — Nested Lists

Create:

```python
matrix = [
    [1, 2],
    [3, 4]
]
```

Print:

* `1`
* `4`

using nested indexing.

---

## Exercise 7 — Loop Through List

Using:

```python
animals = ["cat", "dog", "rabbit"]
```

Print each animal using a `for` loop.

---

## Exercise 8 — Membership Operator

Check whether:

* `"apple"` exists in a fruit list
* `"grape"` exists in a fruit list

using `in`.

---

## Exercise 9 — count() and index()

Using:

```python
numbers = [1, 2, 2, 3, 2, 4]
```

Print:

* how many times `2` appears
* index of first occurrence of `3`

---

## Exercise 10 — List vs String Mutability

Predict output BEFORE running:

```python
text = "Python"
items = [1, 2, 3]

text[0] = "J"
items[0] = 100

print(text)
print(items)
```

Explain why one fails and the other works.

---

# Advanced Extra Problems

## Exercise 11 — Understanding `len()` and Negative Indexing

Predict the output BEFORE running:

```python
numbers = [10, 20, 30, 40]

print(len(numbers))
print(numbers[-1])
print(numbers[-2])
```

Explain each output.

---

## Exercise 12 — Copy vs Reference

Predict the output BEFORE running:

```python
a = [1, 2, 3]
b = a.copy()

b.append(4)

print(len(a))
print(len(b))
print(a[-1])
print(b[-1])
```

Explain why the outputs differ.

---

## Exercise 13 — Reference Assignment

Predict the output BEFORE running:

```python
a = [1, 2, 3]
b = a

b.append(4)

print(len(a))
print(len(b))
print(a[-1])
print(b[-1])
```

Explain why all outputs are the same.

---

## Exercise 14 — Identity vs Equality

Predict the output BEFORE running:

```python
a = [1, 2, 3]
b = a

print(a is b)
print(a == b)
```

Explain the difference between `is` and `==`.

---

## Exercise 15 — Identity vs Equality with Copies

Predict the output BEFORE running:

```python
a = [1, 2, 3]
b = a.copy()

print(a is b)
print(a == b)
```

Explain why one result changes while the other stays the same.

---

## Exercise 16 — Combining List Methods

Create:

```python
numbers = [5, 2, 8, 1]
```

Perform the following operations in order:

1. Append `10`
2. Insert `3` at index `1`
3. Remove `8`
4. Sort the list
5. Reverse the list

Print the final list.

---

## Exercise 17 — Nested List Challenge

Using:

```python
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```

Print:

* `20`
* `60`
* `70`
* `90`

using nested indexing only.

---

## Exercise 18 — Membership and Counting

Using:

```python
fruits = ["apple", "banana", "apple", "mango", "apple"]
```

Print:

* whether `"banana"` exists
* whether `"grape"` exists
* how many times `"apple"` appears

---

## Exercise 19 — Loop and Index

Using:

```python
colors = ["red", "blue", "green"]
```

Print:

```text
Index 0 -> red
Index 1 -> blue
Index 2 -> green
```

using a loop.

---

## Exercise 20 — Mixed Data Types

Create a list containing:

* your name
* your age
* a boolean value
* a floating-point number

Print:

* the entire list
* the type of each element using `type()`

Example:

```python
data = ["Spoorthi", 27, True, 95.5]
```

---

## Exercise 21 — List Concatenation

Create:

```python
a = [1, 2]
b = [3, 4]
```

Combine them using the `+` operator and print the result.

Expected output:

```python
[1, 2, 3, 4]
```

---

## Exercise 22 — List Repetition

Predict the output BEFORE running:

```python
print([1] * 5)
print(["Python"] * 3)
```

Explain how list repetition works.

---

## Exercise 23 — Mini Challenge

Create an empty list.

Ask the user to enter three favorite movies using `input()`.

Store each movie in the list.

Finally print:

```text
Your favorite movies are:
<Movie 1>
<Movie 2>
<Movie 3>
```

using a loop.

---

## Exercise 24 — Comprehensive List Challenge

Create:

```python
numbers = [12, 5, 8, 12, 20, 5]
```

Perform all of the following:

1. Print the length of the list.
2. Print the first element.
3. Print the last element.
4. Count how many times `5` appears.
5. Find the index of the first `12`.
6. Sort the list.
7. Reverse the list.
8. Check whether `20` exists in the list.
9. Create a copy of the list.
10. Append `100` to the copied list only.

Print both lists and explain why they are different.

# Lesson 4 — Lists

## Concepts Covered

* List creation
* List indexing
* Negative indexing
* List slicing
* List mutability
* List methods
* Sorting
* Membership checks
* Nested lists
* Iteration
* List copying
* References vs copies

---

# What Is a List?

A list is an ordered, mutable collection of items.

Example:

```python
fruits = ["apple", "banana", "mango"]
```

Lists can contain:

* strings
* integers
* floats
* booleans
* other lists
* mixed data types

Example:

```python
data = ["Spoorthi", 27, True, 95.5]
```

---

# Characteristics of Lists

Lists are:

* Ordered
* Mutable
* Indexed
* Iterable

---

# List Indexing

```python
fruits = ["apple", "banana", "mango"]
```

| Item  | apple | banana | mango |
| ----- | ----- | ------ | ----- |
| Index | 0     | 1      | 2     |

Access values:

```python
print(fruits[0])
print(fruits[-1])
```

Output:

```python
apple
mango
```

---

# List Slicing

Syntax:

```python
list[start:end]
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

print(numbers[1:4])
```

Output:

```python
[2, 3, 4]
```

---

# Negative Indexing

```python
numbers[-1]
```

Returns last element.

Example:

```python
numbers = [10, 20, 30]

print(numbers[-1])
```

Output:

```python
30
```

---

# List Length

Use:

```python
len(list_name)
```

Example:

```python
numbers = [1, 2, 3]

print(len(numbers))
```

Output:

```python
3
```

---

# Lists Are Mutable

Unlike strings, lists can be modified.

Example:

```python
fruits = ["apple", "banana"]

fruits[0] = "mango"

print(fruits)
```

Output:

```python
['mango', 'banana']
```

---

# Adding Items

## append()

Adds one item at the end.

```python
fruits.append("mango")
```

---

## insert()

Adds item at specific index.

```python
fruits.insert(1, "orange")
```

---

## extend()

Adds multiple items.

```python
a = [1, 2]
b = [3, 4]

a.extend(b)
```

Result:

```python
[1, 2, 3, 4]
```

---

# Removing Items

## remove()

Removes by value.

```python
fruits.remove("banana")
```

---

## pop()

Removes by index.

```python
numbers.pop(1)
```

Returns removed value.

---

## clear()

Removes all items.

```python
numbers.clear()
```

---

# Membership Checks

Use `in`.

```python
"apple" in fruits
```

Returns:

```python
True
```

or

```python
False
```

---

# Searching

## index()

Returns position.

```python
fruits.index("banana")
```

---

## count()

Counts occurrences.

```python
numbers.count(2)
```

Example:

```python
numbers = [1, 2, 2, 3, 2]

print(numbers.count(2))
```

Output:

```python
3
```

---

# Sorting

## sort()

Sorts original list.

```python
numbers.sort()
```

Example:

```python
numbers = [4, 1, 8, 3, 2]

numbers.sort()
```

Output:

```python
[1, 2, 3, 4, 8]
```

---

## Descending Sort

```python
numbers.sort(reverse=True)
```

Output:

```python
[8, 4, 3, 2, 1]
```

---

# reverse()

Reverses current order.

```python
numbers.reverse()
```

Important:

* `sort()` orders values.
* `reverse()` only reverses current sequence.

---

# Copying Lists

## Reference Assignment

```python
a = [1, 2, 3]
b = a
```

Memory model:

```text
a ──┐
    ├──> [1, 2, 3]
b ──┘
```

Both variables reference the same list.

Changes through one variable affect the other.

Example:

```python
b.append(4)

print(a)
```

Output:

```python
[1, 2, 3, 4]
```

---

## Independent Copy

Using:

```python
b = a.copy()
```

or

```python
b = a[:]
```

Memory model:

```text
a ──> [1, 2, 3]

b ──> [1, 2, 3]
```

Separate objects.

Changes to one do not affect the other.

---

# Identity vs Equality

Reference assignment:

```python
a = [1, 2, 3]
b = a
```

```python
a is b
```

Output:

```python
True
```

```python
a == b
```

Output:

```python
True
```

---

Copy:

```python
a = [1, 2, 3]
b = a.copy()
```

```python
a is b
```

Output:

```python
False
```

```python
a == b
```

Output:

```python
True
```

Explanation:

* `is` checks object identity.
* `==` checks value equality.

---

# Nested Lists

Lists can contain other lists.

Example:

```python
matrix = [
    [1, 2],
    [3, 4]
]
```

Access elements:

```python
matrix[0][0]
```

Output:

```python
1
```

```python
matrix[1][1]
```

Output:

```python
4
```

---

# Iterating Through Lists

Using a `for` loop:

```python
animals = ["cat", "dog", "rabbit"]

for animal in animals:
    print(animal)
```

Output:

```python
cat
dog
rabbit
```

---

# List Concatenation

```python
a = [1, 2]
b = [3, 4]

print(a + b)
```

Output:

```python
[1, 2, 3, 4]
```

---

# List Repetition

```python
print([1] * 3)
```

Output:

```python
[1, 1, 1]
```

---

# Important Learnings

* Lists are ordered mutable collections.
* Lists support indexing and slicing.
* Lists can contain mixed data types.
* Lists are mutable unlike strings.
* `append()` adds one item.
* `extend()` adds multiple items.
* `insert()` adds at a specific index.
* `remove()` removes by value.
* `pop()` removes by index.
* `sort()` sorts values.
* `reverse()` reverses order.
* `copy()` creates an independent list.
* `b = a` creates a reference, not a copy.
* `is` checks identity.
* `==` checks equality.
* Nested lists support multi-dimensional data.
* `for` loops iterate through list elements.

# Lesson 5 — Tuples, Sets, and Dictionaries

## Concepts Covered

* Tuples
* Tuple indexing
* Tuple unpacking
* Tuple immutability
* Sets
* Set operations
* Membership testing
* Dictionaries
* Dictionary methods
* Dictionary loops
* Safe lookups with get()

---

# Tuples

## What Is a Tuple?

A tuple is an ordered, immutable collection.

Example:

```python
person = ("John", 25, "Engineer")
```

Characteristics:

* Ordered
* Immutable
* Indexed
* Allows duplicates

---

## Tuple Indexing

```python
person = ("John", 25, "Engineer")

print(person[0])
print(person[1])
print(person[2])
```

Output:

```text
John
25
Engineer
```

---

## Tuple Slicing

```python
numbers = (10, 20, 30, 40)

print(numbers[1:3])
```

Output:

```text
(20, 30)
```

---

## Tuple Unpacking

```python
person = ("John", 25, "Engineer")

name, age, profession = person
```

After unpacking:

```python
print(name)
print(age)
print(profession)
```

Output:

```text
John
25
Engineer
```

---

## Tuple Immutability

This causes an error:

```python
numbers = (1, 2, 3)

numbers[0] = 100
```

Output:

```text
TypeError
```

Reason:

Tuples cannot be modified after creation.

---

# Sets

## What Is a Set?

A set is an unordered collection of unique values.

Example:

```python
numbers = {1, 2, 3}
```

Characteristics:

* Unordered
* Mutable
* Unique values only
* Not indexed

---

## Duplicate Removal

```python
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
```

Output:

```text
{1, 2, 3, 4}
```

Duplicates are automatically removed.

---

## Why Sets Are Unordered

Sets do not store items by position.

This is invalid:

```python
numbers[0]
```

Output:

```text
TypeError: 'set' object is not subscriptable
```

Because sets do not support indexing.

---

## Adding Elements

```python
colors = {"red", "green", "blue"}

colors.add("yellow")
```

---

## Removing Elements

```python
colors.remove("green")
```

Safer alternative:

```python
colors.discard("green")
```

`discard()` does not raise an error if the item is absent.

---

## Membership Testing

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

Membership testing in sets is very fast.

---

## Set Operations

### Union

Combines all unique values.

```python
a | b
```

Example:

```python
{1, 2, 3, 4, 5, 6}
```

---

### Intersection

Returns common values.

```python
a & b
```

Example:

```python
{3, 4}
```

---

### Difference

Returns values present in first set but not second.

```python
a - b
```

Example:

```python
{1, 2}
```

---

# Dictionaries

## What Is a Dictionary?

A dictionary stores key-value pairs.

Example:

```python
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}
```

---

## Accessing Values

```python
student["name"]
```

Output:

```python
Alice
```

---

## Adding New Keys

```python
student["city"] = "Bangalore"
```

---

## Updating Existing Keys

```python
student["age"] = 21
```

---

## Removing Keys

```python
del student["course"]
```

---

## Dictionary Methods

### keys()

Returns all keys.

```python
student.keys()
```

---

### values()

Returns all values.

```python
student.values()
```

---

### items()

Returns key-value pairs.

```python
student.items()
```

---

## Membership Testing

Checks keys by default.

```python
"name" in student
```

Output:

```python
True
```

Example:

```python
"salary" in student
```

Output:

```python
False
```

---

## Safe Lookup with get()

Instead of:

```python
student["salary"]
```

which raises:

```text
KeyError
```

Use:

```python
student.get("salary")
```

Output:

```python
None
```

This avoids program crashes when a key does not exist.

---

## Looping Through Dictionaries

### Loop Through Keys and Values

```python
for key, value in student.items():
    print(key, value)
```

Example Output:

```text
name Alice
age 21
course Python
```

---

# Comparison of Collection Types

| Type       | Ordered | Mutable | Indexed | Duplicates |
| ---------- | ------- | ------- | ------- | ---------- |
| List       | Yes     | Yes     | Yes     | Yes        |
| Tuple      | Yes     | No      | Yes     | Yes        |
| Set        | No      | Yes     | No      | No         |
| Dictionary | Yes*    | Yes     | By Key  | Keys No    |

*Dictionaries preserve insertion order in modern Python.

---

# Important Learnings

## Tuples

* Ordered collections.
* Immutable.
* Support indexing and slicing.
* Support unpacking.

---

## Sets

* Unordered collections.
* Contain unique values only.
* Do not support indexing.
* Support union, intersection, and difference.
* Excellent for membership checks.

---

## Dictionaries

* Store key-value pairs.
* Mutable.
* Access values through keys.
* Support keys(), values(), and items().
* get() safely retrieves values without errors.
* Commonly used to represent structured data.

---

# Mental Model

### List

```python
["apple", "banana", "mango"]
```

Ordered collection with positions.

---

### Tuple

```python
("apple", "banana", "mango")
```

Ordered collection that cannot change.

---

### Set

```python
{"apple", "banana", "mango"}
```

Unique values with no positional access.

---

### Dictionary

```python
{
    "name": "Alice",
    "age": 21
}
```

Data stored as key → value pairs.

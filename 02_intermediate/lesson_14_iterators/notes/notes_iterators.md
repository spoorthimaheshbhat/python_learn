# Lesson 14 — Iterators (Discussion Notes)

## Objective

Understand how Python iterates internally and how `for` loops work behind the scenes using:

* `iter()`
* `next()`
* `StopIteration`
* Iterator objects
* Iterating through files
* Real-world iterator use cases

---

# 1. What is an Iterator?

An iterator is an object that returns values one at a time.

Example:

```python
numbers = [1,2,3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
1
2
3
```

Calling:

```python
next(iterator)
```

again raises:

```text
StopIteration
```

---

# 2. Iterable vs Iterator

Iterable:

* Can create an iterator.

Iterator:

* Produces values one-by-one.

Examples:

```python
iter([1,2,3])
→ list_iterator

iter("hello")
→ str_ascii_iterator

iter((1,2))
→ tuple_iterator

iter({1,2})
→ set_iterator

iter({"a":1})
→ dict_keyiterator
```

---

# 3. What a for loop does internally

Normal loop:

```python
for letter in "Python":
    print(letter)
```

Equivalent:

```python
iterator = iter("Python")

while True:
    try:
        letter = next(iterator)
        print(letter)

    except StopIteration:
        break
```

---

# 4. StopIteration

Signals iterator exhaustion.

Example:

```python
iterator = iter([1,2])

while True:
    try:
        print(next(iterator))

    except StopIteration:
        print("Finished")
        break
```

---

# 5. Strings are Iterables

Example:

```python
word = "Python"

iterator = iter(word)

print(next(iterator))
```

Output:

```text
P
```

---

# 6. Files Can Be Iterated

Files support iteration naturally.

Example:

```python
with open("notes.txt") as file:
    for line in file:
        print(line)
```

---

# 7. Iterating Through Notes File

Flow:

Input
→ write file
→ seek
→ read
→ iterate

Observed:

* blank input
* overwrite behavior
* line iteration

---

# 8. Nested Iterators

Example:

```python
employee = iter(next(record))
```

Iterator consuming another iterator's values.

Useful for understanding nested traversal.

---

# 9. Iterator + Error Handling

Example:

```python
except ValueError:
    print("Invalid transaction")
```

Iterator continues consuming remaining records.

---

# 10. Iterator Mental Model

```text
iter()
↓
iterator object
↓
next()
↓
next()
↓
StopIteration
```

---

# Lesson Outcomes

You learned to:

✅ Create iterators

✅ Consume iterators manually

✅ Handle StopIteration

✅ Understand for loops internally

✅ Iterate files

✅ Build iterator pipelines

✅ Add fault tolerance

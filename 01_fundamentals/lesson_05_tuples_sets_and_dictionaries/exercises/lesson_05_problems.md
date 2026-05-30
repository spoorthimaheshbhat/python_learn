# Lesson 5 — Tuples, Sets, and Dictionaries — Exercise Problems

## Exercise 1 — Tuple Creation

Create:

```python
person = ("John", 25, "Engineer")
```

Print:

* name
* age
* profession

using indexing.

---

## Exercise 2 — Tuple Unpacking

Using:

```python
person = ("John", 25, "Engineer")
```

Unpack into:

```python
name
age
profession
```

Print all variables.

---

## Exercise 3 — Tuple Immutability

Predict output BEFORE running:

```python
numbers = (1, 2, 3)

numbers[0] = 100

print(numbers)
```

Explain why.

---

## Exercise 4 — Create a Set

Create:

```python
numbers = {1, 2, 2, 3, 3, 4}
```

Print the set.

Explain the output.

---

## Exercise 5 — Set Methods

Create:

```python
colors = {"red", "green", "blue"}
```

Perform:

* add `"yellow"`
* remove `"green"`

Print final set.

---

## Exercise 6 — Membership in Sets

Using:

```python
fruits = {"apple", "banana", "mango"}
```

Check:

* `"apple"`
* `"grape"`

using `in`.

---

## Exercise 7 — Set Operations

Create:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

Print:

* union
* intersection
* difference (`a - b`)

---

## Exercise 8 — Dictionary Creation

Create:

```python
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}
```

Print:

* name
* age
* course

---

## Exercise 9 — Dictionary Update

Using the previous dictionary:

* add `"city": "Bangalore"`
* update age to `21`

Print final dictionary.

---

## Exercise 10 — Dictionary Methods

Using:

```python
student = {
    "name": "Alice",
    "age": 21,
    "course": "Python"
}
```

Print:

* all keys
* all values
* all key-value pairs

using:

```python
keys()
values()
items()
```

---

## Exercise 11 — Dictionary Membership

Check whether:

```python
"name"
```

and

```python
"salary"
```

exist in the dictionary.

---

## Exercise 12 — Safe Lookup

Using:

```python
student = {
    "name": "Alice",
    "age": 21
}
```

Print:

```python
student.get("age")
student.get("salary")
```

Explain the difference.

---

## Exercise 13 — Tuple vs List

Predict output BEFORE running:

```python
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]

my_list[0] = 100
my_tuple[0] = 100

print(my_list)
print(my_tuple)
```

Explain why one works and the other fails.

---

## Exercise 14 — Dictionary Loop

Using:

```python
person = {
    "name": "John",
    "age": 25,
    "city": "Mumbai"
}
```

Print all keys and values using a loop.

---

## Exercise 15 — Mini Challenge

Create a dictionary representing yourself:

```python
profile = {
    ...
}
```

Include at least:

* name
* age
* favorite language
* city
* learning_python

Print all key-value pairs using a loop.

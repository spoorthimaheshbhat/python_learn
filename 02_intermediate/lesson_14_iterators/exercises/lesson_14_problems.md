# Lesson 14 — Problems

---

## ex_1 — Iterate Through List Manually

Print each color using:

* `iter()`
* `next()`

Input:

```python
colors=["red","green","blue"]
```

Expected:

```text
red
green
blue
```

---

## ex_2 — Recreate for Loop

Print:

```text
Python
```

twice:

1. normal loop
2. manual iterator

---

## ex_3 — StopIteration

Input:

```python
[1,2]
```

Print:

```text
1
2
End reached
```

---

## ex_4 — Notes File Iterator

Requirements:

* accept multiline input
* save file
* reopen
* iterate contents

Extra cases:

* blank input
* overwrite behavior

---

## ex_5 — Iterator Types

Predict:

```python
type(iter([1,2,3]))
type(iter("hello"))
```

Explain output.

---

# Use Case 1 — Attendance Stream Reader

Requirements:

* read attendance file
* create tuples
* iterate records
* display employee status

Output:

```text
John, Present
Alice, Absent
...
```

---

# Use Case 2 — Transaction Processor

Requirements:

* read transactions
* positive → processed
* negative → failed

Enhancement:

Handle invalid values.

Example:

```text
Invalid transaction
```

Continue processing.

Extra cases:

```text
"filed"
"xyz"
```

---

# Use Case 3 — Countdown Iterator

Requirements:

Display:

```text
3
2
1
Done
```

Use manual iteration.

---

# Optional Challenges

Challenge 1:
Build iterator for CSV rows.

Challenge 2:
Create iterator over dictionary values.

Challenge 3:
Read file line-by-line using `next()`.

Challenge 4:
Build iterator over employee attendance summary.

Challenge 5:
Create custom countdown iterator (preview for generators).

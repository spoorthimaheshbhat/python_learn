# Lesson 7 - Loops - Exercises

## Exercise 1 - Print Numbers

Using a for loop, print:

```
1
2
3
...
10
```

---

## Exercise 2 - Sum of Numbers

Calculate:

```
1 + 2 + 3 + ... + 100
```

using a loop.

Do not use:

```python
sum()
```

---

## Exercise 3 - Even Numbers

Print all even numbers from:

```
1 to 50
```

---

## Exercise 4 - Multiplication Table

Take a number from the user.

Example:

Input:

```
5
```

Output:

```
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

---

## Exercise 5 - Count Vowels

Take a word as input.

Count how many vowels it contains.

Example:

Input:

```
programming
```

Output:

```
3
```

Bonus:
Handle uppercase letters correctly.

---

## Exercise 6 - Find a Number

Given:

```python
numbers = [10, 20, 30, 40, 50]
```

Search for:

```python
30
```

Use:

```python
break
```

Print:

```
Found
```

or

```
Not Found
```

---

## Exercise 7 - Login Attempts

Correct password:

```python
python123
```

Allow only 3 attempts.

If password is correct:

```
Access Granted
```

Otherwise after 3 failures:

```
Account Locked
```

Use:

- while loop
- counter variable

---

## Exercise 8 - Skip Multiples of 3

Print numbers:

```
1 to 20
```

but skip:

```
3
6
9
12
15
18
```

Use:

```python
continue
```

---

## Exercise 9 - Character Frequency

Given:

```python
word = "mississippi"
```

Count occurrences of:

```python
"s"
```

Do not use:

```python
count()
```

Use a loop.

Expected output:

```
4
```

---

## Exercise 10 - Nested Loops

Using nested loops, print:

```
*
**
***
****
*****
```

---

## Exercise 11 - Reverse String Without Slicing

Given:

```python
word = "Python"
```

Output:

```
nohtyP
```

Constraint:

Do not use:

```python
[::-1]
```

Use loops only.

---

## Exercise 12 - Prime Number Checker

Take a number from the user.

Determine whether it is:

```
Prime
```

or

```
Not Prime
```

Examples:

```
2 -> Prime
3 -> Prime
4 -> Not Prime
13 -> Prime
15 -> Not Prime
```

Bonus:

Handle:

```
0
1
negative numbers
```

appropriately.

---

## Exercise 13 - Prediction Challenge

Predict output before running:

```python
for i in range(5):
    if i == 2:
        continue

    if i == 4:
        break

    print(i)
```

Explain carefully.

---

## Exercise 14 - Count Occurrences

Given:

```python
numbers = [4, 7, 2, 7, 9, 7, 1]
```

Without using:

```python
count()
```

Determine how many times:

```python
7
```

appears.

Expected output:

```
3
```
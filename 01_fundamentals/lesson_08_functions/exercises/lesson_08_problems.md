# Lesson 8 - Functions - Exercises

## Exercise 0 - Calculator Using Functions

Create a calculator program using functions.

Requirements:
- Function to input two numbers.
- Function to perform:
  - add
  - subtract
  - multiply
  - divide
- Return results.
- Handle:
  - invalid actions
  - division by zero

---

## Exercise 1 - Hello Function

Create a function:

```python
say_hello()
```

Print:

```text
Hello Python
```

Call the function three times.

---

## Exercise 2 - Greeting Function

Create:

```python
greet(name)
```

Print:

```text
Hello <name>
```

Call it with different names.

---

## Exercise 3 - Addition Function

Create:

```python
add(a, b)
```

Return the sum.

Store the result in a variable and print it.

---

## Exercise 4 - Even Number Checker

Create:

```python
is_even(number)
```

Return:
- `True` if even
- `False` if odd

Print a suitable message.

---

## Exercise 5 - Largest Number

Create:

```python
largest(a, b)
```

Return:
- larger number
- `None` if both are equal

Handle all cases.

---

## Exercise 6 - Grade Calculator

Create:

```python
calculate_grade(marks)
```

Rules:

| Marks | Grade |
|---------|---------|
| 90+ | A |
| 80-89 | B |
| 70-79 | C |
| 60-69 | D |
| Below 60 | F |

Invalid marks:
- less than 0
- greater than 100

Return:
- grade
- `None` for invalid marks

---

## Exercise 7 - Count Vowels

Create:

```python
count_vowels(word)
```

Return the number of vowels.

Examples:

```text
AEIOU -> 5
program -> 2
```

---

## Exercise 8 - Multiplication Table Function

Create:

```python
print_table(number)
```

Display the multiplication table from:

```text
1 to 10
```

---

## Exercise 9 - Login Validator

Create:

```python
validate_login(username, password)
```

Valid credentials:

```text
username = admin
password = python123
```

Return:
- True
- False

Display login result.

---

## Exercise 10 - Multiple Return Values

Create:

```python
calculate(a, b)
```

Return:

- sum
- difference
- product

Receive all returned values separately.

---

## Exercise 11 - Predict Output

```python
x = 100

def test():
    x = 50
    print(x)

test()
print(x)
```

Predict output and explain.

---

## Exercise 12 - Default Parameters

Create:

```python
greet(name="Guest")
```

Call:

```python
greet("Sam")
greet()
```

Observe output.

---

## Exercise 13 - Keyword Arguments

Create:

```python
introduce(name, age, city)
```

Call the function using keyword arguments in a different order.

Example:

```python
introduce(
    city="London",
    age=12,
    name="Harry"
)
```

---

## Exercise 14 - Prime Number Function

Create:

```python
is_prime(number)
```

Return:

- True if prime
- False if composite
- None if number is 0 or 1

Display appropriate messages.

---

## Exercise 15 - Number Analysis Function

Create:

```python
analyze_numbers(numbers)
```

Return:

- total sum
- average
- largest number
- smallest number

Example input:

```python
[10, 20, 30, 40, 50]
```

Display all returned values.

---

## Bonus Challenge

Improve the calculator project by:

- Using functions effectively
- Returning values instead of printing inside functions
- Handling division by zero
- Avoiding duplicated logic
- Separating input collection from calculation logic

This project serves as a practical application of all major function concepts learned in Lesson 8.
def analyze_numbers(numbers):
    summation = 0
    for num in numbers:
        summation += num
    return summation, summation / len(numbers), max(numbers), min(numbers)

list_num = [10, 20, 30, 40, 50]

total, avg, largest, smallest = analyze_numbers(list_num)

print("Total sum is:", total)
print("Average is:", avg)
print("Largest number is:", largest)
print("Smallest number is:", smallest)

# given:
employees = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 75000},
    {"name": "Charlie", "salary": 45000}
]


sorted_employees = sorted(employees, key=lambda emp: emp["salary"])

print(sorted_employees)
# given:

employees = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 75000},
    {"name": "Charlie", "salary": 40000},
    {"name": "David", "salary": 90000}
]

print([employee["name"] for employee in employees if employee["salary"] > 60000])
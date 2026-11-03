#q13

records = [
    ('Neha', 'Pen', 120),
    ('Neha', 'Book', 80),
    ('Neha', 'Bag', 45),
    ('Imran', 'Pen', 90),
    ('Imran', 'Book', 60),
    ('Imran', 'Bag', 30),
    ('Dev', 'Pen', 150),
    ('Dev', 'Book', 110),
    ('Dev', 'Bag', 95),
    ('Sana', 'Pen', 70),
    ('Sana', 'Book', 85),
    ('Sana', 'Bag', 52),
]

# 1. 
products = set()
for who, product, units in records:
    products.add(product)

print(sorted(products))

# 2. 
scores = {}

for who, product, units in records:
    if who not in scores:
        scores[who] = []
    scores[who].append(units)

# 3. 
averages = {}

for who, marks in scores.items():
    avg = sum(marks) / len(marks)
    averages[who] = avg

    if avg >= 90:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    else:
        grade = "C"

    print(f"{who:<8} avg={avg:.1f} grade={grade}")

# 4. Top performer and overall average
top_employee = max(averages, key=averages.get)
overall_avg = sum(averages.values()) / len(averages)

print(f"Top: {top_employee} | Overall average: {overall_avg:.2f}")

# 5. 
above_overall = [who for who, avg in averages.items() if avg > overall_avg]
print("Above overall:", above_overall)

# 6.
all_units = [units for _, _, units in records]
extremes = (min(all_units), max(all_units))

print(extremes, type(extremes).__name__)

# 7. Comment
# Set removes duplicate products, dictionary maps employees to scores,
# list stores multiple unit values per employee, and tuple stores fixed records/extremes.
#q11
nums = [3, 8, 3, 1, 8, 5, 5, 5]

# 1
s = set(nums)
print(sorted(s), len(nums), len(s))

# 2
s.add(12)
s.discard(77)   # no error if not found
s.remove(8)
print(sorted(s))

# 3
try:
    s.remove(1000)
except KeyError:
    print("KeyError")

# 4
s1 = {2, 4, 6, 8, 10}
s2 = {8, 10, 12, 6}

print(sorted(s1 | s2), sorted(s1 & s2))
print(sorted(s1 - s2), sorted(s2 - s1), sorted(s1 ^ s2))

# 5
print(type({}).__name__, type(set()).__name__)

# 6
print(5 in s, 5 not in s1)

# 7
try:
    bad_set = {[1, 2], [3, 4]}
except TypeError:
    print("TypeError")

#q12


d = {
    'title': 'Laptop',
    'price': 55000,
    'brand': 'Acer',
    'tags': ['office', 'student', 'light'],
    'stock': {'shop': 'Pune', 'units': 14},
}


print(d["title"], d.get("warranty"), d.get("warranty", "No warranty"))


d["price"] = 52000
d["color"] = "Silver"
print(d["price"], len(d))


removed = d.pop("brand")
print(removed, d.pop("zzz", "none"))

del d["tags"]
print(list(d.keys()))


print(d["stock"]["shop"])


print("title" in d, "Laptop" in d, "Laptop" in d.values())


for key, value in d.items():
    print(f"{key} -> {value}")


try:
    print(d["rating"])
except KeyError:
    print("KeyError")


dup = {"title": "first", "x": 1, "title": "second"}
print(dup)
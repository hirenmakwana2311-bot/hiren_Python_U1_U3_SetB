#q9

items = ['Delhi', 'Pune', 'Surat', 'Jaipur']

items.append("Indore")
items.extend(['Nagpur', 'Bhopal'])
items.insert(2, "Kochi")
items.remove("Surat")

last = items.pop()
items[0] = "Mumbai"

print(items)
print(last, len(items))

list1 = ['x', 'y', 'z']
list1.append(['p', 'q'])

list2 = ['x', 'y', 'z']
list2.extend(['p', 'q'])

print(list1, len(list1))
print(list2, len(list2))

try:
    print(items[50])
except IndexError:
    print("IndexError")

try:
    items.remove("Chennai")
except ValueError:
    print("ValueError")

try:
    [].pop()
except IndexError:
    print("IndexError")

#q10

t = (5, 15, 15, 25, 35)

# 1
print(t[0], t[-1], t[1:3])

# 2
print(t.count(15), t.index(35))

# 3
x = (9)
y = (9,)
print(type(x).__name__, type(y).__name__)

# 4
for stmt in [
    lambda: exec('t[0] = "orange"'),
    lambda: t.append(99),
    lambda: t.index(1000)
]:
    try:
        stmt()
    except Exception as e:
        print(type(e).__name__)

# 5
data = ([10, 20], 'world')
data[0].append(30)
print(data)

# 6
new_t = ("orange",) + t[1:]
print(new_t)
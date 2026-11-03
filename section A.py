# q1
print("Learning", "Python", "Basics", sep="|", end="!\n")

name, city, year = "Meena", "Rajkot", 2027
print(f"Name:\t{name}\nCity:\t{city}")


print(f'She said "It\'s {year}"')

a, b = 7, 3
a, b = b, a
print(a, b)



#Q2
item = input("Enter item name: ")
price = float(input("Enter price: "))
raw_qty = input("Enter quantity: ")


print(type(raw_qty))
quantity = int(raw_qty)
print(type(quantity))


total = price * quantity
print(f"Total for {item}: {total:.2f}")


try:
    int("25.5")
except ValueError:
    print("ValueError")

try:
    "25" + 5
except TypeError:
    print("TypeError")


print(int(float("25.5")), int(-9.9), -9.9 // 1)
#q6
word = "Collections"

print(word[0], word[-1], len(word))

print(word[:3], word[3:], word[::-1], word[::2])

try:
    word[0] = "K"
except TypeError:
    print("TypeError")

try:
    print(word[40])
except IndexError:
    print("IndexError")

new_word = "K" + word[1:]
print(new_word)

#q7

raw = " sNEha pAtel , Rajkot , sneha@store.in "

clean = raw.strip()
parts = [part.strip() for part in clean.split(",")]
print(parts)

name, city, email = parts
print(name.title(), city.upper(), email.lower(), sep=" | ")


print(email.endswith(".in"), email.startswith("sneha"),
      email.find("@"), email.find("#"))


try:
    email.index("#")
except ValueError:
    print("ValueError")

print(city.replace("o", "0"))

print(raw.lstrip() == clean, raw.rstrip() == clean)

#q8

customer = "Neha"
item = "Water bottle"
price = 350
qty = 4
disc = 0.075

total = price * qty * (1 - disc)

print(f"""
------ RECEIPT ------
Customer: {customer}
Item: {item}
Price: Rs. {price}
Quantity: {qty}
Discount: {disc:.1%}
Total: Rs. {total:.2f}
---------------------
""")

print("{} bought {} item(s)".format(customer, qty))

print("{name} paid {amount:.1f}".format(name=customer, amount=total))

print("%s bought %d item(s) for %.2f" % (customer, qty, total))
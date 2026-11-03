#q4

a, b = 23, 6
print(a // b, a % b, -a // b, -a % b)

print((-a // b) * b + (-a % b) == -a)

print((8 - 2) * 3 ** 2 % 7, 3 ** 2 ** 2, -9 // 4)

print(type(10 / 2).__name__, type(10 // 2).__name__)

price = 480
quantity = 5
tax_rate = 12

subtotal = price * quantity
tax = subtotal * tax_rate / 100
total = subtotal + tax

print(f"Subtotal: {subtotal}  Tax: {tax:.2f}  Total: {total:.2f}")  

#Q5
 
age = 16
has_id = True
has_guardian = True

print(18 <= age <= 60)


 
can_enter = (age >= 18 and has_id) or has_guardian
print(can_enter)

print("Hello" and "World", "" or "Guest", not 10)

user = ""
print(user or "Guest")

score = 20

score -= 4
score **= 2
score %= 50
score /= 5

print(score)


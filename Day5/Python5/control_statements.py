'''
product = ["Bread", "Butter", "Milk","Sugar","Salt"]
for item in product:
    print(item)
'''
'''
products_dict = {"Bread": 30, "Butter":49, "Milk": 20,"Sugar":29,"Salt":25}
for item in products_dict:
    print("product name: ",item)
    print("product value: " ,products_dict[item])
    print("Buy Now, Add to Cart")
    print("Add to fac")
    print("-----------------")
'''

s = 'Python Programming'
for i in s:
    print(i,end="❤")

for i in range(5,96,5):
    print(i)
    


n = int(input("Enter your number: "))
for i in range(1,21):
    print(f"{n} * {i} = {n*i}")

for i in range(10):
    if i == 15:
        break
    print(i)
else:
    print("End of numbers")

pin = 1234
for i in range(5):
    if user_pin == pin:
        print("Login successful")
        break
    else:
        print("Invalid password, try  again")
else:
    print("you have reached the max attempts, try again after 5 mins")
user_pin = int(input("Enter the number: "))





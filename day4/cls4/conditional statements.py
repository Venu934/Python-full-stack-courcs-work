'''min_balence = 5000
curent_balance = 2000
if curent_balance  <  5000:
    print("sent messege and cut some amount") '''

'''data = ('user@gmail.com,user@1234')
mail = input("enter your mail: ")
pasword = input("Enter your password: ")
if data == (mail,pasword):
    print("Login Successful")
else:
    print("Invalid Login")'''
'''
fruits = ['mango', 'apple', 'papaya', 'pine apple']
search_item = input("search fruits: ")
if search_item in fruits:
    print("buy now")
else:
    print("fruit is not there")

'''
'''
time = int(input("Enter the time : "))
          
if 0 <= time <= 6:
    print("Bus\Bus1\Bus3\Bus4")
elif 7 <= time <= 12:
    print("Bus1\nBus\Bus4")
elif 13 <= time <= 18:
    print("Bus2\nBus\Bus6")
else:
    print("Enter the time in the given range")
'''
print("Welcome to UBER, book your ride")
print("1.Bike")
print("2.Auto")
print("3.car")

choice = int(input("choice the option: "))
if choice == 1:
    print(" you have booked the bike successfull .\n Driver is on the way.\n Wear the helmet")
elif choice == 2:
    print("welcome to the uber. \n you have booked a auto successfully")
elif choice == 3:
    print("Wlecome to uber. you have selected cab move to road")


---

##5 Programs Using if-elif-else
# 1. Grade classification
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")

# 2. Temperature check
temp = 30
if temp > 35:
    print("Hot day")
elif temp > 20:
    print("Pleasant day")
else:
    print("Cold day")

# 3. Traffic light system
signal = "yellow"
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Get ready")
else:
    print("Go")

# 4. Number comparison
x = 15
y = 20
if x > y:
    print("x is greater")
elif x < y:
    print("y is greater")
else:
    print("Both are equal")

# 5. Check type of triangle
a, b, c = 5, 5, 5
if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

# 1. Check eligibility for voting
age = 20
citizen = True
if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Too young to vote")

# 2. Login system
username = "admin"
password = "1234"
if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")

# 3. Check number sign and parity
num = -4
if num >= 0:
    if num % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
else:
    if num % 2 == 0:
        print("Negative even")
    else:
        print("Negative odd")

# 4. Scholarship eligibility
marks = 92
income = 25000
if marks >= 90:
    if income < 30000:
        print("Eligible for scholarship")
    else:
        print("Not eligible due to income")
else:
    print("Not eligible due to marks")

# 5. Nested menu selection
menu = "food"
choice = "pizza"
if menu == "food":
    if choice == "pizza":
        print("You selected pizza")
    else:
        print("Other food item")
else:
    if choice == "coffee":
        print("You selected coffee")
    else:
        print("Other drink")


    


    

num = int(input("Enter the number: "))
fact = 1
if num < 0:
    print("factorial not exist")
elif num == 0:
    print("Factorial 0 is 1")
else:
    for i in range(1,num+1):
        fact = fact* i
    print(f"fact is{fact}")

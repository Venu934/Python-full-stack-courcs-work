'''
i = 20
while i <= 30:
    if i == 25:
        pass
    print(i)
    i+=1

bullets = int(input("Enter the number of bullets" ))
while bullets > 0:
    print(f"{bullets} bullets are left , You need to shoot some thing: ")
    bullets -= 1
else:
    print("Game over")
'''
'''
winning_point = 24
moves = int(input("Enter the number: "))
while moves > 0:
    if moves == winning_point:
        print("You won the game")
        break
    print(f"{moves} moves left")
    moves -=1
else:
    print("No more moves left")
'''
    
data = {}
no_std = int(input("enter the no of student: "))
while no_std > 0:
    name = input("enter the name: ")
    data[name] = False
    no_std -= 1

print(data)
for name in data:
    print(name)
    status = int(input(f"Enter the name {name} status (0 - Absent, 1 - present): "))
    data[name] = bool(status)

print(data)


    

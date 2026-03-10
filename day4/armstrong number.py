num = int(input("Enter the number: "))
temp = num

digits = len(str(num))

sums = 0
while temp > 0:
    temp = num % 10
    sums += temp**digits
    temp //= 10

if num == sums:
    print("it is an armstrong number: ")
else:
    print("it is not an armstrong number: ")
    

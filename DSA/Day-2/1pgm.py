'''
def count_even(n):
    count = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            count += 1
    return count

def main():
    n = int(input("Enter the number: "))
    print("Even count: ",count_even(n))

main()

'''

def count_digit(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

def main():
    num = int(input("Enter number : "))
    print("Digits count: ", count_digit(num))
main()
























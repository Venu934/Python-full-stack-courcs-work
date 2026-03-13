def check_num(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
def main():
    num = int(input("Enter the number: "))
    check_num(num)
main()

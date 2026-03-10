def caliculate_sum(n):
    total = 0
    for i in range(1,n+1):
        total += i
    return total
def main():
    n = int(input("Enter the number: "))
    print("Sum",caliculate_sum(n))
main()


def even_nos(n):
    count = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            print(i)
            count += 1
    return count
def main():
    n = int(input("Enter the number: "))
    print("Even numbers", even_nos(n))
main()

#taking student name give it to output
def std_name(name):
    return name
def main():
    name = input("Enter the name: ")
    print("student name : ", std_name(name))
main()

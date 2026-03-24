'''
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def divide(a, b):
    return a / b

def modulus(a, b):
    return a % b

def multiply(a, b):
    return a * b
exp = input()
if '+' in exp:
    a,b = exp.split('+')
    print(add(int(a),int(b)))
elif '-' in exp:
    a,b = exp.split('+')
    print(sub(int(a), int(b)))
elif '*' in exp:
    a,b = exp.split('*')
    print(multiply(int(a), int(b)))
elif '/' in exp:
    a,b = exp.split('/')
    print(divide(int(a), int(b)))




a = int(input("Enter first number: "))
b = int(input("Enter second number: ")) '''





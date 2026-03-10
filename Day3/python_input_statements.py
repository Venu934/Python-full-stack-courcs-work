Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
num = list(map(int, input("Enter the numbers: ").split()))
Enter the numbers: 1,2,3,4,5,6
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    num = list(map(int, input("Enter the numbers: ").split()))
ValueError: invalid literal for int() with base 10: '1,2,3,4,5,6'
num = list(map(int, input("Enter the numbers: ").split()))
Enter the numbers: 1 2 3 4 5 6 7
num
[1, 2, 3, 4, 5, 6, 7]
num = tuple(map(int, input("Enter the numbers: ").split()))
Enter the numbers: 1 2 3 4 5 6 7
num
(1, 2, 3, 4, 5, 6, 7)
names = set(map(int, input("Enter the numbers: ").split()))
Enter the numbers: 3 4 5 6 7
d = eval(input("Enter the input: "))
Enter the input: {1:2,2:3}
d
{1: 2, 2: 3}
a,b,c =1,2,3
a
1
b
2
c
3
a=b=c =10
a
10
b
10
c
10
'anil teja'
'anil teja'
age = int(input("Enter the age of age teja: "))
Enter the age of age teja: 56
age
56
type(age)
<class 'int'>
price = input("Enter the price : ")
Enter the price : 44.3
price
'44.3'
type(price)
<class 'str'>
'venu teja karthik'
'venu teja karthik'
a,b,c = map(int, input("Enter the number: ").split())
Enter the number: 1 2 3
a
1
b
2
>>> c
3
>>> dic = eval("Enter the key value pairs: ")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dic = eval("Enter the key value pairs: ")
  File "<string>", line 1
    Enter the key value pairs: 
          ^^^
SyntaxError: invalid syntax
>>> dic = eval(input("Enter the key value pairs :"))
Enter the key value pairs :{1:2,2:3,3:4}
>>> dic
{1: 2, 2: 3, 3: 4}
>>> flt = list(map(float, input("Enter the float numer: ").split()))
Enter the float numer: 2.3 3.4 5.6 7.8
>>> flt
[2.3, 3.4, 5.6, 7.8]
>>> a = 10
>>> b = 20
>>> a+b
30
>>> a-b
-10
>>> b % a
0
>>> a**2
100
>>> a//b
0

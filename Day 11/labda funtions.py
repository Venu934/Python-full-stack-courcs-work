'''wish = lambda name:f'Hello {name}, welcome to python'
print(wish('venu'))
'''
'''
add = lambda a,b,c: (a+b+c)/3
print(add(3,4,5))

names = ['venu','sanjay']
upper = list(map(lambda x: x.upper(), names))

    

iseven1 = lambda n: "Even" if n%2 == 0 else "Odd"
print(iseven1(3))
'''
'''
isgreat = lambda a,b: "a greater" if a > b else "b greater"
print(isgreat(4,2))


vov = 'aeiouAEIOU'
isvowelcon = lambda a,b: "a greater" if a > b else "b greater"
print(isgreat(4,2))
''''''
l = ['venu','ramya','prasanna','anil']
res = list(map(lambda i:i.title(), l))
print(res)
num = [10,20,30,40,60]
'''
'''
l = ['venu','ramya','prasanna','anil']
res = list(map(lambda i:f'${i}', num))
print(res)
'''
num = [10,20,30,40,60,70,80,90,100]


#res = list(filter(lambda i:i%3==0, num))
'''
res = list(filter(lambda x:x%1==0, num))
print(res)
'''
'''
res = list(filter(lambda i:i>60, num))
print(res)
'''
'''
avl = {'laptop':True, 'iphon':True,'mouse':False,'charges':False}
avls = list(filter(lambda i:avl[i], avl))
print(avls)
'''
'''
l = [1,2,3,4,5,6,7,8,9,0,7,3,4,52,34]
res = list(filter(lambda i:i%2==0 and i!=0, l))
print(res)
'''
from functools import reduce
'''
l = [1,2,3,4,5,6,7,8,9,7,3,4,52,34]
res = reduce(lambda a,b:a*b, l)
print(res)
'''
'''
l = ['python','java','c++','c','html','reactjs']
res = reduce(lambda a,b:a+' ' +b, l)
print(res)
'''
data = {
    'apple':30,
    'orange':25,
    'pianaple':45,
    'graps':23
    }
print(dict(sorted(data.items())))
print(dict(sorted(data.items(),key=lambda i:i[1])))



    









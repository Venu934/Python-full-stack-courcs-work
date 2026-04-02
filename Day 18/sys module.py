
#import collections
#import random
#import math 
#import platform 
#import sys


'''
print(sys.argv)
print(sys.path)
print(sys.version)
print('start')
sys.exit()
print('end')
'''
'''
print(platform.system())
print(platform.release())
print(platform.processor())
'''
'''
print(math.pi)
print(math.e)
print(math.sqrt(16))
print(math.pow(3,4))
print(math.ceil(12.0000001))
print(math.floor(12.99999))
print(round(12.55))
print(abs(-12))
print(math.fabs(-12))
print(math.factorial(5))
print(math.gcd(2,4))
print(math.log(2,2))
print(math.sin(30))
print(math.tan(30))
print(math.cos(30))
print(math.degrees(30))
print(math.radians(30))
'''
'''
l = [1,2,3,4,5,6,7]
random.shuffle(l)
print(l)
'''
'''
s = 'python programming'
l = [1,2,3,4,5,2,1,8,9]
r = ' this is that that is split'.split()
res = collections.Counter(s)
res1 = collections.Counter(l)
res2 = collections.Counter(r)
print(res)
print(res1)
print(res2)



rest = {}
for i in s:
    if i in rest:
        rest[i] += 1
    else:
        rest[i] = 1
print(rest)

'''
'''
q = collections.deque([])
q.appendleft(20)
q.appendleft(30)
q.appendleft(60)
q.appendleft(70)
q.appendleft(90)
q.pop()
q.pop()
q.pop()
q.append(10)
q.append(40)
print(q)
'''

from itertools import combinations, permutations

s = 'abc'
print(list(combinations(s,2)))
print(list(permutations(s,3)))
      








Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = [1,2,3]
b = [4,5,6]
a
[1, 2, 3]






a+b
[1, 2, 3, 4, 5, 6]
a*b
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'list'
a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
names = 'venu', 'gopal', 'swamy'
names
('venu', 'gopal', 'swamy')
names = ['venu', 'gopal', 'swamy']
names
['venu', 'gopal', 'swamy']
>>> names[2]
'swamy'
>>> names[-1]
'swamy'
>>> names[:3]
['venu', 'gopal', 'swamy']
>>> 'venu' in names
True
>>> a,b,c = names
>>> a
'venu'
>>> b
'gopal'
>>> c
'swamy'
>>> 'venu' not in names
False
>>> 'fuck' meaning
SyntaxError: invalid syntax
>>> names.append('teja')
>>> names
['venu', 'gopal', 'swamy', 'teja']
>>> names.insert(3,'saran')
>>> names
['venu', 'gopal', 'swamy', 'saran', 'teja']
>>> id(names)
2383667017024
>>> names.pop(2)
'swamy'
>>> names
['venu', 'gopal', 'saran', 'teja']

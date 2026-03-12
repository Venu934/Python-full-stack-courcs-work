Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: C:/Users/konda/OneDrive/Desktop/python fullstack CW/Day 6/whileloops.py
enter the no of student: 5
enter the name: a
enter the name: b
enter the name: c
enter the name: d
enter the name: e
{'a': False, 'b': False, 'c': False, 'd': False, 'e': False}
a
Enter the name a status (0 - Absent, 1 - present): 1
b
Enter the name b status (0 - Absent, 1 - present): 1
c
Enter the name c status (0 - Absent, 1 - present): 0
d
Enter the name d status (0 - Absent, 1 - present): 0
e
Enter the name e status (0 - Absent, 1 - present): 0
{'a': True, 'b': True, 'c': False, 'd': False, 'e': False}
s ='Python'
s
'Python'
s+ 'lang'
'Pythonlang'
>>> s*2
'PythonPython'
>>> name = 'venu teja saran ramesh saadhubai'
>>> name[3]
'u'
>>> names = 'venu teja saran ramesh saadhubai'
>>> nam = {'venu','teja','saran']
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> nam = ['venu','teja','saran']
>>> nam
['venu', 'teja', 'saran']
>>> nam[1]
'teja'
>>> nam[0]
'venu'
>>> s.center(50,'=')
'======================Python======================'
>>> s.ljust(30,'-')
'Python------------------------'
>>> S = '                venu           '
>>> S.stripe(S)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    S.stripe(S)
AttributeError: 'str' object has no attribute 'stripe'. Did you mean: 'strip'?
>>> S.strip()
'venu'
>>> S.rstrip()
'                venu'
>>> S.lstrip()
'venu           '

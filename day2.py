Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> len(keyword.kwlist)
36
>>> 4/2
2.0
>>> 4//2
2
>>> #it is floor Division
>>> not(6<7)and((4<8)or(6<5))
False
>>> not(6>7)and((4<8)or(6<5))
True
>>> 4<<2
16
>>> 4<<4
64
>>> 4>>2
1
>>> 16>>3
2
>>> help(id)
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.
    
    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

>>> m=10
>>> n=20
>>> p=20
>>> id(p)
2588284775312
>>> id(n)
2588284775312
>>> id(m)
2588284774992
>>> cls
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> cls()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    cls()
NameError: name 'cls' is not defined
>>> s='Hello this is python string'
>>> 
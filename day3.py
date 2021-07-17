Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> b=[5,6,7,[5,7,[['Go'],'Nice',9]]]
>>> b
[5, 6, 7, [5, 7, [['Go'], 'Nice', 9]]]
>>> len(b)
4
>>> b+=[99]
>>> b
[5, 6, 7, [5, 7, [['Go'], 'Nice', 9]], 99]
>>> b+=['h1',70]
>>> b
[5, 6, 7, [5, 7, [['Go'], 'Nice', 9]], 99, 'h1', 70]
>>> b+='good'
>>> b
[5, 6, 7, [5, 7, [['Go'], 'Nice', 9]], 99, 'h1', 70, 'g', 'o', 'o', 'd']
>>> b.count(7)
1
>>> b.count(o)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    b.count(o)
NameError: name 'o' is not defined
>>> b.count('o')
2
>>> 'helllo '.isalpha()
False
>>> 'a'.upper()
'A'
>>> b.sort()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    b.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
>>> s='hi its puthon here'
>>> s.split()
['hi', 'its', 'puthon', 'here']
>>> ' '.join(s.split()[::-1])
'here puthon its hi'
>>> a=30
>>> b=40
>>> k= 'when we add {} and {} together,we get {}'.format(a,b,a+b)
>>> k
'when we add 30 and 40 together,we get 70'
>>> print(k)
when we add 30 and 40 together,we get 70
>>> help(k)
No Python documentation found for 'when we add 30 and 40 together,we get 70'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help(k.isalnum)
Help on built-in function isalnum:

isalnum() method of builtins.str instance
    Return True if the string is an alpha-numeric string, False otherwise.
    
    A string is alpha-numeric if all characters in the string are alpha-numeric and
    there is at least one character in the string.

>>> d={'price':[56,50,54],'brand':['A','B','K']}
>>> d
{'price': [56, 50, 54], 'brand': ['A', 'B', 'K']}
>>> d.['brand']='company'
SyntaxError: invalid syntax
>>> d.keys()
dict_keys(['price', 'brand'])
>>> d.keys(1)=['company']
SyntaxError: cannot assign to function call
>>> d.keys()[1]['company']
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    d.keys()[1]['company']
TypeError: 'dict_keys' object is not subscriptable
>>> d.keys()[1]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d.keys()[1]
TypeError: 'dict_keys' object is not subscriptable
>>> d.keys()[0]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    d.keys()[0]
TypeError: 'dict_keys' object is not subscriptable
>>> d.keys()
dict_keys(['price', 'brand'])
>>> list(d.keys())[1]
'brand'
>>> d['brand']=d['company']
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    d['brand']=d['company']
KeyError: 'company'
>>> d.update['brand']=['company']
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    d.update['brand']=['company']
TypeError: 'builtin_function_or_method' object does not support item assignment
>>> d['company']=d['brand']
>>> del d['brand']
>>> d
{'price': [56, 50, 54], 'company': ['A', 'B', 'K']}
>>> d2={'a':45,666:'wow'}
>>> {**d,**d2}
{'price': [56, 50, 54], 'company': ['A', 'B', 'K'], 'a': 45, 666: 'wow'}
>>> 
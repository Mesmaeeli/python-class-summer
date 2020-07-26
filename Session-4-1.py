
>>> l1 = [5,4,7,9]
>>> for sub in l1:
	print(sub)

	
5
4
7
9
>>> sin(90)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    sin(90)
NameError: name 'sin' is not defined
>>> import math
>>> import mathrdf
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    import mathrdf
ModuleNotFoundError: No module named 'mathrdf'
>>> sin(90)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    sin(90)
NameError: name 'sin' is not defined
>>> math.sin(90)
0.8939966636005579
>>> math.pi
3.141592653589793
>>> import math as mt
>>> mt.sin(90)
0.8939966636005579
>>> 
=============================== RESTART: Shell ===============================
>>> from math import sin
>>> sin(90)
0.8939966636005579
>>> from math import pi
>>> pi
3.141592653589793
>>> 
=============================== RESTART: Shell ===============================
>>> from math import sin,pi ,cos
>>> sin(90)
0.8939966636005579
>>> cos(90)
-0.4480736161291701
>>> pi
3.141592653589793
>>> from math import *
>>> acos(90)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    acos(90)
ValueError: math domain error
>>> acos(0.5)
1.0471975511965979
>>> 
=============================== RESTART: Shell ===============================
>>> import m1
>>> import m2
>>> m1.func(3)
9
>>> m2.func(4)
64
>>> 
=============================== RESTART: Shell ===============================
>>> from m1 import *
>>> from m2 import *
>>> func(2)
8
>>> def function1():
	print('salam')

	
>>> function1()
salam
>>> def function1():
	""" in tebe vorudi nemigire
komak mikone ke ebarat salam chap beshe"""
	print('salam')

	
>>> function1()
salam
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s4.py ==
>>> function1()
salam
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s4.py ==
>>> function2('mohammad')
mohammad
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s4.py ==
>>> function3(2,3)
8
>>> id(function3)
3274945011360
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s4.py ==
>>> 
=============================== RESTART: Shell ===============================
>>> 
=============================== RESTART: Shell ===============================
>>> 
=============================== RESTART: Shell ===============================
>>> function3(2,3)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    function3(2,3)
NameError: name 'function3' is not defined
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s4.py ==
>>> function3(2,4)
16
>>> 
=============================== RESTART: Shell ===============================
>>> import p12-s4
SyntaxError: invalid syntax
>>> import p12_s4
>>> p12_s4.function3(2,10)
1024
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function2('mohammad')
mohammad
>>> name = 'mohammad'
>>> function2(name)
mohammad
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function3(2,4)
16
>>> function3(arg1 = 3, arg2 = 2)
9
>>> function3(arg2 = 5, arg1 = 3)
243
>>> l1 = [4,2,5,7,1]
>>> for i in l1:
	print(i)

	
4
2
5
7
1
>>> print(1,2,4,6)
1 2 4 6
>>> for i in l1:
	print(i, end = ' ')

	
4 2 5 7 1 
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function4(12)
1.2
>>> function4(12,5)
2.4
>>> function4(arg1 = 12, arg2 = 5)
2.4
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function2()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    function2()
TypeError: function2() missing 1 required positional argument: 'arg'
>>> function2(12,12,12)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    function2(12,12,12)
TypeError: function2() takes 1 positional argument but 3 were given
>>> function4(1,5,6,7)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    function4(1,5,6,7)
TypeError: function4() takes from 1 to 2 positional arguments but 4 were given
>>> t1 = (3,5,6,7,8)
>>> sum(t1)
29
>>> result = 0
>>> for sub in t1:
	result += sub

	
>>> result
29
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function5((12,3,7,4))
26
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function6(12,5,7,8,0,11)
done
>>> function6(1)
done
>>> function6()
done
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function6(12,5,7,8,0,11)
(12, 5, 7, 8, 0, 11)
>>> function6(1)
(1,)
>>> function6()
()
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function6(12,5,7,8,0,11)
43
>>> function6(4,3,6)
13
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function7(12,4,6,7,2,6,6, arg2 = 2)
(12, 4, 6, 7, 2, 6, 6, 12, 4, 6, 7, 2, 6, 6)
>>> function6((3,5,6),(2,4,6),(45,7,8))
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    function6((3,5,6),(2,4,6),(45,7,8))
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py", line 29, in function6
    result += sub
TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function6((3,5,6),(2,4,6),(45,7,8))
(3, 5, 6, 2, 4, 6, 45, 7, 8)
>>> t2 = ((3,5,6),(2,4,6),(45,7,8))
>>> for i,x,y in t2:
	print(i,x,y)

	
3 5 6
2 4 6
45 7 8
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function7(3,6,7)
(6, 7, 6, 7, 6, 7)
>>> print(12,4,6,8,9,0,35,8)
12 4 6 8 9 0 35 8
>>> print(sep = '\n',12,4,6,8,9,0,35,8)
SyntaxError: positional argument follows keyword argument
>>> print(sep = '\n', 12,45,7)
SyntaxError: positional argument follows keyword argument
>>> print(sep = '\n', value = (12,45,7))
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    print(sep = '\n', value = (12,45,7))
TypeError: 'value' is an invalid keyword argument for this function
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function8(12,4)
bakhshpazir
>>> function8(12,5)
nistan
>>> sqrt(16)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    sqrt(16)
NameError: name 'sqrt' is not defined
>>> 16 ** 0.5
4.0
>>> import math
>>> math.sqrt(16)
4.0
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function9(3)
aval
>>> function9(17)
aval
aval
aval
aval
aval
aval
aval
aval
aval
aval
aval
aval
aval
aval
aval
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function9(17)
aval
>>> function9(24)
aval nist
aval
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function9(24)
aval nist
>>> function9(17)
aval
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function9(24)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    function9(24)
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py", line 44, in function9
    for i in range(2,arg**0.5):
TypeError: 'float' object cannot be interpreted as an integer
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function9(24)
aval nist
>>> function9(17)
aval
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function10(17,4)
1
>>> function10(17,5)
2
>>> function10(17,17)
0
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function11(3)
6
>>> function11(5)
120
>>> function11(4)
24
>>> num = function11(4)
24
>>> num
>>> type(num)
<class 'NoneType'>
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function13(4)
16
>>> num = function13(4)
16
>>> num
>>> type(num)
<class 'NoneType'>
>>> function12(5)
25
>>> num1 = function12(5)
>>> num1
25
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function14(2,3)
(8, 9)
>>> obj1 = function14(2,3)
>>> obj1
(8, 9)
>>> obj2 = function14(3,5)
>>> obj2
(243, 125)
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> obj2 = function14(3,5)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    obj2 = function14(3,5)
TypeError: function14() takes 0 positional arguments but 2 were given
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function12(3)
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function15(5)
120
>>> function15(3)
6
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function16(7)
13
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function17(100)
'positive'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function17(100)
'positive'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function17(100)
'positive'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function17(100)
'positive'
>>> function17(-100)
'negative'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> function16(50)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    function16(50)
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py", line 92, in function16
    return function16(arg-1) + function16(arg-2)
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py", line 92, in function16
    return function16(arg-1) + function16(arg-2)
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py", line 92, in function16
    return function16(arg-1) + function16(arg-2)
  [Previous line repeated 34 more times]
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> if = 5
SyntaxError: invalid syntax
>>> return = 100
SyntaxError: invalid syntax
>>> print = 120
>>> print
120
>>> print(120)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    print(120)
TypeError: 'int' object is not callable
>>> 
=============================== RESTART: Shell ===============================
>>> def print(arg):
	return arg ** 2

>>> print(12)
144
>>> (lambda arg1,arg2 : arg1 ** arg2)(2,5)
32
>>> (lambda arg1 : arg ** 5)(5)
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    (lambda arg1 : arg ** 5)(5)
  File "<pyshell#154>", line 1, in <lambda>
    (lambda arg1 : arg ** 5)(5)
NameError: name 'arg' is not defined
>>> (lambda arg : arg ** 5)(5)
3125
>>> l1 = [4,6,8,9,3]
>>> l1* 2
[4, 6, 8, 9, 3, 4, 6, 8, 9, 3]
>>> def func(arg):
	return arg * 2

>>> list(map(func , l1))
[8, 12, 16, 18, 6]
>>> l1
[4, 6, 8, 9, 3]
>>> l2 = [ 4,5,7,921]
>>> map(func,l1,l2)
<map object at 0x000002B0A0E687F0>
>>> list(map(func,l1,l2))
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    list(map(func,l1,l2))
TypeError: func() takes 1 positional argument but 2 were given
>>> def func(arg1,arg2):
	return arg1 * arg2

>>> list(map(func,l1,l2))
[16, 30, 56, 8289]
>>> l1
[4, 6, 8, 9, 3]
>>> l2
[4, 5, 7, 921]
>>> list(map(lambda x:x**2, l1))
[16, 36, 64, 81, 9]
>>> l1
[4, 6, 8, 9, 3]
>>> def func(arg1,arg2):
	return arg1, arg2

>>> func(2,3)
(2, 3)
>>> list(map(lambda x:x*2, l1))
[8, 12, 16, 18, 6]
>>> l1
[4, 6, 8, 9, 3]
>>> def func(arg):
	if arg > 0:
		return True
	return False

>>> func(12)
True
>>> func(-12)
False
>>> filter(func,l1)
<filter object at 0x000002B0A0DF8860>
>>> list(filter(func,l1))
[4, 6, 8, 9, 3]
>>> l1
[4, 6, 8, 9, 3]
>>> l3 = [-2,4,1,-5,-7,1,9]
>>> list(filter(func,l3))
[4, 1, 1, 9]
>>> list(filter( lambda x : x > 0, l3))
[4, 1, 1, 9]
>>> l1
[4, 6, 8, 9, 3]
>>> list(filter( lambda x : x % 2 ==  0, l3))
[-2, 4]
>>> list(filter( lambda x : x % 2 ==  0, l1))
[4, 6, 8]
>>> list(filter( lambda x : x % 2 ==0 and x > 0, l3))
[4]
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==l3 = [-2,4,1,-5,-7,1,9]
>>> function16(5)
5
>>> function16(9)
34
>>> function16('salam')
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    function16('salam')
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py", line 86, in function16
    if arg <= 0:
TypeError: '<=' not supported between instances of 'str' and 'int'
>>> filter('str','salam')
<filter object at 0x000001A30F04A7F0>
>>> list(filter('str','salam'))
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    list(filter('str','salam'))
TypeError: 'str' object is not callable
>>> function16(5)
5
>>> function16('salam')
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    function16('salam')
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py", line 86, in function16
    if arg <= 0:
TypeError: '<=' not supported between instances of 'str' and 'int'
>>> def func(arg1,arg2):
	return arg1(arg2)

>>> def arg1(num):
	return num ** 2

>>> func(arg1,3)
9
>>> (lambda x : if x > 0: 5)(3)
SyntaxError: invalid syntax
>>> (lambda x : x % 2 ==  0)(4)
True
>>> function16(3)
2
>>> function16('trt')
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    function16('trt')
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py", line 86, in function16
    if arg <= 0:
TypeError: '<=' not supported between instances of 'str' and 'int'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
yek adad vared konid: salam
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py", line 102, in <module>
    num = int(input('yek adad vared konid: '))
ValueError: invalid literal for int() with base 10: 'salam'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
yek adad vared konid: 12
144
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
yek adad vared konid: salam
vorudi na moatabar
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
vorudi na moatabar
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py", line 104, in <module>
    print(num1/num2)
ZeroDivisionError: division by zero
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
type error
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
12
13

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
day'salam'
khata
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
day'str'
khata
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
day'str'
salam
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
day
salam
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> function16(4)
3
>>> try:
	function16('salam')
except:
	print('error')

	
error
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
error
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
done
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
badaneye try
done
code ejra shode
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
error
code ejra shode
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
error
code ejra shode
>>> def func(arg1,arg2):
	return [arg1,arg2]

>>> func(3,4)
[3, 4]
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12_s4.py ==
>>> 

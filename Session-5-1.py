>>> num = int(input('yek adad vared konid: '))
yek adad vared konid: 13
>>> assert num > 0
>>> assert num < 0
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    assert num < 0
AssertionError
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s5.py ==
sen khod ra vared konid: 12
ali 12 sal sen darad
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s5.py ==
sen khod ra vared konid: -12
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s5.py", line 3, in <module>
    assert age > 0
AssertionError
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s5.py ==
sen khod ra vared konid: -12
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s5.py", line 3, in <module>
    assert age > 0 ,'sen vared shode sahih nist'
AssertionError: sen vared shode sahih nist
>>> l1 = list()
>>> type(l1)
<class 'list'>
>>> class People:
	age = 0
	name = ''
	id_card = 0

	
>>> person1 = People()
>>> type(person1)
<class '__main__.People'>
>>> person1.age
0
>>> person1.name
''
>>> person1.id_card
0
>>> person1.age = 24
>>> person1.age
24
>>> person1.name = 'mohammad'
>>> person1.id_card = 1280034
>>> 
>>> 
>>> person2 = People()
>>> type(person2)
<class '__main__.People'>
>>> person2.age = 90
>>> person2.name = 'ali'
>>> person2.id_card = 567982
>>> person1.age
24
>>> person2.age
90
>>> getattr(person2,age)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    getattr(person2,age)
TypeError: getattr(): attribute name must be string
>>> age
-12
>>> getattr(person2,name)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    getattr(person2,name)
NameError: name 'name' is not defined
>>> name
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> append()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    append()
NameError: name 'append' is not defined
>>> getattr(person2,'age')
90
>>> hasattr(person2,'age')
True
>>> hasattr(person2,'city')
False
>>> person2.city
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    person2.city
AttributeError: 'People' object has no attribute 'city'
>>> person2.age
90
>>> setattr(person2,'age',120)
>>> person2.age
120
>>> delattr(person2,'age')
>>> person2.age
0
>>> person1.age
24
>>> person1.name
'mohammad'
>>> person1.id_card
1280034
>>> person2.hair_color = 'black'
>>> person2.hair_color
'black'
>>> person1.hair_color
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    person1.hair_color
AttributeError: 'People' object has no attribute 'hair_color'
>>> person2.age
0
>>> del(person2.age)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    del(person2.age)
AttributeError: age
>>> del(person2.hair_color)
>>> person2.hair_color
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    person2.hair_color
AttributeError: 'People' object has no attribute 'hair_color'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s5.py ==
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s5.py", line 15, in <module>
    person1.age = 90
NameError: name 'person1' is not defined
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s5.py ==
kodum attr mikhay taghir bedi ya bebini: age
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s5.py ==
kodum attr mikhay taghir bedi ya bebini: age
90
True
>>> person1.age
90
>>> person1.name
'ali'
>>> id(person1.name)
1890906378456
>>> setattr(person1,'name','Mohammad')
>>> person1.name
'Mohammad'
>>> id(person1.name)
1890906288496
>>> person1.name = "jadid
SyntaxError: EOL while scanning string literal
>>> person1.name = "jadid"
>>> l1 = [5,2,7]
>>> del(l1)
>>> l1
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    l1
NameError: name 'l1' is not defined
>>> class Points:
	x = 0
	y = 0

	
>>> P1 = Points()
>>> P1.x = 3
>>> P1.y = 4
>>> P2 = Points()
>>> P2.x = 5
>>> P2.y = 2
>>> def dist(Point):
	return (Point.x ** 2 + Point.y ** 2) ** 0.5

>>> def dist(arg):
	return (arg.x ** 2 + arg.y ** 2) ** 0.5

>>> dist(P1)
5.0
>>> l1 = [5,3,6]
>>> dist(l1)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    dist(l1)
  File "<pyshell#78>", line 2, in dist
    return (arg.x ** 2 + arg.y ** 2) ** 0.5
AttributeError: 'list' object has no attribute 'x'
>>> 
=============================== RESTART: Shell ===============================
>>> class Points:
	x = 0
	y = 0

	
>>> class Points:
	x = 0
	y = 0
	def dist(arg):
		return (arg.x ** 2 + arg.y ** 2) ** 0.5

	
>>> P1 = Points()
>>> P1.x = 5
>>> P1.y = 4
>>> P1.dist()
6.4031242374328485
>>> def func(arg):
	return arg ** 2

>>> func(2)
4
>>> func()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    func()
TypeError: func() missing 1 required positional argument: 'arg'
>>> func(3,2)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    func(3,2)
TypeError: func() takes 1 positional argument but 2 were given
>>> class Points:
	x = 0
	y = 0
	def dist():
		return 'salam'

	
>>> P1 = Points()
>>> P1.dist()
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    P1.dist()
TypeError: dist() takes 0 positional arguments but 1 was given
>>> class Points:
	x = 0
	y = 0
	def dist(arg):
		return (arg.x ** 2 + arg.y ** 2) ** 0.5

	
>>> class Points:
	x = 0
	y = 0
	def dist(arg1,arg2):
		return ((arg2.x ** 2 + arg2.y ** 2) ** 0.5)*2

	
>>> P1 = Points()
>>> P1.x = 3
>>> P1.y = 4
>>> class Points:
	x = 0
	y = 0
	def dist(arg1,arg2):
		return ((arg1.x ** 2 + arg1.y ** 2) ** 0.5)*2

	
>>> 
>>> P1 = Points()
>>> P1.x = 3
>>> P1.y = 4
>>> P1.dist(2)
10.0
>>> class Points:
	x = 0
	y = 0
	def dist(arg1,arg2):
		return ((arg1.x ** 2 + arg1.y ** 2) ** 0.5)*arg2

	
>>> P1 = Points()
>>> P1.x = 3
>>> P1.y = 4
>>> P1.dist(2)
10.0
>>> P1.dist(3)
15.0
>>> P1.dist(4)
20.0
>>> l1 = [4,65,7]
>>> type(P1)
<class '__main__.Points'>
>>> class Points:
	x = 0
	y = 0
	def dist(arg1,arg2):
		return ((arg1.x ** 2 + arg1.y ** 2) ** 0.5)*arg2
	def show(arg):
		return (x,y)

	
>>> P1 = Points()
>>> P1.x = 3
>>> P1.y = 4
>>> P1.show()
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    P1.show()
  File "<pyshell#132>", line 7, in show
    return (x,y)
NameError: name 'x' is not defined
>>> class Points:
	x = 0
	y = 0
	def dist(arg1,arg2):
		return ((arg1.x ** 2 + arg1.y ** 2) ** 0.5)*arg2
	def show(arg):
		return (arg.x,arg.y)

	
>>> P1 = Points()
>>> P1.x = 3
>>> P1.y = 4
>>> P1.show()
(3, 4)
>>> class Time:
	Hour = 0
	Minute = 0
	Second = 0
	def show(arg):
		return str(arg.Hour)+':'+str(arg.Minute)+':'+str(arg.Second)

	
>>> t1 = Time()
>>> t1.Hour = 12
>>> t1.Minute = 43
>>> t1.Second = 29
>>> t1.show()
'12:43:29'
>>> class Points:
	
	def __init__(arg,x_coordinate,y_coordinate):
		arg.x = x_coordinate
		arg.y = y_coordinate
		
	def dist(arg1,arg2):
		return ((arg1.x ** 2 + arg1.y ** 2) ** 0.5)*arg2
	def show(arg):
		return (x,y)

	
>>> P1 = Points(3,4)
>>> P1.x
3
>>> P1.y
4
>>> P1 = Points()
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    P1 = Points()
TypeError: __init__() missing 2 required positional arguments: 'x_coordinate' and 'y_coordinate'
>>> class Points:

	def __init__(arg,x_coordinate = 0,y_coordinate = 0):
		arg.x = x_coordinate
		arg.y = y_coordinate

	def dist(arg1,arg2):
		return ((arg1.x ** 2 + arg1.y ** 2) ** 0.5)*arg2
	def show(arg):
		return (x,y)

	
>>> P2 = Points(3,4)
>>> P2.x
3
>>> P2.y
4
>>> class Points:

	def __init__(self,x_coordinate = 0,y_coordinate = 0):
		self.x = x_coordinate
		self.y = y_coordinate

	def dist(self,arg2):
		return ((self.x ** 2 + self.y ** 2) ** 0.5)*arg2
	def show(self):
		return (x,y)

	
>>> t1 = Time()
>>> t1.Hour = 12
>>> t1.Minute = 5
>>> t1.Second = 8
>>> p1 = Points(4,6)
>>> class People:
	def __init__(self,age_value,name_value,id_card_value):
		
		self.age = age_value
		self.name = name_value
		self.id_card = id_card_value

		
>>> p1 = People(23,'mohammad',63882)
>>> del(p1.age)
>>> p1.age
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    p1.age
AttributeError: 'People' object has no attribute 'age'
>>> delattr(p1,'name')
>>> p1.name
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    p1.name
AttributeError: 'People' object has no attribute 'name'
>>> print(p1)
<__main__.People object at 0x000001BDC8BD6E80>
>>> print(t1)
<__main__.Time object at 0x000001BDC8B7D358>
>>> Num = 12
>>> Num
12
>>> p1
<__main__.People object at 0x000001BDC8BD6E80>
>>> t1
<__main__.Time object at 0x000001BDC8B7D358>
>>> class Points:

	def __init__(self,x_coordinate = 0,y_coordinate = 0):
		self.x = x_coordinate
		self.y = y_coordinate

	def dist(self,arg2):
		return ((self.x ** 2 + self.y ** 2) ** 0.5)*arg2
	def show(self):
		return (x,y)
	
	def __str__(self):
		return str(self.x)+':'+str(self.y)

	
>>> P1 = Points(3,4)
>>> print(P1)
3:4
>>> P1
<__main__.Points object at 0x000001BDC8BD6D30>
>>> class Points:

	def __init__(self,x_coordinate = 0,y_coordinate = 0):
		self.x = x_coordinate
		self.y = y_coordinate

	def dist(self,arg2):
		return ((self.x ** 2 + self.y ** 2) ** 0.5)*arg2
	def show(self):
		return (x,y)

	def __str__(self):
		return str(self.x)+':'+str(self.y)
	def __repr__(self):
		return str(self.x)+':'+str(self.y)

	
>>> P1 = Points(3,4)
>>> print(P1)
3:4
>>> P1
3:4
>>> l1 = [3,4,5]
>>> l2 = [5,2,6]
>>> m1 = zip(l1,l2)
>>> m1
<zip object at 0x000001BDC8BEEEC8>
>>> print(m1)
<zip object at 0x000001BDC8BEEEC8>
>>> list(m1)
[(3, 5), (4, 2), (5, 6)]
>>> P2 = Points(5,9)
>>> P1 + P1
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    P1 + P1
TypeError: unsupported operand type(s) for +: 'Points' and 'Points'
>>> P1.show()
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    P1.show()
  File "<pyshell#198>", line 10, in show
    return (x,y)
NameError: name 'x' is not defined
>>> class Points:

	def __init__(self,x_coordinate = 0,y_coordinate = 0):
		self.x = x_coordinate
		self.y = y_coordinate

	def dist(self,arg2):
		return ((self.x ** 2 + self.y ** 2) ** 0.5)*arg2
	def show(self):
		return (self.x,self.y)

	def __str__(self):
		return str(self.x)+':'+str(self.y)
	def __repr__(self):
		return str(self.x)+':'+str(self.y)

	
>>> P1 = Points(3,4)
>>> P1.show()
(3, 4)
>>> P1
3:4
>>> class Points:

	def __init__(self,x_coordinate = 0,y_coordinate = 0):
		self.x = x_coordinate
		self.y = y_coordinate

	def dist(self,arg2):
		return ((self.x ** 2 + self.y ** 2) ** 0.5)*arg2
	def show(self):
		return (self.x,self.y)

	def __str__(self):
		return str(self.x)+':'+str(self.y)
	def __repr__(self):
		return str(self.x)+':'+str(self.y)
	def __add__(self,other):
		return self.x + other.x,self.y + other.y

	
>>> P1 = Points(3,4)
>>> P2 = Points(12,7)
>>> P1 + P2
(15, 11)
>>> P1 + 2
Traceback (most recent call last):
  File "<pyshell#225>", line 1, in <module>
    P1 + 2
  File "<pyshell#221>", line 17, in __add__
    return self.x + other.x,self.y + other.y
AttributeError: 'int' object has no attribute 'x'
>>> class Points:

	def __init__(self,x_coordinate = 0,y_coordinate = 0):
		self.x = x_coordinate
		self.y = y_coordinate

	def dist(self,arg2):
		return ((self.x ** 2 + self.y ** 2) ** 0.5)*arg2
	def show(self):
		return (self.x,self.y)

	def __str__(self):
		return str(self.x)+':'+str(self.y)
	def __repr__(self):
		return str(self.x)+':'+str(self.y)
	def __add__(self,other):
		return self.x + other,self.y + other

	
>>> P1 = Points(3,4)
>>> P1 + 4
(7, 8)
>>> class Points:

	def __init__(self,x_coordinate = 0,y_coordinate = 0):
		self.x = x_coordinate
		self.y = y_coordinate

	def dist(self,arg2):
		return ((self.x ** 2 + self.y ** 2) ** 0.5)*arg2
	def show(self):
		return (self.x,self.y)

	def __str__(self):
		return str(self.x)+':'+str(self.y)
	def __repr__(self):
		return str(self.x)+':'+str(self.y)
	def __add__(self,other):
		return self.x + other.x,self.y + other.y
	def __sub__(self,other):
		return self.x - other.x, self.y - other.y

	
>>> P1 = Points(3,4)
>>> P2 = Points(10,9)
>>> P2 - P1
(7, 5)
>>> minute = 256
>>> minute//60
4
>>> minute - 60
196
>>> P1 + P2 + P1
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    P1 + P2 + P1
TypeError: can only concatenate tuple (not "Points") to tuple
>>> class Points:

	def __init__(self,x_coordinate = 0,y_coordinate = 0):
		self.x = x_coordinate
		self.y = y_coordinate

	def dist(self,arg2):
		return ((self.x ** 2 + self.y ** 2) ** 0.5)*arg2
	def show(self):
		return (self.x,self.y)

	def __str__(self):
		return str(self.x)+':'+str(self.y)
	def __repr__(self):
		return str(self.x)+':'+str(self.y)
	def __add__(self,other):
		return Points(self.x + other.x,self.y + other.y)
	def __sub__(self,other):
		return self.x - other.x, self.y - other.y

	
>>> P1 = Points(3,4)
>>> P2 = Points(5,10)
>>> P1 + P2 + P1
11:18
>>> class People:
	def __init__(self,age_value,name_value,id_card_value):

		self.age = age_value
		self.name = name_value
		self.id_card = id_card_value

		
>>> class People:
	def __init__(self,age_value,name_value,id_card_value):

		self.age = age_value
		self.name = name_value
		self.id_card = id_card_value
	def show(self):
		return self.name
	hair_color = 'black'

	
>>> class Students(People):
	major = ''
	university = ''

	
>>> S1 = Students(25,'mohammad',63839)
>>> class Students(People):
	major = ''
	university = ''
	hair_color = 'white'

	
>>> S1 = Students(23,'ali',67282)
>>> S1.hair_color
'white'
>>> S1.company
Traceback (most recent call last):
  File "<pyshell#265>", line 1, in <module>
    S1.company
AttributeError: 'Students' object has no attribute 'company'
>>> class Iranian:
	hair_color = 'yellow'

	
>>> class Students(People,Iranian):
	major = ''
	university = ''
	hair_color = 'white'

	
>>> S1 = Students(23,'ali',67282)
>>> S1.hair_color
'white'
>>> class Students(People,Iranian):
	major = ''
	university = ''

	
>>> S1 = Students(23,'ali',67282)
>>> S1.hair_color
'black'
>>> class People:
	def __init__(self,age_value,name_value,id_card_value):

		self.age = age_value
		self.name = name_value
		self.id_card = id_card_value
	def show(self):
		return self.name

	
>>> class Students(People,Iranian):
	major = ''
	university = ''

	
>>> S1 = Students(23,'ali',67282)
>>> S1.hair_color
'yellow'
>>> class People:
	def __init__(self,age_value,name_value,id_card_value):

		self.age = age_value
		self.name = name_value
		self.id_card = id_card_value
	def show(self):
		return self.name

	
>>> class Students(People,Iranian):
	def __ini__(self,major,university):
		self.major = major
		self.university = university

		
>>> S1 = Students(23,'name',73737)
>>> class Students(People,Iranian):
	def __init__(self,major,university):
		self.major = major
		self.university = university

		
>>> S1 = Students('GIS','UT')
>>> isinstance(S1,Students)
True
>>> isinstance(S1,People)
True
>>> issubclass(Students,People)
True
>>> issubclass(People,Iranian)
False
>>> raise TypeError
Traceback (most recent call last):
  File "<pyshell#298>", line 1, in <module>
    raise TypeError
TypeError
>>> raise AttributeError
Traceback (most recent call last):
  File "<pyshell#299>", line 1, in <module>
    raise AttributeError
AttributeError
>>> M = type(12)
>>> M
<class 'int'>
>>> str(M)
"<class 'int'>"
>>> str1 = 'shshs'
>>> type(str1)
<class 'str'>
>>> isinstance(str1,str)
True
>>> class Students:
	def __init__(self,major,university):
		if isinstance(major,int):
			raise TypeError
		else:
			self.major = major
			self.university = university

			
>>> 
>>> S1 = Students(12,'UT')
Traceback (most recent call last):
  File "<pyshell#310>", line 1, in <module>
    S1 = Students(12,'UT')
  File "<pyshell#308>", line 4, in __init__
    raise TypeError
TypeError
>>> def fact(num):
	if num == 1:
		return 1
	else:
		return num * fact(num -1)

	
>>> fact(6)
720
>>> fact('salam')
Traceback (most recent call last):
  File "<pyshell#318>", line 1, in <module>
    fact('salam')
  File "<pyshell#316>", line 5, in fact
    return num * fact(num -1)
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> def fact(num):
	if isinstance(num, str):
		return 'vorudi eshtebah'
	if num == 1:
		return 1
	else:
		return num * fact(num -1)

	
>>> fact('salam')
'vorudi eshtebah'
>>> import m1
>>> import Session_2_1
Traceback (most recent call last):
  File "<pyshell#324>", line 1, in <module>
    import Session_2_1
ModuleNotFoundError: No module named 'Session_2_1'
>>> import os

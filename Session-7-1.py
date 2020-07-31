
>>> import os
>>> os.getcwd()
'C:\\Users\\esmae\\AppData\\Local\\Programs\\Python\\Python36'
>>> import m1
>>> import Session_4_1
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    import Session_4_1
ModuleNotFoundError: No module named 'Session_4_1'
>>> os.chdir('C:\\Users\\esmae\\Desktop\\UTech\\Python Course\\Session 4')
>>> os.getcwd()
'C:\\Users\\esmae\\Desktop\\UTech\\Python Course\\Session 4'
>>> import Session_4_1
hi
>>> a1 = Session_4_1.time(12,6,5)
>>> type(a1)
<class 'Session_4_1.time'>
>>> os.listdir()
['Python-4.pdf', 'Session-4-2.py', 'Session_4_1.py', '__pycache__']
>>> os.mkdir('salam')
>>> os.path.join('C:\\Users\\esmae\\Desktop\\UTech\\Python Course\\Session 4','salam')
'C:\\Users\\esmae\\Desktop\\UTech\\Python Course\\Session 4\\salam'
>>> os.getcwd()
'C:\\Users\\esmae\\Desktop\\UTech\\Python Course\\Session 4'
>>> import salam
>>> import salam.modul1
>>> import numpy
>>> import numpy.random
>>> 
=============================== RESTART: Shell ===============================
>>> import numpy
>>> 
=============================== RESTART: Shell ===============================
>>> os.getcwd()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    os.getcwd()
NameError: name 'os' is not defined
>>> import os
>>> os.getcwd()
'C:\\Users\\esmae\\AppData\\Local\\Programs\\Python\\Python36'
>>> os.chdir('C:\\Users\\esmae\\Desktop\\UTech\\Python Course\\Session 4')
>>> os.listdir()
['names.txt', 'Python-4.pdf', 'salam', 'Session-4-2.py', 'Session_4_1.py', '__pycache__']
>>> open('names.txt','r')
<_io.TextIOWrapper name='names.txt' mode='r' encoding='cp1252'>
>>> file = open('names.txt','r')
>>> file.close()
>>> with open('names.txt','r') as file:
	pass

>>> file = open('names.txt','r')
>>> file.write('salam')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    file.write('salam')
io.UnsupportedOperation: not writable
>>> file.readable()
True
>>> file.read()
'mohammad\nali\nhasan\nhosein\nzahra'
>>> file.read()
''
>>> file.seek(0)
0
>>> file.read()
'mohammad\nali\nhasan\nhosein\nzahra'
>>> file.seek(0)
0
>>> file.read(5)
'moham'
>>> file.seek(0)
0
>>> file.readline()
'mohammad\n'
>>> file.readline()
'ali\n'
>>> file.readline()
'hasan\n'
>>> file.seek(0)
0
>>> file.readlines()
['mohammad\n', 'ali\n', 'hasan\n', 'hosein\n', 'zahra']
>>> file.close()
>>> with open('names.txt','r') as file:
	file.readlines()

	
['mohammad\n', 'ali\n', 'hasan\n', 'hosein\n', 'zahra']
>>> file = open('names.txt','w')
>>> file.write('salam donya')
11
>>> file.close()
>>> file = open('names.txt','w')
>>> file.writable()
True
>>> file.readable()
False
>>> file.writelines(['mohammad\n', 'ali\n', 'hasan\n', 'hosein\n', 'zahra'])
>>> file.close()
>>> file = open('names.txt','w')
>>> file.readlines()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    file.readlines()
io.UnsupportedOperation: not readable
>>> file.close()
>>> file = open('names.txt','a')
>>> file.write('salam donya')
11
>>> file.close()
>>> file = open('names.txt','a')
>>> file.write('mohammad hastam')
15
>>> file.close()
>>> file = open('names.txt','r')
>>> 
>>> file.readlines()
['12\n', '14\n', '16\n', '20\n', '23\n', '10']
>>> file.seek(0)
0
>>> lines = file.readlines()
>>> list1 = []
>>> for i in lines:
	list1.append(int(i[:-2]))

	
Traceback (most recent call last):
  File "<pyshell#73>", line 2, in <module>
    list1.append(int(i[:-2]))
ValueError: invalid literal for int() with base 10: ''
>>> for i in lines:
	print(i)
	list1.append(int(i[:-2]))

	
12

14

16

20

23

10
Traceback (most recent call last):
  File "<pyshell#75>", line 3, in <module>
    list1.append(int(i[:-2]))
ValueError: invalid literal for int() with base 10: ''
>>> for i in lines:
	print(i[:-2])

	
1
1
1
2
2

>>> lines
['12\n', '14\n', '16\n', '20\n', '23\n', '10']
>>> for i in lines:
	print(i[:-1])

	
12
14
16
20
23
1
>>> for i in lines:
	print(int(i[:-1]))

	
12
14
16
20
23
1
>>> for i in lines:
	list1.append(int(i[:-1]))

	
>>> list1
[1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 12, 14, 16, 20, 23, 1]
>>> list1 = []
>>> for i in lines:
	list1.append(int(i[:-1]))

	
>>> list1
[12, 14, 16, 20, 23, 1]
>>> for i in lines:
	if i[-1] == '\n':
		print('done')

		
done
done
done
done
done
>>> lines
['12\n', '14\n', '16\n', '20\n', '23\n', '10']
>>> for i in lines:
	if i[-1] == '\n':
		list1.append(int(i[:-1]))
	else:
		list1.append(int(i))

		
>>> list1 = []
>>> for i in lines:
	if i[-1] == '\n':
		list1.append(int(i[:-1]))
	else:
		list1.append(int(i))

		
>>> list1
[12, 14, 16, 20, 23, 10]
>>> file.close()
>>> file = open('names.txt','r')
>>> lines = file.readlines()
>>> lines
['Name,age\n', 'ali,32\n', 'mohammad,51']
>>> 'salam donya man mohammad hastam'
'salam donya man mohammad hastam'
>>> str1 = 'salam donya man mohammad hastam'
>>> str1.split(sep = ' ')
['salam', 'donya', 'man', 'mohammad', 'hastam']
>>> str2 = 'Name,age'
>>> str2.split(sep = ',')
['Name', 'age']
>>> 
=============================== RESTART: Shell ===============================
>>> list1 = []
>>> def func(arg):
	list1.append()

	
>>> func(5)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    func(5)
  File "<pyshell#115>", line 2, in func
    list1.append()
TypeError: append() takes exactly one argument (0 given)
>>> def func(arg):
	list1.append(arg)

	
>>> func(5)
>>> func(6)
>>> list1
[5, 6]
>>> def func1(arg):
	num = arg ** 2

	
>>> func1(5)
>>> func1(6)
>>> num
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    num
NameError: name 'num' is not defined
>>> Num = 10
>>> l1 = [4,56,8]
>>> Num ** 2
100
>>> Num * 5
50
>>> l1.append(8)
>>> l1
[4, 56, 8, 8]
>>> def func1(arg):
	global num
	num = arg ** 2

	
>>> func1(5)
>>> num
25
>>> def func1(arg):
	num = arg ** 2

	
>>> num
25
>>> 
=============================== RESTART: Shell ===============================
>>> def func1(arg):
	num = arg ** 2

	
>>> func1(5)
>>> num
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    num
NameError: name 'num' is not defined
>>> def general_func(arg):
	def func1():
		pass
	def func2():
		pass
	def func3():
		pass

	
>>> def general_func():
	def func1():
		num = 5
	def func2():
		pass
	def func3():
		pass
	print(num)

	
>>> general_func()
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    general_func()
  File "<pyshell#157>", line 8, in general_func
    print(num)
NameError: name 'num' is not defined
>>> def general_func():
	def func1():
		nonlocal num
		num = 5
	def func2():
		pass
	def func3():
		pass
	print(num)
	
SyntaxError: no binding for nonlocal 'num' found
>>> def general_func():
	nonlocal num
	def func1():
		
		num = 5
	def func2():
		pass
	def func3():
		pass
	print(num)
	
SyntaxError: no binding for nonlocal 'num' found
>>> def general_func():
	
	def func1():
		nonlocal num
		num = 5
	def func2():
		pass
	def func3():
		pass
	print(num)
	
SyntaxError: no binding for nonlocal 'num' found
>>> 
=============================== RESTART: Shell ===============================
>>> def general_func():
	num = 10
	def func1():
		nonlocal num
		num = 5
	def func2():
		pass
	def func3():
		pass
	print(num)

	
>>> general_func()
10
>>> def general_func():
	num = 10
	def func1():
		nonlocal num
		num = 5
	def func2():
		pass
	def func3():
		pass
	func1()
	print(num)

	
>>> general_func()
5
>>> 
=============================== RESTART: Shell ===============================
>>> def func1():
	num = 5

	
>>> num = 10
>>> num
10
>>> num
10
>>> func1()
>>> num
10
>>> def func1():
	global num
	num = 5

	
>>> func1()
>>> num
5
>>> def general_func():
	num = 10
	def func1():
		
		num = 5
	func1()
	print(num)

	
>>> general_func()
10
>>> def general_func():
	num = 10
	def func1():
		nonlocal num
		num = 5
	func1()
	print(num)

	
>>> general_func()
5
>>> 
=============================== RESTART: Shell ===============================
>>> def general_func():
	num = 10
	def func1():
		nonlocal num
		num = 5
	func1()
	print(num)

	
>>> general_func()
5
>>> num
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    num
NameError: name 'num' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> def func():
	num = 5

	
>>> num
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    num
NameError: name 'num' is not defined
>>> def func():
	global num
	num = 5

	
>>> num
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    num
NameError: name 'num' is not defined
>>> func()
>>> num
5
>>> import tkinter
>>> import json
>>> import csv
>>> import matplotlib.pyplot as plt
>>> fig = plt.figure(facecolor = (1,0,0,1))
>>> plt.show()
>>> fig = plt.figure(facecolor = (1,0,0,0.1))
>>> plt.show()
>>> fig = plt.figure(figsize = (2,2))
>>> plt.show()
>>> fig = plt.figure()
>>> ax = fig.add_subplot(111)
>>> ax.set(xlabel = 'mehvar x ha',ylabel = 'mehvar y ha',title = 'sample matplot', xlim = [0,5],ylim = [10,100])
[(10, 100), Text(0, 0.5, 'mehvar y ha'), (0, 5), Text(0.5, 0, 'mehvar x ha'), Text(0.5, 1.0, 'sample matplot')]
>>> plt.show()
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==
esme khodetuno vared konid: mohammad
salam man mohammad hsatam
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==
esme khodetuno vared konid: ali
salam man ali hsatam
>>> str1 = 'sen man {} hast'
>>> str1.format(25)
'sen man 25 hast'
>>> str2 = 'man {} hastam {} sen daram'
>>> str2.format('ali',25)
'man ali hastam 25 sen daram'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==
>>> xh
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    xh
NameError: name 'xh' is not defined
>>> xha
array([0.        , 0.6981317 , 1.3962634 , 2.0943951 , 2.7925268 ,
       3.4906585 , 4.1887902 , 4.88692191, 5.58505361, 6.28318531])
>>> yha
array([ 0.00000000e+00,  6.42787610e-01,  9.84807753e-01,  8.66025404e-01,
        3.42020143e-01, -3.42020143e-01, -8.66025404e-01, -9.84807753e-01,
       -6.42787610e-01, -2.44929360e-16])
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py", line 14, in <module>
    ax.show()
AttributeError: 'AxesSubplot' object has no attribute 'show'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p12-s7.py ==
>>> A = np.arange(100).reshape(10,10)
>>> A
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
       [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
       [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
       [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
       [70, 71, 72, 73, 74, 75, 76, 77, 78, 79],
       [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
       [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]])
>>> MUL = A[:5,:5]
>>> MUR = A[:5,5:]
>>> MLL = A[5:,:5]
>>> MLR = A[5:,5:]
>>> MUL
array([[ 0,  1,  2,  3,  4],
       [10, 11, 12, 13, 14],
       [20, 21, 22, 23, 24],
       [30, 31, 32, 33, 34],
       [40, 41, 42, 43, 44]])
>>> MUR
array([[ 5,  6,  7,  8,  9],
       [15, 16, 17, 18, 19],
       [25, 26, 27, 28, 29],
       [35, 36, 37, 38, 39],
       [45, 46, 47, 48, 49]])
>>> MLL
array([[50, 51, 52, 53, 54],
       [60, 61, 62, 63, 64],
       [70, 71, 72, 73, 74],
       [80, 81, 82, 83, 84],
       [90, 91, 92, 93, 94]])
>>> MLR
array([[55, 56, 57, 58, 59],
       [65, 66, 67, 68, 69],
       [75, 76, 77, 78, 79],
       [85, 86, 87, 88, 89],
       [95, 96, 97, 98, 99]])
>>> type(MLR)
<class 'numpy.ndarray'>
>>> MLR.shape()
Traceback (most recent call last):
  File "<pyshell#231>", line 1, in <module>
    MLR.shape()
TypeError: 'tuple' object is not callable
>>> MLR
array([[55, 56, 57, 58, 59],
       [65, 66, 67, 68, 69],
       [75, 76, 77, 78, 79],
       [85, 86, 87, 88, 89],
       [95, 96, 97, 98, 99]])
>>> MLR.shape
(5, 5)
>>> np.array(MLR)
array([[55, 56, 57, 58, 59],
       [65, 66, 67, 68, 69],
       [75, 76, 77, 78, 79],
       [85, 86, 87, 88, 89],
       [95, 96, 97, 98, 99]])
>>> a = np.array(MLR)
>>> a.shape
(5, 5)
>>> a.reshape((1,5,5))
array([[[55, 56, 57, 58, 59],
        [65, 66, 67, 68, 69],
        [75, 76, 77, 78, 79],
        [85, 86, 87, 88, 89],
        [95, 96, 97, 98, 99]]])
>>> ndim(a)
Traceback (most recent call last):
  File "<pyshell#238>", line 1, in <module>
    ndim(a)
NameError: name 'ndim' is not defined
>>> a.ndim
2
>>> a = a.reshape((1,5,5))
>>> a.ndim
3
>>> l1 = [(),()]
>>> l1 = [(0,0),(5,5)]
>>> l2 = [(5,0),(0,5)]
>>> A = np.array([[0,0,1],[5,5,1],[5,0,1]])
>>> B = np.array([[0,0,1],[5,5,1],[0,5,1]])
>>> np.linalg.det(A)
-24.999999999999996
>>> np.linalg.det(B)
24.999999999999996
>>> l3 = [(1,0),(3,4)]
>>> A = np.array([[0,0,1],[5,5,1],[1,0,1]])
>>> B = np.array([[0,0,1],[5,5,1],[3,4,1]])
>>> np.linalg.det(A)
-4.999999999999999
>>> np.linalg.det(B)
4.999999999999997
>>> l3 = [(0,1),(3,4)]
>>> B = np.array([[0,0,1],[5,5,1],[3,4,1]])
>>> A = np.array([[0,0,1],[5,5,1],[0,1,1]])
>>> A = np.array([[0,0,1],[5,5,1],[1,0,1]])
>>> np.linalg.det(A)
-4.999999999999999
>>> np.linalg.det(B)
4.999999999999997
>>> A = np.array([[0,0,1],[5,5,1],[0,1,1]])
>>> np.linalg.det(A)
4.999999999999999
>>> np.linalg.det(B)
4.999999999999997
>>> 
 RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/lineintersection.py 
mokhtasat khat aval ro vared konid: (12,4),(4,6)
mokhtasat khat dovvom ro vared konid: (5,8),(10,10)
>>> l1
'(12,4),(4,6)'
>>> l2
'(5,8),(10,10)'
>>> list(l1)
['(', '1', '2', ',', '4', ')', ',', '(', '4', ',', '6', ')']
>>> l1.split('),(')
['(12,4', '4,6)']
>>> l1[1:-1]
'12,4),(4,6'
>>> l1[1:-1].split('),(')
['12,4', '4,6']
>>> a = l1[1:-1].split('),(')
>>> a
['12,4', '4,6']
>>> a[0]
'12,4'
>>> a[1]
'4,6'
>>> a[0].split(',')
['12', '4']
>>> list(map(int,['12', '4']))
[12, 4]
>>> 
 RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/lineintersection.py 
mokhtasat khat aval ro vared konid: (12,5),(45,3)
mokhtasat khat dovvom ro vared konid: (0,0),(6,6)
>>> l1
[(12, 5), (12, 5)]
>>> l2
[(0, 0), (0, 0)]
>>> 
 RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/lineintersection.py 
mokhtasat khat aval ro vared konid: (12,5),(45,3)
mokhtasat khat dovvom ro vared konid: (0,0),(6,6)
>>> l1
[(12, 5), (45, 3)]
>>> l2
[(0, 0), (6, 6)]
>>> 
 RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/lineintersection.py 
mokhtasat khat aval ro vared konid: (0,0),(5,5)
mokhtasat khat dovvom ro vared konid: (0,1)(3,4)
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/lineintersection.py", line 8, in <module>
    l2 = [tuple(map(int,l2[0].split(','))),tuple(map(int,l2[1].split(',')))]
ValueError: invalid literal for int() with base 10: '1)(3'
>>> 
 RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/lineintersection.py 
mokhtasat khat aval ro vared konid: (0,0),(5,5)
mokhtasat khat dovvom ro vared konid: (0,1),(3,4)
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/lineintersection.py", line 10, in <module>
    A = np.array([[l1[0][0],l1[0][1],1],[l1[1][0],l1[1][1],1],[l2[0][0],l2[0][1],1]])
NameError: name 'np' is not defined
>>> 
 RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/lineintersection.py 
mokhtasat khat aval ro vared konid: (0,0),(5,5)
mokhtasat khat dovvom ro vared konid: (0,1),(3,4)
taghato nadarand
>>> 
 RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/lineintersection.py 
mokhtasat khat aval ro vared konid: (0,0),(5,5)
mokhtasat khat dovvom ro vared konid: (5,0),(0,5)
moteghate hastan
>>> 
 RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/lineintersection.py 
>>> line_intersection([(0,0),(5,5)],[(5,0),(0,5)])
True
>>> 
 RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/lineintersection.py 
>>> det_mosalas((0,0),(5,5),(5,0))
Traceback (most recent call last):
  File "<pyshell#280>", line 1, in <module>
    det_mosalas((0,0),(5,5),(5,0))
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/lineintersection.py", line 22, in det_mosalas
    return np.linalg.det(np.array([[p1[0][0],p1[0][1],1],[p2[1][0],p2[1][1],1],[p3[0][0],p3[0][1],1]]))
TypeError: 'int' object is not subscriptable
>>> 
 RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/lineintersection.py 
>>> det_mosalas((0,0),(5,5),(5,0))
-24.999999999999996
>>> 
 RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/lineintersection.py 
>>> point_in_polygon([(0,0),(0,1),(1,1),(1,0)],(0.5,0.5))
[(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)]
>>> 
 RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/lineintersection.py 
>>> point_in_polygon([(0,0),(0,1),(1,1),(1,0)],(0.5,0.5))
Traceback (most recent call last):
  File "<pyshell#283>", line 1, in <module>
    point_in_polygon([(0,0),(0,1),(1,1),(1,0)],(0.5,0.5))
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/lineintersection.py", line 29, in point_in_polygon
    result *= det_mosalas(polygon[i],polygon[i+1],point)
IndexError: list index out of range
>>> 
 RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/lineintersection.py 
>>> point_in_polygon([(0,0),(0,1),(1,1),(1,0)],(0.5,0.5))
True
>>> 

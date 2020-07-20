>>> l1 = [12,65,89,34,23]
>>> type(l1)
<class 'list'>
>>> l1 = ['45','salam','a',76,23,3.5]
>>> l1[13]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    l1[13]
IndexError: list index out of range
>>> l1[0:2]
['45', 'salam']
>>> str1 = 'salam'
>>> str1[0] = 'S'
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    str1[0] = 'S'
TypeError: 'str' object does not support item assignment
>>> l1[0] = 'mohammad'
>>> print(l1)
['mohammad', 'salam', 'a', 76, 23, 3.5]
>>> id(str1)
2628580335832
>>> str1 = 'Salam!'
>>> id(str1)
2628580337512
>>> id(l1)
2628539510344
>>> print(l1)
['mohammad', 'salam', 'a', 76, 23, 3.5]
>>> l1[2] = 3.14
>>> print(l1)
['mohammad', 'salam', 3.14, 76, 23, 3.5]
>>> id(l1)
2628539510344
>>> len(l1)
6
>>> str1
'Salam!'
>>> str1.find('l')
2
>>> str1
'Salam!'
>>> del(str1)
>>> str1
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    str1
NameError: name 'str1' is not defined
>>> l1
['mohammad', 'salam', 3.14, 76, 23, 3.5]
>>> l2 = [12,74,87,120,['salam','mohammad','hastam'],75,96,100]
>>> len(l2)
8
>>> l2[4]
['salam', 'mohammad', 'hastam']
>>> l2[4][1]
'mohammad'
>>> l2[4][-2]
'mohammad'
>>> l2[4][-2][3]
'a'
>>> l2[4][-2][2:4]
'ha'
>>> l2
[12, 74, 87, 120, ['salam', 'mohammad', 'hastam'], 75, 96, 100]
>>> del(l2[3])
>>> l2
[12, 74, 87, ['salam', 'mohammad', 'hastam'], 75, 96, 100]
>>> id(l2)
2628580501128
>>> del(l2[2])
>>> id(l2)
2628580501128
>>> l2
[12, 74, ['salam', 'mohammad', 'hastam'], 75, 96, 100]
>>> l2[1] = ''
>>> l2
[12, '', ['salam', 'mohammad', 'hastam'], 75, 96, 100]
>>> l2[1] = None
>>> l2
[12, None, ['salam', 'mohammad', 'hastam'], 75, 96, 100]
>>> l2[-3:] = [12,13,14,15,16]
>>> l2
[12, None, ['salam', 'mohammad', 'hastam'], 12, 13, 14, 15, 16]
>>> l3 = [0,0,0,0]
>>> l2[-4] = l3
>>> l2
[12, None, ['salam', 'mohammad', 'hastam'], 12, [0, 0, 0, 0], 14, 15, 16]
>>> del(l2[:])
>>> l2
[]
>>> l2 = [12, None, ['salam', 'mohammad', 'hastam'], 12, [0, 0, 0, 0], 14, 15, 16]
>>> l2 = []
>>> ;2
SyntaxError: invalid syntax
>>> l2
[]
>>> l2 = [12, None, ['salam', 'mohammad', 'hastam'], 12, [0, 0, 0, 0], 14, 15, 16]
>>> l2[:] = []
>>> l2
[]
>>> str1 = 'salam'
>>> str2 = 'bye'
>>> str1 + str2
'salambye'
>>> str1 * 2
'salamsalam'
>>> str1 ** 2
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    str1 ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> l1
['mohammad', 'salam', 3.14, 76, 23, 3.5]
>>> l3
[0, 0, 0, 0]
>>> l1 + l3
['mohammad', 'salam', 3.14, 76, 23, 3.5, 0, 0, 0, 0]
>>> l3 + l1
[0, 0, 0, 0, 'mohammad', 'salam', 3.14, 76, 23, 3.5]
>>> l3 * 2
[0, 0, 0, 0, 0, 0, 0, 0]
>>> l3 ** 2
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    l3 ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
>>> l2
[]
>>> l2 = [12, None, ['salam', 'mohammad', 'hastam'], 12, [0, 0, 0, 0], 14, 15, 16]
>>> str
<class 'str'>
>>> str1
'salam'
>>> 'l' in str1
True
>>> 'z' un str1
SyntaxError: invalid syntax
>>> 'z' in str1
False
>>> 'salam' in l2
False
>>> 0 not in l2
True
>>> 'salam' in l2[2]
True
>>> str1
'salam'
>>> str2
'bye'
>>> str1 * str2
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    str1 * str2
TypeError: can't multiply sequence by non-int of type 'str'
>>> l2
[12, None, ['salam', 'mohammad', 'hastam'], 12, [0, 0, 0, 0], 14, 15, 16]
>>> l2 + [4]
[12, None, ['salam', 'mohammad', 'hastam'], 12, [0, 0, 0, 0], 14, 15, 16, 4]
>>> l2
[12, None, ['salam', 'mohammad', 'hastam'], 12, [0, 0, 0, 0], 14, 15, 16]
>>> l2 = l2 + [4]
>>> l2
[12, None, ['salam', 'mohammad', 'hastam'], 12, [0, 0, 0, 0], 14, 15, 16, 4]
>>> l3
[0, 0, 0, 0]
>>> l3.append(5)
>>> l3
[0, 0, 0, 0, 5]
>>> id(l3)
2628580431176
>>> l3.append(10)
>>> id(l3)
2628580431176
>>> l3
[0, 0, 0, 0, 5, 10]
>>> l3 = [0 , 0]
>>> l3.append([5,6])
>>> l3
[0, 0, [5, 6]]
>>> l3.extend([5,6])
>>> l3
[0, 0, [5, 6], 5, 6]
>>> l3.extend('salam')
>>> l3
[0, 0, [5, 6], 5, 6, 's', 'a', 'l', 'a', 'm']
>>> l3.append('salam')
>>> l3
[0, 0, [5, 6], 5, 6, 's', 'a', 'l', 'a', 'm', 'salam']
>>> l3.insert(3,'mohammad')
>>> l3
[0, 0, [5, 6], 'mohammad', 5, 6, 's', 'a', 'l', 'a', 'm', 'salam']
>>> l3.remove(0)
>>> l3
[0, [5, 6], 'mohammad', 5, 6, 's', 'a', 'l', 'a', 'm', 'salam']
>>> l3.remove('z')
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    l3.remove('z')
ValueError: list.remove(x): x not in list
>>> l3.index('mohammad')
2
>>> nomre = [16,19,20,0,14,16,0]
>>> nomre.remove(0)
>>> nomre
[16, 19, 20, 14, 16, 0]
>>> nomre.remove(0)
>>> nomre
[16, 19, 20, 14, 16]
>>> del(nomre[2])
>>> nomre
[16, 19, 14, 16]
>>> l2
[12, None, ['salam', 'mohammad', 'hastam'], 12, [0, 0, 0, 0], 14, 15, 16, 4]
>>> l2.index(12)
0
>>> l2.index(12,1)
3
>>> l2.count(12)
2
>>> str1
'salam'
>>> str1.count('a')
2
>>> l2.reverse()
>>> l2
[4, 16, 15, 14, [0, 0, 0, 0], 12, ['salam', 'mohammad', 'hastam'], None, 12]
>>> l2.clear()
>>> l2
[]
>>> l2 = [3,9,0,12,4,13]
>>> l2
[3, 9, 0, 12, 4, 13]
>>> l2.sort()
>>> l2
[0, 3, 4, 9, 12, 13]
>>> l3 = [12,41,6,10,'salam','hasan',0,'5']
>>> l3.sort()
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    l3.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 'salam' > 5
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    'salam' > 5
TypeError: '>' not supported between instances of 'str' and 'int'
>>> l3 = [12,41,6,10,0]
>>> l3.sort()
>>> l3
[0, 6, 10, 12, 41]
>>> l3.reverse()
>>> l3
[41, 12, 10, 6, 0]
>>> nomrarat = [12,14,10,19,20,18]
>>> id(nomarat)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    id(nomarat)
NameError: name 'nomarat' is not defined
>>> grades = [12,14,10,19,20,18]
>>> id(grades)
2628580204232
>>> grades[0] = 14
>>> grades[1] = 16
>>> grades
[14, 16, 10, 19, 20, 18]
>>> ne_grades = grades
>>> ne_grades
[14, 16, 10, 19, 20, 18]
>>> grades
[14, 16, 10, 19, 20, 18]
>>> grades
[14, 16, 10, 19, 20, 18]
>>> temp = gardes
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    temp = gardes
NameError: name 'gardes' is not defined
>>> temp = grades
>>> temp
[14, 16, 10, 19, 20, 18]
>>> grades
[14, 16, 10, 19, 20, 18]
>>> grades[3] = 20
>>> grades
[14, 16, 10, 20, 20, 18]
>>> temp
[14, 16, 10, 20, 20, 18]
>>> copy1 = grades.copy()
>>> copy1
[14, 16, 10, 20, 20, 18]
>>> grades
[14, 16, 10, 20, 20, 18]
>>> temp
[14, 16, 10, 20, 20, 18]
>>> grades[0] = 20
>>> grades
[20, 16, 10, 20, 20, 18]
>>> temp
[20, 16, 10, 20, 20, 18]
>>> copy1
[14, 16, 10, 20, 20, 18]
>>> id(grades)
2628580204232
>>> id(temp)
2628580204232
>>> id(copy1)
2628580500936
>>> grades is temp
True
>>> copy1 is grades
False
>>> copy1 is not temp
True
>>> temp
[20, 16, 10, 20, 20, 18]
>>> copy1
[14, 16, 10, 20, 20, 18]
>>> copy1[0] = 20
>>> copy1
[20, 16, 10, 20, 20, 18]
>>> temp
[20, 16, 10, 20, 20, 18]
>>> temp is copy1
False
>>> temp == copy1
True
>>> l1 = [5,4,6]
>>> l2 = l1.copy()
>>> l1
[5, 4, 6]
>>> l2
[5, 4, 6]
>>> l1 == l2
True
>>> l1 is l2
False
>>> T1 = (12,45,12,89,0)
>>> type(T1)
<class 'tuple'>
>>> T1[0]
12
>>> T1[-3]
12
>>> T1[-4]
45
>>> T1[:-2]
(12, 45, 12)
>>> T1[-4:-2]
(45, 12)
>>> T1[0] = 100
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    T1[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> len(T1)
5
>>> Num = (5)
>>> type(Num)
<class 'int'>
>>> Name = ('hasan')
>>> type(Name)
<class 'str'>
>>> Num1 = (5,)
>>> type(Num1)
<class 'tuple'>
>>> Num2 = 2,4,8
>>> type(Num2)
<class 'tuple'>
>>> Num3 = 6,
>>> type(Num3)
<class 'tuple'>
>>> Num4 = 6
>>> l1 = [(3,4,6),[6,3],90]
>>> T2 = (12,76,(54,'salam'),'salam')
>>> type(T2)
<class 'tuple'>
>>> len(T2)
4
>>> T2[2]
(54, 'salam')
>>> T2[2][1]
'salam'
>>> T2[2][1][2]
'l'
>>> T3 = (45,63)
>>> age_ali = T3[0]
>>> age_mohammad = T3[1]
>>> (age_ali, age_mohammad)
(45, 63)
>>> T4 = ([6,4,7],)
>>> type(T4)
<class 'tuple'>
>>> age_ali = 89
>>> T3
(45, 63)
>>> T5 = ([8,7,9],12,13,14)
>>> id(T5)
2628580331176
>>> T5[0] = 3
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    T5[0] = 3
TypeError: 'tuple' object does not support item assignment
>>> T5[0][0] = 9
>>> T5
([9, 7, 9], 12, 13, 14)
>>> id(T5)
2628580331176
>>> T6 = (12,12,7,2,7,0)
>>> T6.count(12)
2
>>> T6.index(7)
2
>>> T6.index(2)
3
>>> 0 in T6
True
>>> 23 in T6
False
>>> 23 not in T6
True
>>> T6 * 2
(12, 12, 7, 2, 7, 0, 12, 12, 7, 2, 7, 0)
>>> T6 + T5
(12, 12, 7, 2, 7, 0, [9, 7, 9], 12, 13, 14)
>>> T6 ** 2
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    T6 ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'
>>> T6
(12, 12, 7, 2, 7, 0)
>>> T5
([9, 7, 9], 12, 13, 14)
>>> T7 = T6,T5
>>> T7
((12, 12, 7, 2, 7, 0), ([9, 7, 9], 12, 13, 14))
>>> D1 = {1:'salam',2:'hasan','sevvom': 80}
>>> type(D1)
<class 'dict'>
>>> T6
(12, 12, 7, 2, 7, 0)
>>> T6[0]
12
>>> D1[2]
'hasan'
>>> D1[1:2]
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    D1[1:2]
TypeError: unhashable type: 'slice'
>>> D1[-1]
Traceback (most recent call last):
  File "<pyshell#243>", line 1, in <module>
    D1[-1]
KeyError: -1
>>> D1['Sevvom']
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    D1['Sevvom']
KeyError: 'Sevvom'
>>> D1['sevvom']
80
>>> D1
{1: 'salam', 2: 'hasan', 'sevvom': 80}
>>> D1[1] = 'mohammad'
>>> D1
{1: 'mohammad', 2: 'hasan', 'sevvom': 80}
>>> l1
[(3, 4, 6), [6, 3], 90]
>>> l1[90]
Traceback (most recent call last):
  File "<pyshell#250>", line 1, in <module>
    l1[90]
IndexError: list index out of range
>>> D1[90]
Traceback (most recent call last):
  File "<pyshell#251>", line 1, in <module>
    D1[90]
KeyError: 90
>>> l1
[(3, 4, 6), [6, 3], 90]
>>> l1[90] = 78
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    l1[90] = 78
IndexError: list assignment index out of range
>>> D1[90] = 'navad'
>>> D1
{1: 'mohammad', 2: 'hasan', 'sevvom': 80, 90: 'navad'}
>>> D2 = {1:'yek', 2: 'v', 3: 'h', 1: 'salam'}
>>> D2
{1: 'salam', 2: 'v', 3: 'h'}
>>> D1 + D2
Traceback (most recent call last):
  File "<pyshell#258>", line 1, in <module>
    D1 + D2
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> D1 * 2
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    D1 * 2
TypeError: unsupported operand type(s) for *: 'dict' and 'int'
>>> del(D2)
>>> D2
Traceback (most recent call last):
  File "<pyshell#261>", line 1, in <module>
    D2
NameError: name 'D2' is not defined
>>> len(D1)
4
>>> D1
{1: 'mohammad', 2: 'hasan', 'sevvom': 80, 90: 'navad'}
>>> 'hasan' in D1
False
>>> 'navad' in D1
False
>>> 1 in D1
True
>>> 90 in D1
True
>>> D3 = {[7,5,8]:67,(45,90):'salam'}
Traceback (most recent call last):
  File "<pyshell#268>", line 1, in <module>
    D3 = {[7,5,8]:67,(45,90):'salam'}
TypeError: unhashable type: 'list'
>>> D3 = {(45,90):'salam'}
>>> D3
{(45, 90): 'salam'}
>>> D4 = {1:[45,78],2:(45,89),3:{12,56,80}}
>>> D4
{1: [45, 78], 2: (45, 89), 3: {56, 80, 12}}
>>> D4 = {1:[45,78],2:(45,89),3:{12:12,56:67,80:0}}
>>> D4
{1: [45, 78], 2: (45, 89), 3: {12: 12, 56: 67, 80: 0}}
>>> D4[3][80]
0
>>> D4[3]
{12: 12, 56: 67, 80: 0}
>>> D4[3][80]
0
>>> id(D4)
2628580490552
>>> D4[1] = 6
>>> id(D4)
2628580490552
>>> D5 = D4.copy()
>>> id(D4)
2628580490552
>>> id(D5)
2628580491056
>>> D5.clear()
>>> D5
{}
>>> D4
{1: 6, 2: (45, 89), 3: {12: 12, 56: 67, 80: 0}}
>>> D4.pop(2)
(45, 89)
>>> D4
{1: 6, 3: {12: 12, 56: 67, 80: 0}}
>>> D4.pop(100)
Traceback (most recent call last):
  File "<pyshell#289>", line 1, in <module>
    D4.pop(100)
KeyError: 100
>>> D4.pop(100,'error')
'error'
>>> D4
{1: 6, 3: {12: 12, 56: 67, 80: 0}}
>>> D4.get(100)
>>> D4.get(1)
6
>>> D4.get(100,'error')
'error'
>>> D4.setdefault(1)
6
>>> D4.setdefault(100)
>>> D4
{1: 6, 3: {12: 12, 56: 67, 80: 0}, 100: None}
>>> D4.setdefault(200,'error')
'error'
>>> D4
{1: 6, 3: {12: 12, 56: 67, 80: 0}, 100: None, 200: 'error'}
>>> D4[300]
Traceback (most recent call last):
  File "<pyshell#300>", line 1, in <module>
    D4[300]
KeyError: 300
>>> D4
{1: 6, 3: {12: 12, 56: 67, 80: 0}, 100: None, 200: 'error'}
>>> D4.keys()
dict_keys([1, 3, 100, 200])
>>> D4.values()
dict_values([6, {12: 12, 56: 67, 80: 0}, None, 'error'])
>>> D4.items()
dict_items([(1, 6), (3, {12: 12, 56: 67, 80: 0}), (100, None), (200, 'error')])
>>> obj1 = D4.keys()
>>> obj1
dict_keys([1, 3, 100, 200])
>>> type(obj1)
<class 'dict_keys'>
>>> set1 = {12,56,15,89,100}
>>> type(set1)
<class 'set'>
>>> set1.clear()
>>> set1
set()
>>> D4.clear()
>>> D4
{}
>>> set1.add(10)
>>> set1
{10}
>>> set1.add(9)
>>> set1
{9, 10}
>>> set1.remove(10)
>>> set1
{9}
>>> set1
{9}
>>> set1.add(10)
>>> set1
{9, 10}
>>> set1.add(100)
>>> set1
{9, 10, 100}
>>> set1.add([12,14])
Traceback (most recent call last):
  File "<pyshell#325>", line 1, in <module>
    set1.add([12,14])
TypeError: unhashable type: 'list'
>>> set1.add((12,15))
>>> set1
{9, 10, (12, 15), 100}
>>> set1.add('salam')
>>> set1
{(12, 15), 100, 'salam', 9, 10}
>>> set1.remove(100)
>>> set1
{(12, 15), 'salam', 9, 10}
>>> set1.remove(100)
Traceback (most recent call last):
  File "<pyshell#332>", line 1, in <module>
    set1.remove(100)
KeyError: 100
>>> set1.update('salam')
>>> set1
{(12, 15), 'a', 's', 'salam', 9, 10, 'm', 'l'}
>>> l1 = []
>>> l1.extend('SALAM')
>>> l1
['S', 'A', 'L', 'A', 'M']
>>> A = {1,2,3,4}
>>> B = {4,5,6}
>>> C = {7,8}
>>> A.isdisjoint(B)
False
>>> A.isdisjoint(C)
True
>>> D = {5,6}
>>> D.issubset(B)
True
>>> B.issubset(A)
False
>>> B.issubset(D)
False
>>> B.issuperset(D)
True
>>> A.union(C)
{1, 2, 3, 4, 7, 8}
>>> A.intersection(B)
{4}
>>> A.intersection(C)
set()
>>> A.difference(B)
{1, 2, 3}
>>> B.difference(A)
{5, 6}
>>> A.symmetric_difference(B)
{1, 2, 3, 5, 6}
>>> set2 = {1,1,1,1,1,1}
>>> set2
{1}
>>> set2.add(1)
>>> set2
{1}
>>> Num = '12'
>>> Num * 2
'1212'
>>> Num = int(Num)
>>> Num
12
>>> Num * 2
24
>>> str1 = '12a'
>>> int(str1)
Traceback (most recent call last):
  File "<pyshell#364>", line 1, in <module>
    int(str1)
ValueError: invalid literal for int() with base 10: '12a'
>>> T1 = [12,5,7,9]
>>> L1 = list(T1)
>>> L1
[12, 5, 7, 9]
>>> T1 = (12,5,7,9)
>>> L1 = list(T1)
>>> T1
(12, 5, 7, 9)
>>> L1
[12, 5, 7, 9]
>>> nomarat = [12,5,7,12,0,12,0,12]
>>> nomarat_jadid = set(nomarat)
>>> nomarat_jadid
{0, 12, 5, 7}
>>> new = list(nomarate_jadid)
Traceback (most recent call last):
  File "<pyshell#375>", line 1, in <module>
    new = list(nomarate_jadid)
NameError: name 'nomarate_jadid' is not defined
>>> new = list(nomarat_jadid)
>>> new
[0, 12, 5, 7]
>>> new1 = list(set(nomarat))
>>> new1
[0, 12, 5, 7]
>>> input('yek adad vared konid: ')
yek adad vared konid: 12
'12'
>>> Num = input('yek adad vared konid: ')
yek adad vared konid: 12
>>> Num
'12'
>>> type(Num)
<class 'str'>
>>> Num * 3
'121212'
>>> Num = input('yek adad vared konid: ')
yek adad vared konid: 12
>>> Num = int(Num)
>>> Num * 2
24
>>> Num = int(input('yek adad vared konid: '))
yek adad vared konid: 13
>>> type(Num)
<class 'int'>
>>> Num = int(input('yek adad vared konid: '))
yek adad vared konid: salam
Traceback (most recent call last):
  File "<pyshell#390>", line 1, in <module>
    Num = int(input('yek adad vared konid: '))
ValueError: invalid literal for int() with base 10: 'salam'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/P12-S2.py ==
yek adad vared konid: 13
169
Done
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/P12-S2.py ==
yek adad vared konid: 13
169
Done
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/P12-S2.py ==
yek adad vared konid: 10
100
Done
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/P12-S2.py ==
yek adad vared konid: 7
49
Done
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/P12-S2.py ==
yek adad vared konid: 5
25
Done
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/P12-S2.py ==
yek adad vared konid: 12
144
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/P12-S2.py", line 14, in <module>
    Print('Done')
NameError: name 'Print' is not defined
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/P12-S2.py ==
yek adad vared konid: 
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/P12-S2.py", line 3, in <module>
    Num = int(input('yek adad vared konid: '))
KeyboardInterrupt
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/P12-S2.py ==
yek adad vared konid: 12
yek adad digar vared konid: 2
6.0
Done
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/P12-S2.py ==
yek adad vared konid: 12
yek adad digar vared konid: 0
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/P12-S2.py", line 10, in <module>
    print(Num / Num1)
ZeroDivisionError: division by zero
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/P12-S2.py ==
yek adad vared konid: 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/P12-S2.py ==
yek adad vared konid: 12
1212
Done
>>> set1 = {2,5,9}
>>> set1.add(5)
>>> set1
{9, 2, 5}
>>> set1.add('salam')
>>> set1
{9, 2, 5, 'salam'}
>>> set1.update('salam')
>>> set1
{2, 5, 9, 'l', 'salam', 'm', 'a', 's'}
>>> 

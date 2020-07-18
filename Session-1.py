>>> Number = 5
>>> age = 25
>>> age_ali , age_mohammad = 45 , 63
>>> print(7)
7
>>> print(Number)
5
>>> print(age)
25
>>> print(age_ali)
45
>>> x1 = x2 = x3 = x4 = 0
>>> print(x1)
0
>>> print(x3)
0
>>> Number2 = -45
>>> float1 = 3.14
>>> float2 = 6.9
>>> type(Number)
<class 'int'>
>>> type(float1)
<class 'float'>
>>> complex1 = 14 + 5j
>>> complex2 = 56 - 10j
>>> type(complex1)
<class 'complex'>
>>> type(complex2)
<class 'complex'>
>>> b1 = True
>>> b2 = False
>>> type(b1)
<class 'bool'>
>>> type(b2)
<class 'bool'>
>>> s1 = None
>>> Name = mohammad
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    Name = mohammad
NameError: name 'mohammad' is not defined
>>> Name = 'mohammad'
>>> type(Name)
<class 'str'>
>>> Num = 5
>>> Num = 10
>>> Num1 = 17
>>> print(Num)
10
>>> print(Num1)
17
>>> Num + Num1
27
>>> str1 = 'salam'
>>> str2 = 'donya'
>>> str1 + str2
'salamdonya'
>>> str2 + str1
'donyasalam'
>>> Num1 + Num
27
>>> Num + str1
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    Num + str1
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> float1 = 5.6
>>> Num + float1
15.6
>>> Num1 - Num
7
>>> Num1 * Num
170
>>> Num1 / Num
1.7
>>> 12 % 5
2
>>> 12 / 5
2.4
>>> 12 // 5
2
>>> 2 ** 3
8
>>> 150 % 6
0
>>> Num1 > Num
True
>>> Num > Num1
False
>>> Num1 >= Num
True
>>> Num1 == Num
False
>>> Num1 != Num
True
\
>>> Num1 != Num
True
>>> Num1 > Num and Num1 > 0
True
>>> True and True
True
>>> False and True
False
>>> True and False
False
>>> False and False
False
>>> 












>>> Num1 > Num or Num1 < 0
True
>>> True or False
True
>>> False or True
True
>>> True or True
True
>>> False or False
False
>>> 








>>> not True
False
>>> not False
True
>>> Num2 = 3
>>> Num3 = 10
>>> Num2 = Num2 * Num3
>>> print(Num2)
30
>>> Num2 = 3
>>> Num2 *= Num3
>>> print(Num2)
30
>>> Num2 += Num3
>>> print(Num2)
40
>>> str2 = "ali"
>>> str3 = 'ali'
>>> str4 = """ali"""
>>> str5 = " 'ali'  "
>>> str6 = 'ali
SyntaxError: EOL while scanning string literal
>>> str7 = 'ali\nmohammad'
>>> print(str7)
ali
mohammad
>>> str8 = """ali
mohammad
hasan
hosein"""
>>> print(str8)
ali
mohammad
hasan
hosein
>>> str9 = 'salam donya'
>>> print(str9)
salam donya
>>> print(str9[6])
d
>>> print(str9[0])
s
>>> print(str9[23])
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    print(str9[23])
IndexError: string index out of range
>>> print(str9[4:7])
m d
>>> print(str9[4:8])
m do
>>> print(str9[:8])
salam do
>>> print(str9[4:])
m donya
>>> print(str9[4:23])
m donya
>>> len(str9)
11
>>> str9[len(str9)]
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    str9[len(str9)]
IndexError: string index out of range
>>> str9[11]
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    str9[11]
IndexError: string index out of range
>>> print(str9)
salam donya
>>> str9[0] = 'S'
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    str9[0] = 'S'
TypeError: 'str' object does not support item assignment
>>> 'S' + str9[1:]
'Salam donya'
>>> str9
'salam donya'
>>> id(str9)
1852505741360
>>> id(Num)
1661043088
>>> str9 = 'Salam Donya'
>>> id(str9)
1852505805872
>>> print(str9)
Salam Donya
>>> 'D' in str9
True
>>> 'z' in str9
False
>>> 'j' not in str9
True
>>> 'a' not in str9
False
>>> str1 = "ali
SyntaxError: EOL while scanning string literal
>>> str1 = "ali\nmohammad
SyntaxError: EOL while scanning string literal
>>> str1 = "ali\nmohammad"
>>> print(str1)
ali
mohammad
>>> str2 = """ ali






mohammad





hasan"""
>>> print(str2)
 ali






mohammad





hasan
>>> type(str9)
<class 'str'>
>>> str9.capitalize()
'Salam donya'
>>> str9
'Salam Donya'
>>> str10 = 'salam man mohammad hastam. 26 sal sen daram'
>>> str10.capitalize()
'Salam man mohammad hastam. 26 sal sen daram'
>>> 'S' + str10[1:]
'Salam man mohammad hastam. 26 sal sen daram'
>>> str10.count('a')
10
>>> str10.count('a',5,15)
2
>>> str10
'salam man mohammad hastam. 26 sal sen daram'
>>> print(str10)
salam man mohammad hastam. 26 sal sen daram
>>> str10.find('h')
12
>>> str10.find('n')
8
>>> str10.find('n',10,20)
-1
>>> str10.find('n',10)
36
>>> str10.find('Z')
-1
>>> str10.index('Z')
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    str10.index('Z')
ValueError: substring not found
>>> str10[-1]
'm'
>>> str10[-2]
'a'
>>> str11 = 'salam donya'
>>> str11[-7:-2]
'm don'
>>> str11[-7:9]
'm don'
>>> str11[4:9]
'm don'
>>> str11[-3]
'n'
>>> print(Num)
10
>>> Num
10
>>> float1
5.6
>>> l1 = [12,78,45]
>>> type(l1)
<class 'list'>
>>> l1[0]
12
>>> l1[1]
78
>>> l1[2]
45
>>> l1[89]
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    l1[89]
IndexError: list index out of range
>>> l1[-1]
45
>>> l1[-2]
78
>>> type(l1[-1])
<class 'int'>
>>> l1[:2]
[12, 78]
>>> l2 = [12,6,3,7,'salam']
>>> str1
'ali\nmohammad'
>>> str1 = 'mohammad'
>>> str1.upper()
'MOHAMMAD'
>>> str2 = 'MOHMad'
>>> str2.lower()
'mohmad'
>>> 

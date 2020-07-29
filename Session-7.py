Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from numpy import *

>>> a1 = array([1,2,4,6])
>>> a1
array([1, 2, 4, 6])
>>> type(a1)
<class 'numpy.ndarray'>
>>> a1
array([1, 2, 4, 6])
>>> a2 = array([6,3,6,8])
>>> a2
array([6, 3, 6, 8])
>>> l1 = [6,5,6,0]
>>> l2 = [4,2,4,8]
>>> l1 + l2
[6, 5, 6, 0, 4, 2, 4, 8]
>>> a1 * a2
array([ 6,  6, 24, 48])
>>> a1 + a2
array([ 7,  5, 10, 14])
>>> a1 * a2
array([ 6,  6, 24, 48])
>>> a1 ** a2
array([      1,       8,    4096, 1679616], dtype=int32)
>>> a1.dtype
dtype('int32')
>>> a1.shape
(4,)
>>> a1
array([1, 2, 4, 6])
>>> a.size
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.size
NameError: name 'a' is not defined
>>> a1.size
4
>>> a1.ndim
1
>>> a1
array([1, 2, 4, 6])
>>> a1[3]
6
>>> a1[3] = 100
>>> a1
array([  1,   2,   4, 100])
>>> a1.fill(255)
>>> a1
array([255, 255, 255, 255])
>>> a1.dtype
dtype('int32')
>>> a1
array([255, 255, 255, 255])
>>> a1[2] = 10.6
>>> a1
array([255, 255,  10, 255])
>>> a1.fill(10.6)
>>> a1
array([10, 10, 10, 10])
>>> a3 = array((3,4,6))
>>> a3
array([3, 4, 6])
>>> a4 = array([5,3,6,8,9,3,2,5,7,2])
>>> a4[1:3]
array([3, 6])
>>> a4[1:7]
array([3, 6, 8, 9, 3, 2])
>>> a4[-4:7]
array([2])
>>> a4[:4]
array([5, 3, 6, 8])
>>> a4[4:]
array([9, 3, 2, 5, 7, 2])
>>> a4[4::2]
array([9, 2, 7])
>>> a4.shape
(10,)
>>> a5 = array([[5,7,2],[1,0,4]])
>>> a5
array([[5, 7, 2],
       [1, 0, 4]])
>>> a5.shape
(2, 3)
>>> a5.size
6
>>> a5.ndim
2
>>> l3 = [[5,7,2],[1,0,4]]
>>> l3[1][1]
0
>>> a5[1][1]
0
>>> a5[1,1]
0
>>> a4
array([5, 3, 6, 8, 9, 3, 2, 5, 7, 2])
>>> b1 = a4[3,7]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    b1 = a4[3,7]
IndexError: too many indices for array
>>> b1 = a4[3:7]
>>> b1
array([8, 9, 3, 2])
>>> b1[1] = 10
>>> b1
array([ 8, 10,  3,  2])
>>> a4
array([ 5,  3,  6,  8, 10,  3,  2,  5,  7,  2])
>>> index = [1,4,7]
>>> a4[index]
array([ 3, 10,  5])
>>> a4
array([ 5,  3,  6,  8, 10,  3,  2,  5,  7,  2])
>>> a5
array([[5, 7, 2],
       [1, 0, 4]])
>>> a5[[0,1],[0,1]]
array([5, 0])
>>> a4
array([ 5,  3,  6,  8, 10,  3,  2,  5,  7,  2])
>>> where(a4 % 2 == 0)
(array([2, 3, 4, 6, 9], dtype=int64),)
>>> a4[where(a4 % 2 == 0)]
array([ 6,  8, 10,  2,  2])
>>> a4[[2,3,4,6,9]]
array([ 6,  8, 10,  2,  2])
>>> a5
array([[5, 7, 2],
       [1, 0, 4]])
>>> where(a5 % 2 == 0)
(array([0, 1, 1], dtype=int64), array([2, 1, 2], dtype=int64))
>>> a5[where(a5 % 2 == 0)]
array([2, 0, 4])
>>> a4
array([ 5,  3,  6,  8, 10,  3,  2,  5,  7,  2])
>>> a4 % 2 == 0
array([False, False,  True,  True,  True, False,  True, False, False,
        True])
>>> a4 > 3
array([ True, False,  True,  True,  True, False, False,  True,  True,
       False])
>>> l1
[6, 5, 6, 0]
>>> l1 > 4
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    l1 > 4
TypeError: '>' not supported between instances of 'list' and 'int'
>>> a5
array([[5, 7, 2],
       [1, 0, 4]])
>>> a5.shape
(2, 3)
>>> a5.reshape(3,2)
array([[5, 7],
       [2, 1],
       [0, 4]])
>>> a5
array([[5, 7, 2],
       [1, 0, 4]])
>>> a5 = a5.reshape(3,2)
>>> a5
array([[5, 7],
       [2, 1],
       [0, 4]])
>>> a5.reshape(5,2)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a5.reshape(5,2)
ValueError: cannot reshape array of size 6 into shape (5,2)
>>> a6 = array([[5,3,6],[10,4,2],[11,8,0]])
>>> a6
array([[ 5,  3,  6],
       [10,  4,  2],
       [11,  8,  0]])
>>> a6.diagonal()
array([5, 4, 0])
>>> a6.diagonal(offset = 1)
array([3, 2])
>>> a6.diagonal(offset = 2)
array([6])
>>> a6.diagonal(offset = -1)
array([10,  8])
>>> a6.diagonal(offset = -2)
array([11])
>>> 

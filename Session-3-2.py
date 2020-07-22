"""Num = int(input('yek adad vared konid: '))"""

"""
if False:
   print('positive')
   print('Done')
   print('done1')

print('kharej az body if')
"""


"""
if Num > 0:
   print('positive')

if Num < 0:
   print('negative')

print('done')
"""
"""
if Num % 2 == 0:
   print('even')

if Num % 2 != 0:
   print('odd')

print('done')
"""
"""
if Num % 2 == 0:
   print('even')
   if Num % 3 == 0:
      print('Done')
"""
"""
if Num > 0:
   print('positive')

elif Num == 0:
   print('zero')

else:
   print('negative')
"""
"""
if Num > 100:
   print('bozorgtar az 100')

elif 130 >= Num > 0:
   print('beyn 0 o 130')

elif 0 == Num:
   print('zero')

else:
   print('manfi')

"""
"""
Grades = {'Riazi1': 0, 'fizik1' : 0, 'zaban': 0, 'az1': 20}

Num = Grades['Riazi1']+ Grades['fizik1']+Grades['zaban']+Grades['az1']
GPA = Num / len(Grades)

if GPA > 12:
   print('passed')
   print(GPA)

else:
   print('failed')
   print(GPA)

"""
"""   
if not(Num % 2 == 0 and Num % 3 == 0) or Num % 5 == 0:
   print('adad mored naza ma')
"""
"""
year=int(input('please input  year milade :'))

if (year % 4 ==0 and year % 100 !=0 ) or year %400 ==0:
   print ('hast')
else :
   print ('nist')
"""
"""
while Num > 0:
   
   print(Num)
   Num -= 1
"""
"""
while Num < 100:
   print(Num)
   Num += 1
"""
"""
while Num < 100:
   if Num % 2 == 0:
      print(Num)
   Num += 1

"""
"""
l1 = []
while Num < 100:
   if Num % 5 == 0:
      l1.append(Num)
   Num += 1
"""
"""
l1 = [0,7,12,14,16,19]
cum_sum = 0

Num = len(l1)
while Num > 0:
   print(l1[Num-1])
   cum_sum += l1[Num-1]   
   Num -= 1

if cum_sum / len(l1) > 12 :
   print('passed')
   print(cum_sum / len(l1))
else:
   print('failed')
   print(cum_sum / len(l1))
"""
"""
while Num < 100:
   print(Num)
   Num += 5
"""

l1 = [45,2,7,145,6,14,90]
str1 = 'Mohammad'
set1 = {12,4,1,5}
dict1 = {1:'salam',2:'bye'}
"""
for num in l1:
   print(num)

for char in str1:
   print(char)

for i in set1:
   print(i)
"""
"""
for subset in dict1:
   print(subset)
"""
"""
for i in l1:
   l1.remove(i)
   print(i)
"""
"""
for grade in l1:
   if grade % 2 == 0:
      print(grade)
      print('even')

"""
"""
num = len(l1)

for i in num:
   print(l1[i])

"""
"""
for i in l1[3:]:
   print(i)
"""
"""
l2 = ['salam']

for i in l2[0]:
   print(i)
"""
"""
Num = len(l1)
for i in range(Num):
   print(l1[i])
"""
"""
for i in range(1,3):
   for j in range(1,3):
      print(i * j)
"""   
"""
while Num < 100:
   if Num != 90:
      print(Num)
      Num += 1
   else:
      Num += 1
   
"""
"""
while Num < 100:
   
   if Num == 90:
      Num += 1
      continue
   print(Num)
   Num += 1
"""
"""
while Num < 100:
   
   if Num == 90:
      Num += 1
      break
   print(Num)
   Num += 1
"""
"""
for i in l1:
   if i == 145:
      break
   print(i)
"""

for i in l1:
   if i == 145:
      pass
else:
   print('done')

"""
num = 10
while num > 0:
   if num == 5:
      num -= 1
      continue
   print(num)
   num -= 1

else:
   print('done')
"""


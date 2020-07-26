
#def function1():
#	""" in tebe vorudi nemigire
#komak mikone ke ebarat salam chap beshe"""
#	print('salam')
"""

def function2(arg):
   print(arg)


def function3(arg1,arg2):
   print(arg1 ** arg2)


def function4(arg1, arg2 = 10):
   print(arg1 / arg2)


def function5(t1):
   result = 0
   for sub in t1:
      result += sub
   print(result)

def function6(*arg):
   result = ()
   for sub in arg:
      result += sub
   print(result)


def function7(arg2, *arg,):
   print(arg2 * arg)


def function8(arg1,arg2):
   if arg1 % arg2 == 0:
      print('bakhshpazir')
   else:
      print('nistan')

def function9(arg):
   for i in range(2,int(arg**0.5)):
      if arg % i == 0:
         print('aval nist')
         break
   
   else:
      print('aval')

def function10(arg1, arg2):
   print(arg1 - (arg1 // arg2) * arg2)

def function11(arg):
   result = 1
   for i in range(2,arg+1):
      result *= i
   print(result)


def function12(arg):
   num = arg ** 2
   return num

def function13(arg):
   print(arg ** 2)


def function14(arg1, arg2):
   return arg1 ** arg2 , arg2 ** arg1

def function14():
   print('salam')

def function15(arg):
   if arg == 1:
      return 1
   elif arg < 1:
      print('vorudi dorost nist')
   else:
      return arg * function15(arg-1)

"""
def function16(arg):
   if arg <= 0:
      print('error')

   elif arg == 1 or arg == 2:
      return 1
   else:
      return function16(arg-1) + function16(arg-2)
"""

def function17(arg):
   if arg >= 0:
      return 'positive'
   return 'negative'

"""
"""
def func():
   print('salam')
   
try:
   day = int(input('day'))
   month = int(input('month'))
   year = int(input('year'))
   day ** 2

except ZeroDivisionError:
   print('taghsim bar sefr rokh dade')

except TypeError:
   print('type error')
except (NameError, RuntimeError):
   func()

except:
   func()
"""
"""
try:
   int('s')
   print('badaneye try')

except:
   print('error')

else:
   print('done')

print('code ejra shode')

"""
def date(day,month,year):
   
   return 61
   
   
   

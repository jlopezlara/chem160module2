Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from random import choices
>>> nrolls=10000
>>> total=0
>>> ndice=2
>>> for i in range(nrolls):
	dice=choices(range(1:7),k=ndice)
	
SyntaxError: invalid syntax
>>> 	dice=choices(range(1 : 7),k=ndice)
	
SyntaxError: unexpected indent
>>> dice=choices(range(1 : 7),k=ndice)
SyntaxError: invalid syntax
>>> dice.sort(reverse=True)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dice.sort(reverse=True)
NameError: name 'dice' is not defined
>>> total=total+dice[0]+dice[1]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    total=total+dice[0]+dice[1]
NameError: name 'dice' is not defined
>>> print("Average roll=",total/nrolls)
Average roll= 0.0
>>> 

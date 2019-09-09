Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from random import choice
>>> trials=100
>>> steps=1000
>>> gothome=0
>>> for i in range(trials):
	point=0
	for step in range(steps):
		point+=choice((-1,1))
		if point==0:
			gothome+=1
			break
print("Franction that got home=",gothome/trials)
SyntaxError: invalid syntax
>>> Print("Fraction that got home=",gothome/trials)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    Print("Fraction that got home=",gothome/trials)
NameError: name 'Print' is not defined
>>> for i in range(trials):
	point=0
	for step in range(steps):
		point+=choice((-1,1))
		if point==0:
			gothome+=1
			break
print("Franction that got home=",gothome/trials)
SyntaxError: invalid syntax
>>> for i in range(trials):
	point=0
	for step in range(steps):
		point+=choice((-1,1))
		if point==0:
			gothome+=1
			break
			print("Franction that got home=",gothome/trials)

			
>>> 

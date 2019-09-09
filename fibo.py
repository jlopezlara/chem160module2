Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> Prev2=0
>>> Prev1=1
>>> fori in range (20):
	
SyntaxError: invalid syntax
>>> for i in range (20):
	current=Prev2+Prev1
	print (current)
	Prev2,Prev1=Prev1,current
	

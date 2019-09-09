Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random, math
>>> inside=0
>>> ntrials=1000
>>> for i in range(ntrials):
	x=random.random()
	y=random.random()
	if (x*x+y*y)<1.0:
		inside+=1
pi=4.*inside/ntrials
SyntaxError: invalid syntax
>>> Pi=4 *inside/ntrials
>>> print("N=%d Error=%8.5f"%(ntrials, Pi-math.Pi))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print("N=%d Error=%8.5f"%(ntrials, Pi-math.Pi))
AttributeError: module 'math' has no attribute 'Pi'
>>> print("N=%d Error=%8.5f "% (ntrials, pi-math.pi))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print("N=%d Error=%8.5f "% (ntrials, pi-math.pi))
NameError: name 'pi' is not defined
>>> 

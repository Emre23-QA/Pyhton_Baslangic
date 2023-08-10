Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> format()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    format()
TypeError: format expected at least 1 argument, got 0
>>> A=5
>>> print('A.:','A')
A.: A
>>> print('A.:',A)
A.: 5
>>> print("a{0}".format(A))
a5
>>> print("a={0}".format(A))
a=5
>>> print (f"A={A}")
A=5
>>> print ('A='+str(A))
A=5

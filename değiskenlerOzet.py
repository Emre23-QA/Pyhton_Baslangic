Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> X=Y=Z="BTK"
>>> type(X)
<class 'str'>
>>> i=0
>>> j=0
>>> i=i+j
>>> i+=j
>>> B=0
>>> C=0
>>> C=5
>>> B,C=C,B
>>> print(B)
5
>>> t=20+15-10
>>> x=t/4+7
>>> print(x)
13.25
>>> import keywords
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    import keywords
ModuleNotFoundError: No module named 'keywords'
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> B=40
>>> C=str(B)+'5'
>>> print(C)
405
>>> type(C)
<class 'str'>
>>> type(C)
<class 'str'>
>>> type(C) # c değişkeni veri tipi bul
<class 'str'>

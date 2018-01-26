#!usr/bin/env python
# _*_ coding: utf-8 _*_

'''
#输出
print('linkpark','chainsmokers','coldplay','greenday')

print('100 + 333 = ',100+333)

#输入
name=input('please enter your name!\n')
#name=input(b'please enter your name!\n')
print('my name is:',name)
'''
'''
#转义字符\
print('i\'m ok!')
print('\\\n\\')
print('\\\\')
'''

#多行换行  r不进行转义
#print('''line1 \n
#line2
#line3''')
#print(r'''line1 \n
#line2
#line3''')

'''
#boolean值，常用于条件判断
print(3>2)
print(True and False)
print(True and True)
print(True or False)
print(False or False)
print(not True)

#eg:
age=input('please enter yout age！\n')
if int(age)>18:
	print('your are adult!')
else:
	print('my boy young child')
'''

'''
#空值None,不等于数值0
print(0 is None)
'''

'''
#变量
a='ABC'
b=a
a='DEF'
print(b)
#注意 赋值 = 和 等于 == 的区别
#a --> 'ABC'
#b --> 'ABC'
#a --> 'DEF'
'''

'''
#常量
PI=3.12159265359
print('PI=',PI)
print('10/3=',10/3)
print('10/5=',10/5)
print('10//5=',10//5)
print('10%3=',10%3)
'''

'''
#str的编码
print('A:',ord('A'))
print('城:',ord('城'))
print('66:',chr(66))
print('22479:',chr(22479))
print('ABC:','ABC'.encode('ascii'))
print('你好:','你好'.encode('utf-8'))
#print('你好'.encode('ascii'))  notice：含中文的str不能用ascii来编辑码
print("b'ABC':",b'ABC'.decode('utf-8'))
print(r"b'\xe4\xb8\xad\xe6\x96\x87':", b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(r"b'\xe4\xb8\xad\xff':",b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))
print("len('ABC'\):",len('ABC'))
print("len('世界'):",len('世界'))
print("len('世界').encode('utf-8'):",len('世界'.encode('utf-8')))
'''

'''
#占位符 格式转换
print('hello! my name is %s, %d books,$%.2f' %('solaris',2,3456.789))
print('%02d' %2)
print('hello! my name is {0},I have ${1:.2f}'.format('百岁山',	123.456))
'''

'''
print('世界'.encode('gb2312'))
print('世界'.encode('utf-8'))
'''

'''
#list
color=['pink','blue','green']
print('color length:',len(color))
for x in range(0,len(color)):
	print(color[x])
	print(color[-x])
color.append('yellow')
print(color[len(color)-1])
color.insert(2,'red')
for x in range(0,len(color)):
	print(color[x])
print('*******************')
color.pop(1)
for x in range(0,len(color)):
	print(color[x])

list1=['apple',23.3,True]
print(list1)
'''

'''
#tuple
color=('pink','blue','green')
print(color[-2])
#创建'会变'的tuple
'''

#条件判断


#循环判断

'''
#dict
d={'pink':1,'green':2,'yellow':3}
print(d['green'])
print("'red' in d:",'red' in d)
print(d.get('green'))
print(d.get('red'))
print(d.get('red',-1))
print(d.pop('green'))
print(d)
'''

'''
#set
s=set([1,2,2,2,3])
print(s)
s.add(4)
print(s)
s.remove(2)
print(s)
print('********************')
s1=set([1,2,3])
s2=set([2,3,4])
print('s1&s2 =',s1&s2)
print('s1|s2 =',s1|s2)
'''

'''
#不可变对象
#list 可变对象
a=['c','b','a']
print(a)
a.sort()
print(a)
print('*****************')
#str 不可变对象
s='abc'
s2=s.replace('a','A')
print(s)
print(s2)
'''

'''
#函数
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operat type')
	if x >= 0:
		return x
	else:
		return -x
'''

'''
import math

print('pi:',math.pi)
'''

'''
#位置参数
def power(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

print('power(3,5):',power(3,5))
'''

'''
#默认参数
def my_power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

print('my_power(8):',my_power(8,3))
'''

'''
#!!!
def add_end(L=[]):
	L.append('end')
	return L

print('add_end()1:',add_end())
print('add_end()2:',add_end())
print('add_end()3:',add_end())

def add_end_modife(L=None):
	if L is None:
			L=[]
	L.append('end')
	return L

print('add_end_modife()1:',add_end_modife())
print('add_end_modife()2:',add_end_modife())
print('add_end_modife()3:',add_end_modife())
'''

'''
#可变参数
def sum_numbers(numbers):
	sum=0
	for n in numbers:
		sum=sum+n
	return sum

print('sum_numbers()-list:',sum_numbers([1,2,3]))
print('sum_numbers()-tuple:',sum_numbers((1,2,3)))	
l=[1,2,3]
#print('sum_numbers(*l):',sum_numbers(*l))

def sum_cal(*numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum

print('sum_cal(*numbers):',sum_cal(1,2))

def sum_three(a,b,c):
	sum=a+b+c
	return sum
l=[1,2,3]
print('sum_three(*l):',sum_three(*l))
'''

'''
#关键字参数
def person1(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

person1('yw',24,city='hangzhou',job='none')	

def person2(name,age,*,city,job):
	print('name:',name,'age:',age,'city:',city,'job:',job)

person2('yw',24,city='hangzhou',job='none')	
person2('ys',14,'nanjing','wda')	
'''

'''
python的参数总结
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''

'''
def fact(n):
	if n == 1:
		return 1
	return n*fact(n-1)

print('fact():',fact(998))
'''

'''
#尾递归
def fact_iter(num,sum):
	if num ==1:
		return sum
	return fact_iter(num-1,sum*num)

def fact2(n):
	return fact_iter(n,1)

print('fact2():',fact2(1000))
'''

'''
#汉若塔
def move(n,a,b,c):
	if n==1:
		print(a,'-->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)
move(4,'a','b','c')
'''

'''
#切片
color=['pink','blue','yellow','red','green']
print('color[0:3]:',color[2:3])
print('color[-4:-2]:',color[-4:-2])

list=list(range(100))
print('list:',list)
print('list[::5]:',list[::5])
print('list[:]:',list[:])

tuple=tuple(range(11))
print('tuple:',tuple)
print('tuple[::2]:',tuple[::2])

str='abcdefg'
print('str[::2]:',str[::2])
'''

'''
def trim(s):
	while s[:1]==' ':
		s=s[1:]
	while s[-1:]==' ':
		s=s[:-1]
	return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
'''

'''
#迭代
d={'a':1,'b':2,'c':3}
for key in d:
	print('key:',key)
for value in d.values():
	print('value:',value)
for k,v in d.items():
	print('key:value-->',k,':',v)

from collections import Iterable

print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance((1,2,3),Iterable))

for i,value in enumerate(['a','b','c']):
	print('i:value-->',i,value)
for x,y in [(1,1),(2,4),(3,9)]:
	print('x,y:',x,y)

def find_min_and_max(l):
	if l == []:
		return (None,None)
	min=max=l[0]
	for i in l:
		if i<min:
			min=i
		elif i>max:
			max=i
	return (min,max)

# 测试
if find_min_and_max([]) != (None, None):
    print('测试失败!')
elif find_min_and_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_and_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
'''

'''
#列表生成式
list=list(range(1,11))
print('list:',list)

L=[]
for x in range(1,11):
	L.append(x*x)
print('L:',L)

print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x%2==0])
print([m+n for m in 'abc' for n in 'xyz'])

import os
print([d for d in os.listdir('.')])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
'''

'''
#生成器 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
g=(x*x for x in range(1,11))
print(g)
for n in g:
	print(n)

def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n += 1
	return 'Done'
f=fib(6)
print('f:',f)
for n in f:
	print(n)
'''

'''
def odd():
	print('step 1')
	yield(1)
	print('step 2')
	yield(3)
	print('step 3')
	yield(5)
o=odd()
print('1:',next(o))
print('2:',next(o))
print('3:',next(o))
print('4:',next(o))	

def triangles():

    L=[1]
    while True:
        yield L
        L=[x+y for x,y in zip(L+[0],[0]+L)]

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
'''

'''
#迭代器
from collections import Iterable
print(isinstance([1,2],Iterable))
print(isinstance({},Iterable))
print(isinstance((),Iterable))
print(isinstance('abc',Iterable))
print(isinstance(100,Iterable))
'''

'''
#高阶函数
print(abs)
f=abs
print('f:',f(-12.23))


def add(x,y,f):
	return f(x)+f(y)
print(add(-2,3,abs))
'''

'''
def f(x):
	return x * x

r=map(f,range(1,11))
print(list(r))
'''
'''
from functools import reduce
def fn(x,y):
	return x*10+y

print(reduce(fn,[1,3,5,6,2]))
'''

'''
def normalize(name):
   return name[:1].upper()+name[1:].lower()
   #return name.capitalize()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
'''

'''
from functools import reduce	
def prod(L):
	return reduce(lambda x,y:x*y,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
'''

'''
from functools import reduce

number={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def str_int(s):
	return number[s]
def int(s):
	return reduce(lambda x,y:10*x+y,map(str_int,s))
def str2float(s):
	l=s.split('.')
	return int(l[0])+int(l[1])/(10**len(l[1]))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
'''

'''
def not_empty(s):
	return s and s.strip()

f=filter(not_empty, ['A', '', 'B', None, 'C', '  '])
print(list(f))
'''
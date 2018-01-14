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
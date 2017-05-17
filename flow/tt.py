
# a is b ==>id(a)==id(b)
import operator

a = 4.3
b = 1.3+3.0
print( a == b) #True
print( a is b) #False
print(id(a)) #3054691033496
print(id(b)) #3054691033616
x=10.0
y=10.0
z=10
print(id(x)) #2644910350864
print(id(y)) #2644910350864
print(id(z)) #1463461248
print( x is y) #True
print( x is z) #False
print( x == z) #True

#not
print(not (x is z))#True

# and or
print(x>5.0 and x<15.0) #True
print(x<5.0 or x>15.0) #False

#type
e = 100001554884514
print(type(e)) #<class 'int'>
print(type(x)) #<class 'float'>
string1="adgddd"
print(type(string1)) #<class 'str'>
print(type(0+0j)) #<class 'complex'>
print(type([])) #<class 'list'>
print(type({})) #<class 'dict'>
print(type(type)) #<class 'type'>

class Foo:pass
foo = Foo()

class Bar(object):pass
bar = Bar()

print(type(Foo))#<class 'type'>
print(type(foo))#<class '__main__.Foo'>
print(type(Bar))#<class 'type'>
print(type(bar))#<class '__main__.Bar'>
print(isinstance(foo,Foo))


i,j = -4,12
print(operator.lt(i, j))
print(operator.__lt__(i, j))



students = ['dave', 'john', 'jane']
grades = {'john': 'F', 'jane':'A', 'dave': 'C'}
print(sorted(students, key=grades.__getitem__))

array1 = [5, 2, 3, 1, 4]
print(sorted(array1))
print(array1)
array1.sort()
print(array1)

array2 ={4: 'E',1: 'D', 2: 'B', 3: 'B',  5: 'A'}
print(sorted(array2))

print(sorted("This is a test string from Andrew".split(),key=str.lower))

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
#reverse参数很好理解，如果reverse=True，将以降序排序
print(sorted(student_tuples, key=lambda student: student[2],reverse=True))
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]



from operator import itemgetter, attrgetter, methodcaller

print(sorted(student_tuples, key=itemgetter(2)));
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
print( sorted(student_tuples, key=itemgetter(1,2)))#多级
#[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

messages = ['critical!!!', 'hurry!', 'standby', 'immediate!!']
print(sorted(messages, key=methodcaller('count', '!')))

str2 ="1234jjd"
print(str(str2))
print(repr(str2))
print(eval(repr(str2)))
print(str2 == eval(repr(str2)))



# a is b ==>id(a)==id(b)
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
str="adgddd"
print(type(str)) #<class 'str'>




x = 10; 
y = 15
print(x + y)
print(x)
# This is a single line comment
'''
This 
is 
muliblt 
line comment
'''
# if statement
x = 20
if x<y:
    print('x is smaller')
elif x==y:
    print('x is equal y')
else:
    print('y is smaller')

# function In Python 
def function_name():
    print(x)
    print('X into function')
function_name()

# list
mylist1 = ['ahemd', 'sara', 1, True, 1]
print(mylist1) 
print(mylist1[0]) 
# print(mylist1[4]) # Error
print(mylist1[-1])
print(mylist1[1:3])
print(mylist1[1:4:1])
print(mylist1[1:4:2])
print(mylist1[1:])
print(mylist1[:3])
# list methods 
mylist1.append('end')
print(mylist1)
mylist2 = ['a','b', 'c']
mylist1.extend(mylist2)
# print(mylist1 + mylist2)
print(mylist1)
print(mylist2)
mylist1.remove(1) # first match
print(mylist1)
# mylist1.remove(2) # ValueError: list.remove(x): x not in list
mylist3 = [5, 4, 6, 1, -1]
# mylist4 = [5, 4, 6, 1, -1, 'ahmed']
mylist5 = ['B', 'Z', 'A', 'N']
mylist5.sort()
print(mylist5)
mylist3.sort()
# mylist4.sort() # TypeError: '<' not supported between instances of 'str' and 'int'
# mylist3.sort(reverse=True)
print(mylist3)
# reverse()
mylist3 = [-1, 1, 4, 5, 6, 'ahmed', True, False]
mylist3.reverse()
print(mylist3)
# clear()
mylist3.clear()
print(mylist3)
# copy()
mylist3 = mylist1.copy()
print(mylist3)
# count()
mylist1.extend(mylist2)
print(mylist1)
print(mylist1.count('a')) # 2
# len()
print(len(mylist1))
# index()
print(mylist1.index('a')) # 5
# pop()
print(mylist1.pop()) # c
print(mylist1)
mylist1.pop()
print(mylist1)

# value1 = input('Enter your name: ')
# value2 = int(input('Enter your age: '))
# print(type(value1))
# print(type(value2))

# Tuple
mytuple1 = ('ahmed', 'sara', 1, True, 1)
mytuple2 = 'ahmed', 'sara', 1, True, 1
print(type(mytuple2))
# mytuple3 = ('ahmed',) # tuple one element
# print(type(mytuple3))
print(mytuple1[1]) # sara
print(mytuple1[-1]) # 1
mytuple1 = ('ahmed', 'sara', 1, True, 1, mylist2)
print(mytuple1[-1][-1]) # c
# count()
print(mytuple1.count(1)) # 3
mytuple3 = (1, 22, 30, 4, -5 , 106, 7, 8, -9)
# mytuple3.sort() # AttributeError: 'tuple' object has no attribute 'sort'
# tuple destruct
a = ('A', 'B', 'C', 'D')
j,k,z,_ = a
print(j)
print(k)
print(z)

# Set
myset1 = {1,'ahmed', 'sara', 1, True, 1}
print(myset1)
# myset2 = {'ahmed', 'sara', 1, [1, 2, 3]}
# print(myset2) #TypeError: unhashable type: 'list'

b = (1,2,3,4,5,6)
print('The position of index is: {:d}'.format(b.index(4)))
print(f'The position of index is: {b.index(4)}')


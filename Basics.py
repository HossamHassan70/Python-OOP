# Define varible
x = 10; h=6  # simecolan is optional (end of statement)
y,f,g = 15,10,7 # multiple assignment 
y = x = 4 # assign the same value to multiple variables
print("this is "+str(x + y)) # convert int to string using str()
print(x)
print(type(x))
print(f'this is {x}') 
print('this is {:d}'.format(x)) 
# This is a single line comment
'''
This 
is 
muliblt 
line comment
'''
print('This is \
How can \
write multi line of string without error')

# if statement
x = 20
if x<y:
    print('x is smaller')
elif x==y:
    print('x is equal y')
else:
    print('y is smaller')

if x >=5:
    print("ex")
elif x >=3 and x<=4:
    print("good")
elif x >= 2 and x<=2.99:
    print ("bad")
# ================================
# function In Python 
def function_name():
    print(x)
    print('X into function')
function_name()

# ================================
# list
# 1. List Items Are Ordered, Index and Slice 
# 2. List Items Are Mutable (changeable) ==> add, remove, change
# 3. List Allows Duplicate Values (Items Not Unique)
# 4. List Items Are Enclosed in Square Brackets []
# 5. List can have any data type
mylist1 = ['ahemd', 'sara', 1, True, 1]
print(mylist1) 
print(mylist1[0]) # ahemd
# print(mylist1[45]) # Error out of range
print(mylist1[-1]) # 1
print(mylist1[1:3]) # ['sara', 1] last index not included
print(mylist1[1:4:1]) # ['sara', 1, True] 
print(mylist1[1:4:2]) # ['sara', True] step 2
print(mylist1[1:])
print(mylist1[:3])

# list methods 
mylist1.append('end') # add to the end of the list
print(mylist1) # ['ahemd', 'sara', 1, True, 1, 'end']
mylist2 = ['a','b', 'c']

mylist1.extend(mylist2) # add list to the end of the list
# print(mylist1 + mylist2)
print(mylist1) # ['ahemd', 'sara', 1, True, 1, 'end', 'a', 'b', 'c']
print(mylist2) # ['a', 'b', 'c']

mylist1.remove(1) # remove the first occurance of the value
print(mylist1) # ['ahemd', 'sara', True, 1, 'end', 'a', 'b', 'c']
# mylist1.remove(2) # ValueError: list.remove(x): x not in list

mylist3 = [5, 4, 6, 1, -1]
# mylist4 = [5, 4, 6, 1, -1, 'ahmed']
mylist5 = ['B', 'Z', 'A', 'N']
mylist5.sort() # sort the list in ascending order
print(mylist5) # ['A', 'B', 'N', 'Z']
mylist3.sort() 
# mylist4.sort() # TypeError: '<' not supported between instances of 'str' and 'int'
# mylist3.sort(reverse=True)
print(f'This is list3 : {mylist3}')

# insert()
mylist3.insert(1, 'ahmed') # insert value at index 1
print(mylist3) # [1, 'ahmed', 4, 5, 6, 'ahmed', True, False]

# reverse()
mylist3 = [-1, 1, 4, 5, 6, 'ahmed', True, False]
mylist3.reverse() # reverse the list
print(mylist3)

# clear()
mylist3.clear() # clear the list 
print(mylist3)

# copy()
mylist3 = mylist1.copy() # copy the list to another list 
print(mylist3)

# count()
print(mylist1) # ['ahemd', 'sara', True, 1, 'end', 'a', 'b', 'c']
mylist1.extend(mylist2)
print(mylist1) # ['ahemd', 'sara', True, 1, 'end', 'a', 'b', 'c', 'a', 'b', 'c']
print(mylist1.count('a')) # 2 (count the number of 'a' in the list)

# len()
print(len(mylist1)) # 11 (count the number of elements in the list)

# index()
print(mylist1.index('a')) # 5 (return the index of the first occurance of 'a')

# pop()
print(mylist1.pop()) # c (remove the last element in the list)
print(mylist1) # ['ahemd', 'sara', True, 1, 'end', 'a', 'b', 'c', 'a', 'b']
mylist1.pop() # remove the last element in the list 'b'
print(mylist1) # ['ahemd', 'sara', True, 1, 'end', 'a', 'b', 'c', 'a']

# value1 = input('Enter your name: ') # string get from the user
# value2 = int(input('Enter your age: ')) # integer get from the user
# print(type(value1))
# print(type(value2))
# ================================
# Tuple
# 1. Tuple Items Are Ordered, Index and Slice
# 2. Tuple Items Are Immutable (unchangeable) ==> can't add, remove, change
# 3. Tuple Allows Duplicate Values (Items Not Unique)
# 4. Tuple Items Are Enclosed in Parentheses () you can use without ()
# 5. Tuple can have any data type
# 6. Tuple can have one element with comma
mytuple1 = ('ahmed', 'sara', 1, True, 1) 
mytuple2 = 'ahmed', 'sara', 1, True, 1
print(type(mytuple2))
# mytuple3 = ('ahmed',) # tuple one element
# print(type(mytuple3))
print(mytuple1[1]) # sara
print(mytuple1[-1]) # 1
mytuple1 = ('ahmed', 'sara', 1, True, 1, mylist2)
print(mytuple1[-1][-1]) # c

# tuple methods
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

# ================================
# Set
# 1. Set Items Are Unordered, Not Indexed, No Slice
# 2. Set Items Are Mutable But it has only Immutable data type (Numbers, Strings, Tuples) List and dict are NOT
# A set itself may be modified, but the elements contained in the set must be of an immutable type.
# 3. Set Items Are Unique (No Duplicate Values)
# 4. Set Items Are Enclosed in Curly Braces {}
# 5. Set can have any data type

myset1 = {1,'ahmed', 'sara', 1, True, 1}
myset2 = {'one', 'two', 'three'}
myset3 = {1,2,3,4}
print(myset1)
# print(myset2 | myset3)
print(myset2.union(myset3))
# myset2 = {'ahmed', 'sara', 1, [1, 2, 3]}
# print(myset2) #TypeError: unhashable type: 'list'

b = (1,2,3,4,5,6)
print('The position of index is: {:d}'.format(b.index(4)))
print(f'The position of index is: {b.index(4)}')

# ================================
# Dictionary
mydict1 = {
        'name':'ahmed',
        'age': 25,
        'grade': 'A',
        (1,2): 'tuple',
        'name':'sara' # duplicate key (the last value will be saved)
}
print(f'This is my Dict1{mydict1}') 
print(mydict1['name']) # sara
print(mydict1.keys()) # dict_keys(['name', 'age', 'grade', (1, 2)])
print(mydict1.values()) # dict_values(['sara', 25, 'A', 'tuple'])

# range()
print(range(10)) # range(0, 10)

for i in range(10): # 0 to 9 (10 not included)
    print(i)

# print(dir(int))

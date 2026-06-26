# a = int (input("enter first number"))
# b = int (input("enter second number"))
# sum = a+b
# print(sum)

# x = "10.15"
# print(x)== 10.15
# print(str(x))


# x=20.5
# y='abc'
# z=20

# print(str(y)) #abc

# print(int(y)) # conversion error

# print(float(x)) #20.5
# print(float(z)) #20.5

# #======================

# text = 'abc'
# print(int(text)) #conversion error

# # conclusion: number can done type conversion but string cannot be a number

# name= 'Yamuna'
# age= 20
# gpa=3.714

# print(f'{name} is {age} years old.')
# print(f'GPA: {gpa:.2f}') #.2f=2 decimal places
# print(f'10 squared = {10 ** 5}')
# print(f'Is adult: {age>=19}')

# def greet (name):
#     """Return a greeting string for the given name."""
#     return f'Hello,{name}!'
# print(greet('Yamuna'))
# print(greet.__doc__)

# name= input('Your name:')
# weight= float (input('Weight in kg:'))
# height= float(input('Height in m:'))

# bmi= weight/height ** 2
# print(f'\n{name}, Your BMI is{bmi:.1f}')
# print('(Healthy range: 18.5 to 24.9)')
# %= modulus
# //=floor division


# a= input('first number')
# b= input('second number')
# print (a // 7)

# year = int(input("Enter a year:"))
# if(year%4 == 0 and year % 100 !=0) or (year% 400 == 0):
#     print (f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# sum = 0

# sum += 1 #same as: sum = sum+1
# print(sum) #1

# sum +=1
# print(sum)

# sum *= 10
# print(sum) #20

# sum //= 3
# print(sum) #6

# sum **=2
# print(sum)

# sum=+ 2
# print(sum)

# sum=- 5
# print(sum)

# sum=* 5
# print(sum)

# sum=// 7
# print(sum)

#basic arithmetic 
# a= 20
# b= 6
# print (a+b)
# print (a-b)
# print (a*b)
# print (a/b)

#floor divison and modulo
# print(17//5) #(3*5=15, rem 2)
# print(17 % 5) #2 (the leftover)
# #floor division flooers towards -infinity, not toward zero
# print(-17 // 5) #(not -3!)
# print(-17 % 5) #(because -4*5+3=-17)

#exponentiation 
# print(2**10)
# print(9**0.5)#square root of 9 --> 3.0
# print(2**-1) #0.5(negative exponent=reciprocal)

#string concatenation and repetition

# first = 'hello'
# second = 'world'
# greeting = first + second #concatenation
# print(greeting)

# line = '_'*20 #repetition
# print(line)
# #you cannot mix string with string and number with +
# # print('age:'+25)#typeerror!
# print('age:' + str(25))#fix:convert to str first

#list concatenation and repetition

# a=[1,2,3]
# b=[4,5,6]
# print(a+b)#concatenation
# print(a*3)#repetition

# #comparing numbers and strings
# print(10==10.0) #true(int and float equal in value)
# print(3>2)#true
# #string compared lexicographically(by unicode code point)
# print('apple'<'banana')#true('a'<'b)
# print('Zoo'<'apple')#true('z'=90<'a'=97)

#chained comparison
# x=5
# print(0<x<10)#true x is between 0 and 10
# print(1<=x<=5)#true
# print(10<x<20)#false x is not in that range
# #useful in input validation
# age = 65
# if 18<=age<=65:
#     print('working age')

#logical operators
#truth table and/or/not
# print(True and True)
# print (True and False)
# print(False and True)
# print(False and False)

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# print(not True)
# print(not False)

#short circuit evaluation
# and short circuits: right side skipped when left is False
# x=0
# result = x !=0 (10 / x > 1) 
# print (result)

# #or short circuit: right side skipped when left is true
# name='something'
# default=name or 'unknown'
# print(default)

# #key insight: and/or return an OPERAND, not always bool
# print(0 or 'x')
# print(5 or 'x')
# print(0 and 'x')

#identify vs equality

# a = [1,2,3]
# b = [1,2,3]
# c = a
# print(a==b)
# print(a is b)
# print(a is c)

#small integer caching gotcha
# x = 100
# y = 100
# print(x is y)

# x = 1000
# y = 1000
# print(x is y)
# print(x==y)

# idiomatic non check using is
# value=None
# if value is None:
#     print('No value provided')
# if value is not None:
#     print('value exists:', value)

#membership operators on strings, list, and dicts

# print('py' in 'python')
# print('z' not in 'python')

# nums = [10, 20, 30, 40]
# print(20 in nums)
# print(99 not in nums)

# info = {'name':'hii', 'age':30}
# print('name' in info)
# print('hii' in info)
# print('hii' in info.values())

# bitwise operations with bin() output

# a=0b1010
# b=0b1100
# print(bin(a&b))
# print(bin(a|b))
# print(bin(a^b))
# print(~a)

# #shift operators
# x=1
# print(x<<3)
# print(64>>4)

# n=42
# print(n&1)

#without parentheses -- precedence riles apply
# print(2+3*4)
# print(10-2**3)
# print(True or False and False)

# #with parentheses -you control the order
# print((2+3)*4)
# print((10-2)**3)

#classic beginner surprise
# x=1
# y=2
# z=3
# print(x==1 or y==2 and z==9)
# #'and' binds tighter than 'or', so this is:
# #x==1 or (y==2 and z==9)
# #True or (True and False)
# #True or False
# #True
# #if you meant (x==1 or y==2) and z==9- add parens!
# print((x==1 or y==2) and z==9)

#expression -- produce a value 
# x= 3+4
# y= len('hello')

#statements -- perform actions
#x=5 is a statement (assignment); you cannot write:
#if(x=5):

#without walrus -- process reads twice or needs extra variable
# import random
# value = random.randint(1,10)
# while value !=5:
#     print('Got:', value)
#     value= random.randint(1,10)
# #with walrus -- cleaner: assign and test in one expression
# import random
# while(value:=random.randint(1,10)) != 5:
#     print('Got:',value)
#     print('Found 5!')

#another common use: avoid calling an expensive function twice
# data=[1,2,3,4,5,6,7.8,9,10]
# evens= [y for x in data if(y:=x*2)>8]
# print(evens)



#class-task

#in with string (checks for substrings)
# print('py' in 'python')
# print('z' not in 'python')

# #in with lists
# nums=[10,20,30,40]
# print(40 in nums)
# print(77 not in nums)
# #in with dicts- checks keys, not values
# info={"name": "alice", "age": 30}
# print("name" in info)
# print("alice" in info)
# print("alice" in info.values())


#without walrus- process reads twice or needs extra variables
# import random
# value = random.randint(1,10)
# while value!= 5:
#     print('Got:', value)
#     value=random.randint(1,10)

#with walrus - cleaner: assign and test in one expression
# import random
# while(value:= random.randint(1,10)) !=5:
#     print('Got:', value)
#     print("Found 5!")

#str('')--use to convert in string
# '''"""" -- use cases: poem
# "" -- text
# '' -- name 
# s = "hello"
# new_s = "H" + s[1:]
# print(new_s)
# print(s)

# s = "python Rocks"

# print(s[0:6])
# print(s[::4])
# print(s[::-1])
# print(s[:6])
# print(s[7:12:2])
# print(s[7:])

# for ch in "China!":
#     print(ch)

# s = "hello world"
# ("Stra0e".casefold())

#trim .strip()
# in python indexing start from 0

#list and tuple
#methods: append, extend, insert, remove, pop, clear, index, count, sort, reverse , copy

# empty=[]
# scores = [85,92,78,95,60]
# mixed=[42,3.14,'hello', True, None]
# matrix=[[1,2,3],
#         [4,5,6],
#         [7,8,9]
#         ]
# print(scores)
# print(mixed)
# print(matrix[1])

#indexing and slicing
# fruits=['apple', 'banana', 'cherry', 'elderberry']
# print(fruits[0])
# print(fruits[-1])
# print(fruits[1:4])
# print(fruits[:3])
# print(fruits[::2])

#mutating a list
# fruits =['apple', 'banana', 'cherry']
# fruits[1]='blueberry'
# print(fruits)

# fruits[1:3]=['mango', 'kiwi', 'papaya']
# print(fruits)

nums=[0,1,2,3,4,5,6,7,8,9]
nums.append(7)
print('append:', nums)

nums.extend([True])
print('hello:', nums)

nums.insert(7,99)
print('insert:', nums)

nums.remove(1)
print('remove:', nums)

popped = nums.pop()
print('pop:   ', nums, 'got:', popped )

print('index:', nums.index(5))
print('count 8:', nums.count(8))
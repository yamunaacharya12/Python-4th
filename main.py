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

sum = 0

sum += 1 #same as: sum = sum+1
print(sum) #1

sum +=1
print(sum)

sum *= 10
print(sum) #20

sum //= 3
print(sum) #6

sum **=2
print(sum)

sum=+ 2
print(sum)

sum=- 5
print(sum)

# sum=* 5
# print(sum)

# sum=// 7
# print(sum)

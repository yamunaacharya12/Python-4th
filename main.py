a = int (input("enter first number"))
b = int (input("enter second number"))
sum = a+b
print(sum)

x = "10.15"
print(x)== 10.15
print(str(x))


x=20.5
y='abc'
z=20

print(str(y)) #abc

print(int(y)) # conversion error

print(float(x)) #20.5
print(float(z)) #20.5

#======================

text = 'abc'
print(int(text)) #conversion error

# conclusion: number can done type conversion but string cannot be a number

name= 'Yamuna'
age= 20
gpa=3.714

print(f'{name} is {age} years old.')
print(f'GPA: {gpa:.2f}') #.2f=2 decimal places
print(f'10 squared = {10 ** 5}')
print(f'Is adult: {age>=19}')

def greet (name):
    """Return a greeting string for the given name."""
    return f'Hello,{name}!'
print(greet('Yamuna'))
print(greet.__doc__)

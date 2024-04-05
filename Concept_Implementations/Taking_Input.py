#Taking input from user
name = input("What's your name ? ")
print("Hello ", name)
#Taking integer input from user
age = int(input("What's your age ? "))
print("Your age is ", age)
#Taking float input from user
height = float(input("What's your height ? "))
print("Your height is ", height)
#Taking boolean input from user
is_student = bool(input("Are you a student ? "))
print("Are you a student ? ", is_student)
#Taking complex input from user
complex_number = complex(input("Enter a complex number : "))
print("Complex number is ", complex_number)
#Taking list input from user
list = list(input("Enter a list : "))
print("List is ", list)
#Taking tuple input from user
tuple = tuple(input("Enter a tuple : "))
print("Tuple is ", tuple)
#Taking set input from user
set = set(input("Enter a set : "))
print("Set is ", set)
#Taking dictionary input from user
dict = dict(input("Enter a dictionary : "))
print("Dictionary is ", dict)
#Taking string input from user
string = str(input("Enter a string : "))
print("String is ", string)
#Taking multiple inputs from user
name, age = input("Enter your name and age : ").split()
print("Your name is ", name)
print("Your age is ", age)
#Taking multiple integer inputs from user
x, y = map(int, input("Enter two numbers : ").split())
print("Sum is ", x+y)
#Taking multiple float inputs from user
x, y = map(float, input("Enter two numbers : ").split())
print("Sum is ", x+y)
#Taking multiple boolean inputs from user
x, y = map(bool, input("Enter two boolean values : ").split())
print("Sum is ", x+y)
#Taking multiple complex inputs from user
x, y = map(complex, input("Enter two complex numbers : ").split())
print("Sum is ", x+y)
#Taking multiple list inputs from user
x, y = map(list, input("Enter two lists : ").split())
print("Sum is ", x+y)
#Taking multiple tuple inputs from user
x, y = map(tuple, input("Enter two tuples : ").split())
print("Sum is ", x+y)
#Taking multiple set inputs from user
x, y = map(set, input("Enter two sets : ").split())
print("Sum is ", x+y)
#Taking multiple dictionary inputs from user
x, y = map(dict, input("Enter two dictionaries : ").split())
print("Sum is ", x+y)
#Taking multiple string inputs from user
x, y = map(str, input("Enter two strings : ").split())
print("Sum is ", x+y)
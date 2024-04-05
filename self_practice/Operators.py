#Operators in Python :-

#Arithmetic Operators :-
#Addition :-
a = 10
b = 20
c = a + b
print("Addition of a and b is : ", c)
#Subtraction :-
c = a - b
print("Subtraction of a and b is : ", c)
#Multiplication :-
c = a * b
print("Multiplication of a and b is : ", c)
#Division :-
c = a / b
print("Division of a and b is : ", c)
#Modulus :-
c = a % b
print("Modulus of a and b is : ", c)
#Floor Division :-
c = a // b
print("Floor Division of a and b is : ", c)
#Exponentiation :-
c = a ** b
print("Exponentiation of a and b is : ", c)
#Comparison Operators :-
#Equal to :-
a = 10
b = 20
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")
#Not Equal to :-
if a != b:
    print("a is not equal to b")
else:
    print("a is equal to b")
#Greater than :-
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")
#Less than :-
if a < b:
    print("a is less than b")
else:
    print("a is not less than b")
#Greater than or equal to :-
if a >= b:
    print("a is greater than or equal to b")
else:
    print("a is not greater than or equal to b")
#Less than or equal to :-
if a <= b:
    print("a is less than or equal to b")
else:
    print("a is not less than or equal to b")
#Logical Operators :-
#AND :-
a = 10
b = 20
c = 30
if a > b and a > c:
    print("a is the greatest")
elif b > a and b > c:
    print("b is the greatest")
else:
    print("c is the greatest")
#OR :-
if a > b or a > c:
    print("a is the greatest")
elif b > a or b > c:
    print("b is the greatest")
else:
    print("c is the greatest")
#NOT :-
if not a > b:
    print("a is not greater than b")
else:
    print("a is greater than b")
#Assignment Operators :-
#Equal to :-
a = 10
b = 20
c = a
print("c is : ", c)
#Addition :-
c += a
print("c is : ", c)
#Subtraction :-
c -= a
print("c is : ", c)
#Multiplication :-
c *= a
print("c is : ", c)
#Division :-
c /= a
print("c is : ", c)
#Modulus :-
c %= a
print("c is : ", c)
#Floor Division :-
c //= a
print("c is : ", c)
#Exponentiation :-
c **= a
print("c is : ", c)
#Bitwise Operators :-
#AND :-
a = 10
b = 20
c = a & b
print("c is : ", c)
#OR :-
c = a | b
print("c is : ", c)
#XOR :-
c = a ^ b
print("c is : ", c)
#NOT :-
c = ~a
print("c is : ", c)
#Left Shift :-
c = a << 2
print("c is : ", c)
#Right Shift :-
c = a >> 2
print("c is : ", c)
#Identity Operators :-
#is :-
a = 10
b = 20
if a is b:
    print("a and b are same")
else:
    print("a and b are not same")
#is not :-
if a is not b:
    print("a and b are not same")
else:
    print("a and b are same")
#Membership Operators :-
#in :-
a = [10, 20, 30, 40, 50]
if 10 in a:
    print("10 is in a")
else:
    print("10 is not in a")
#not in :-
if 10 not in a:
    print("10 is not in a")
else:
    print("10 is in a")
#Ternary Operator :-
a = 10
b = 20
c = a if a > b else b
print("c is : ", c)
#Operator Precedence :-
#Precedence of Operators :-
#1. Parentheses ()
#2. Exponentiation **
#3. Complement ~, Unary +, Unary -
#4. Multiplication *, Division /, Floor Division //, Modulus %
#5. Addition +, Subtraction -
#6. Right to Left
#7. Left Shift <<, Right Shift >>
#8. Bitwise AND &
#9. Bitwise XOR ^
#10. Bitwise OR |
#11. Comparison Operators
#12. Logical Operators
#13. Assignment Operators
#14. Identity Operators
#15. Membership Operators
#16. Ternary Operator
#17. Comma ,

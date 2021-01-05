import math

print("Le kalkulator")
one = int(input("Działanie: "))
oper = input()
two = int(input())

if oper == "/" and two == 0:
    print("Nie dziel cholero przez zero")
else:
    if oper == "+":
        print(str(one) + oper + str(two) + "=" + str(one + two))
    elif oper == "-":
        print(str(one) + oper + str(two) + "=" + str(one - two))
    elif oper == "*":
        print(str(one) + oper + str(two) + "=" + str(one * two))
    elif oper == "/":
        print(str(one) + oper + str(two) + "=" + str(one / two))

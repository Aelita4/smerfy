print("Le kalkulator")

one = input("Działanie: \n")

check_int = isinstance(one, int)

if check_int == False :
    print("To nie liczba")

oper = input()
two = input()

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
    else:
        print("Nie można wykonać operacji!")

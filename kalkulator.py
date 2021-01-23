

print("Le kalkulator")

while True:

    one = input("Działanie: \n")

    try:
        t = int(one)
    except ValueError:
        print("To nie liczba")
        continue

    oper = input()


    two = input()

    try:
        t2 = int(two)
    except ValueError:
        print("To nie liczba")
        continue




#check section
    if oper == "/" and t2 == 0:
        print("Nie dziel cholero przez zero")
    else:
        if oper == "+":
            print(str(t) + oper + str(t2) + "=" + str(t + t2))
            break
        elif oper == "-":
            print(str(t) + oper + str(t2) + "=" + str(t - t2))
            break
        elif oper == "*":
            print(str(t) + oper + str(t2) + "=" + str(t * t2))
            break
        elif oper == "/":
            print(str(t) + oper + str(t2) + "=" + str(t / t2))
            break
        else:
            print("Nie można wykonać operacji!")
            continue

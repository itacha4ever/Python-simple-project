def calculator():
    print("1- add \n2- sub \n3- multiple  \n4- divied \n5- modeul")

    opration = input("please choose and operation :")
    if opration != "1" and opration != "2" and opration != "3" and opration != "4" and opration != "5":
        print("wrong choice")
        exit()

    number1 = int(input("please enter ur first number : "))
    number2 = int(input("please enter ur second number : "))

    if opration == "1":
        add = number1 + number2
        print("ur value is :" + str(add))
    elif opration == "2":
        sub = number1 - number2
        print("ur value is :" + str(sub))
    elif opration == "3":
        mult = number1 * number2
        print("ur value is :" + str(mult))
    elif opration == "4":
        div = number1 / number2
        print("ur value is :" + str(div))
    elif opration == "5":
        mod = number1 % number2
        print("ur value is :" + str(mod))


calculator()

def calc():
    print("CALCULATOR 1.0")
    print("current possible arithmetics: +,-,*,/")

    num1=float(input("1st Number:"))
    num2=float(input("2nd Number:"))
    operator=input("Operator (+,-,*/):")

    if operator=="+":
        print(num1+num2)
    if operator=="-":
        print(num1-num2)
    if operator=="*":
        print(num1*num2)
    if operator=="/":
        print(num1/num2)

calc()
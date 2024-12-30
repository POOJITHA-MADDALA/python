a = int(input("Enter the initial number:"))
while True:
    ch = input("Enter the operation(+,-,*,/):")
    b = int(input("Enter the next number:"))
    if ch == '+':
        a = a + b
        print(f"{a - b} + {b} = {a}")
    elif ch == '-':
        a = a - b
        print(f"{a + b} - {b} = {a}")
    elif ch == '*':
        a = a * b
        print(f"{a // b} * {b} = {a}")
    elif ch == '/':
        if b != 0:
            a = a / b
            print(f"{a * b} / {b} = {a}")
        else:
            print("error/0")
    else:
        print("Invalid operator....")
        break
    cont = input("Do you want to continue(Y/n):")
    if cont.lower() != 'y':
        break

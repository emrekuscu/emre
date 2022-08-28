print("""
Emrelator
for addition  = +
for subtraction  = -
for multiplication = x
for division = /
""")
while (True):
    process = input("which process")
    number1 = int(input(" First Number for process"))
    number2 = int(input(" Second Number for process"))
    if process == "+":
        print(number1 + number2," result")
        print("do you want to do any other process? Y/N")
        reply = input()
        if reply == "Y":
            print("please wait...")
        elif reply == "N":
            print("thanks for use Emrelator")
            break
        else :
            print ("Do not try bug you smart!!!")
            break
    elif process == "-":
        print(number1 - number2," result")
        print("do you want to do any other process? Y/N")
        reply = input()
        if reply == "Y":
            print("please wait...")
        elif reply == "N":
            print("thanks for use Emrelator")
            break
        else :
            print ("Do not try bug you smart!!!")
            break
    elif process == "x":        
        print(number1 * number2," result")
        print("do you want to do any other process? Y/N")
        reply = input()
        if reply == "Y":
            print("please wait...")
        elif reply == "N":
            print("thanks for use Emrelator")
            break
        else :
            print ("Do not try bug you smart!!!")
            break
    elif process == "/":     
        print(number1 / number2," result")
        print("do you want to do any other process? Y/N")
        reply = input()
        if reply == "Y":
            print("please wait...")
        elif reply == "N":
            print("thanks for use Emrelator")
            break
        else :
            print ("Do not try bug you smart!!!")
            break
    else :
        print ("Do not try bug you smart!!!")
        break
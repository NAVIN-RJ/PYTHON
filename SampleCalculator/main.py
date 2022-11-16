import operations

def calculate():  
    numbers =  input("Please enter two numbers\n")
    first, second = numbers.split(" ")
    first, second = int(first), int(second)
    print("Please choose any of the following options:\n")

    choice = input(" 1: Addition \n 2: Subtraction \n 3: Product \n 4: IntegerDivision \n 5: FloatDivision \n 6: Modulo\n")

    match int(choice):
        case 1:
            print(operations.addition(first, second))
        case 2:
            print(operations.subtraction(first, second))
        case 3:
            print(operations.product(first, second))
        case 4:
            print(operations.integerDivision(first, second))
        case 5:
            print(operations.floatDivision(first, second))
        case 6:
            print(operations.modulo(first, second))
        case _:
            print("Invalid choice!")
            return
    calculate()

def main():
    print("Welcome to Calculator")
    calculate()

main()

import operations

def operate():

    print("Please choose any of the following options:\n")
    choice = input(" 1: Balance Check \n 2: Cash Deposit \n 3: Cash Withdraw \n 4: PIN Change \n")
    match int(choice):
        case 1:
            print("Available Balance: ", operations.BALANCE, "\n")
        case 2:
            amount = int(input("Enter amount to deposit: "))
            operations.BALANCE += amount
        case 3:
            amount = int(input("Enter amount to withdraw: "))
            if amount > operations.BALANCE :
                print("Insufficient Balance!")
            operations.BALANCE -= amount
        case 4:
            number = int(input("Please enter registered mobile number: "))
            if number != operations.MOBILE:
                print("Incorrect Number!")
            else:
                operations.PIN = int(input("Enter New PIN"))
        case _:
            print("Invalid Choice")
            return
    operate()

def main():
    print("Welcome to MiniBanking")
    operate()
    print("Thank you :)")


main()

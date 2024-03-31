
customernames=['Annie','Bunny','David','Marry','Chiku']
customerpins=['1001','1002','1003','1004','1005']
customerbalances=[20000, 3500, 80000, 500, 1000]
balance=0
deposition=0
while(True):
    print()
    print("="*40)
    print(" ----- WELCOME TO ANDHRA BANK ----- ")
    print("="*40)
    print("*"*40)
    print("=>>     1. Open New Account          <<=")
    print("=>>     2. Withdraw Money            <<=")
    print("=>>     3. Deposit Money             <<=")
    print("=>>     4. Check Customers Balance   <<=")
    print("=>>     5. Exit/Quit                 <<=")
    print("*"*40)
    choice=int(input("Select your choice number from th above menu:"))
    if choice == 1:
        print("Choice number 1 is selected by the customer")
        print("Let's start creating your account in our bank:")
        name=str(input("Enter Your Name:"))
        customernames.append(name)
        pin=eval(input("Enter Your Pin:"))
        customerpins.append(pin)
        deposition=eval(input("Deposit amount to start an account:"))
        balance=0
        balance=balance+deposition
        customerbalances.append(balance)
        print("\nYour name is added to customers system")
        print("Your pin is added to customer system")
        print("Your balance is added to customer system")
        print("----New account created successfully !----")
        print("\n")
        print("Your name is avalilable on the customers list now : ")
        print(customernames)
        print("\n")
        print("Note! Please remember the Name and Pin")
        print("==============================================================================================")
    # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choice == 2:
        print("Choice number 2 is selected by the customer")
        name=str(input("Enter your name:"))
        pin=input("Enter your pin:")
        if name in customernames and pin in customerpins:
            index = customernames.index(name)
            withdraw=eval(input("Enter amount to withdraw:"))
            if withdraw < customerbalances[index]:
                customerbalances[index] -= withdraw 
                print(withdraw,"Withdraw Successfull!")
                print("Current Balance:",customerbalances[index])
            else:
                print("Insufficient Balance!")    
        else:
            print("Sorry!, Invalid Credentials. Please Try Again!") 
    elif choice == 3:
        print("Choice number 3 is selected by the customer")
        name=str(input("Enter Name:"))
        pin=input("Enter Pin:")
        if name in customernames and pin in customerpins:
            index = customernames.index(name)
            deposit = eval(input("Enter money to deposit:"))
            customerbalances[index] += deposit
            print(deposit,"Amount Deposited To Your Account")
            print("Current Balance:",customerbalances[index])
        else:
            print("Sorry,Invalid Account Credentials!. Please Try Again!")  
    elif choice == 4:
        print("Choice number 4 is selected by the customer")
        name=str(input("Enter Name:"))
        pin=input("Enter Pin:")
        if name in customernames and pin in customerpins:
            index = customernames.index(name)
            print("Customer Balance:",customerbalances[index])
        else:
            print("Sorry,Invalid Account Credentials!. Please Try Again!")
    elif choice == 5:
        # These statements would be just showed to the customer.
        print()
        print("Choice number 5 is selected by the customer")
        print()
        print("Thank you for using our banking system!")
        print("\n")
        print("Come again")
        print("Bye bye")
        break
    else:
        # This else function above would work when a wrong function is chosen.
        print("Invalid option selected by the customer")
        print("Please Try again!")
        # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")


                   









    

        






    
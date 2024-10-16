print("Welcome to Sidian Bank!")
pin = 5678
chances = 3
balance = 50000

while chances != 0:
    entered_pin = int(input("Enter your four digit PIN: "))
    if entered_pin != pin:
        chances -= 1
        print("Wrong PIN. You have")
        print(f"You have {chances} chances left.")
        
    else:
        user_choice = input("B : balance, D : deposit, W : withdraw")
        if user_choice == "B":
            print(f"Your current balance is Ksh.{balance}")


        if user_choice == "D":
            deposit_user = int(input("Enter your amount to  deposit:"))
            total_balance = deposit_user + balance 
            print(f"You have deposited  Ksh.{total_balance}")
            print(f"Your total balance is Ksh.{total_balance}")


            if user_choice == "W":
                withdraw_user = int(input("Enter your amount to withdraw"))
                total_balance = balance - withdraw_user
                print("You have withdrawn Ksh.{total_balance}")
                print (f"Your total balance is Ksh.{total_balance}")
            else:
             print("Insufficient funds.")
        


             user_exit = input("Would you like to exit? (Yes/No):")
        if user_exit == "Yes":
            print("Thank you for using Sidian Bank!")
            break
        else:
            continue          

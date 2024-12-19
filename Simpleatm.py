import time

print("Please insert your card")
time.sleep(5)

password = 1234
balance = 5000

pin = int(input("Enter your ATM card PIN: "))

if pin == password:
    while True:
        print("""
            1. Check Balance
            2. Withdraw Amount
            3. Deposit Balance
            4. Exit
        """)
        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option")
            continue

        if option == 1:
            print(f"Your balance is: {balance}")
            
        elif option == 2:
            withdraw_amount = int(input("Please enter withdrawal amount: "))
           
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account.")
                print(f"Your current balance is: {balance}")
         
            else:
                print("Insufficient balance!")
      
        elif option == 3:
            deposit_amount = int(input("Please enter deposit amount: "))
            balance += deposit_amount
            print(f"{deposit_amount} is credited to your account.")
            print(f"Your updated balance is: {balance}")
       
        elif option == 4:
            print("Thank you for using our ATM. Goodbye!")
            break
       
        else:
            print("Invalid choice. Please try again.")
else:
    print("Wrong PIN. Please try again.")

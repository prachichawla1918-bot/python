print("-----Welcom to ATM machine------")
pin="1918"
Balance=10000
               
user_pin=(input("enter your pin:"))
if user_pin == pin:

    print("---ATM DETAILS---")
    print("1. Check Balance")
    print("2. Withdraw Amount")
    print("3. Deposit Amount")
    print("4. Change PIN")
    print("5. Account Details") 
    print("6.Exit")

    choice=input("enter your choice:")

    if choice=="1":
        print("Available balance:",Balance)
  
    elif choice=="2":
        amount=int(input("enter your amount"))
        if amount<=Balance:
            Balance-=amount
            print("withdrawal successfull")
            print("updated balance:",Balance)
        else:
            print("insufficient balance")

    elif choice=="3":
        amount=float(input("enter deposit amount:"))
        Balance +=amount
        print("deposit successdully")
        print("updated balance:",Balance)

    elif choice=="4":
        new_pin=int(input("enter new pin"))
        pin=new_pin
        print("pin changed successfully")

    elif choice=="5":
        print("Account Holder: radha chawla")
        print("Account number: 123456789")
        print("current Balance",Balance)

    elif choice=="6":
        print("---THANKING YOU FOR USING ATM---")
        
    else:
        print("invalid Choice")
else:
    print("INVALID PIN.ACCESS DENIED")        
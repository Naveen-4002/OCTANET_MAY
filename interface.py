import time
print("please insert your card")
time.sleep(6)
password=7890
pin=int(input("enter your atm pin"))
balance=10000
if pin==password:
  while True:
    print(""""
        1==balance
        2==withdraw balance
        3== deposit balance
        4==exit
        """ )
    
    
    try:
        choice=int(input("please enter your choice "))
    except:
        print("please enter valid option")

    if choice==1:
        print(f"your current balance is {balance}")
        print("=================================================")
    if choice ==2:
        withdraw_money=int(input("please enter withdraw_money"))
        print("=================================================")
        print("=================================================")
        print("=================================================")
        balance=balance-withdraw_money
        print(f"{withdraw_money} is debited from your account")
        print("=================================================")
        print("=================================================")
        print(f"your current balance is {balance}")
    if choice==3:
        deposit_amt=int(input("please enter deposit amount"))
        balance=balance+deposit_amt
        print("=================================================")
        print("=================================================")
        print(f"{deposit_amt} is credited to your account")
        print("=================================================")
        print("=================================================")
        print(f"your updated balance is {balance}")
        print("=================================================")
        print("=================================================")
    if choice==4:

        break
else:
        print("wrong pin please try again")


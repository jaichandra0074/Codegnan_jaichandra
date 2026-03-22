''' this is my day 5 working with python i want to develop a sample program
includes all the previous learning concepts.(all operators )
'''
#small atm type program:

#user personal details
original_pin = 2303
Total_amount = 150000
daily_limit = 20000
options = ["withdrawl(1)","check_balance(2)"]

#process:
#inserting card
print(f'INSERT YOUR ATM CARD ')

#number verification and after verfication process
Num = int(input(f'Enter any number between  0 to 99 :'))
if Num >=0 and Num <= 99:
    Number_verification = True
else:
    Number_verification = False
    print("enter only two digit number")
if  Number_verification:
    user_pin = int(input("Enter your pin :"))
    if user_pin == original_pin:
        print("select any of the below options")
        print(options)
        user_option = int(input())
        if user_option == 1:
            withdrawl_amount = int(input("Enter amount"))
            if (withdrawl_amount <= Total_amount and withdrawl_amount >= daily_limit) or\
            (withdrawl_amount >= Total_amount and withdrawl_amount <= daily_limit)or\
            (withdrawl_amount >= Total_amount and withdrawl_amount >= daily_limit):
                print("AMOUNT CANT BE WITHDRAWL")
                print("may be insufficent balance or daily limit exceeds")
                
            if withdrawl_amount <= Total_amount and withdrawl_amount <= daily_limit:
                print(f'please collect yoiur cash: {withdrawl_amount}')
                Total_amount -= withdrawl_amount
                if input("display balancce (yes(1)/no(0):"):
                    print(f'available balance after withdrawl - {Total_amount}')
                print("THANKS FOR USING SBI")    
        if user_option == 2:
            print("balance amount",Total_amount)
            print("Thanks remove your card")
    else:
        print("WRONG PIN")
        print("Restart process again insert your card")
    

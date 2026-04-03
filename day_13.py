'''
pattern programs
'''
num = int(input("enter the limit of the pattern : "))
for j in range (num):
    for i in range(j):
        print("*",end = "")
    print()

num = int(input("enter the limit of the pattern : "))
for j in range (num):
    for i in range(1,j):
        print(i,end = "")
    print()

num = int(input("enter the limit of the pattern : "))
for j in range (num):
    for i in range (num):
        print("*",end = "")
    print()
    
num = int(input("enter the limit of the pattern : "))
for j in range (num):
    for i in range(num-j):
        print("*",end = "")
    print()

num = int(input("enter the limit of the pattern : "))
for j in range (num):
        print(" "*(num - j), end = "")
        for i in range(j+1,j-1) :
            print("*", end= " ")
        print()
icici_ramayya_ac_details = {"Name":"Neduri jaichandra dasaradha ramayya",
                            "date-of-brith" : "15-06-2004",
                            "ATM PIN" : "113374",
                            "Balance" : 200000}
print("welcome to the icici bank")
print("please insert the ATM card")
icici_user_pin = input("please enter your 6 digits ATM pin : ")
if len(icici_user_pin) == 6:
    if icici_user_pin in icici_ramayya_ac_details['ATM PIN']:
        icici_user_choice = int(input("enter \n1.withdraw: ")) 
        if icici_user_choice == 1:
            money_w = int(input("enter the money to withdraw : "))
            if money_w <= icici_ramayya_ac_details['Balance']:
                icici_ramayya_ac_details['Balance'] -= money_w
                print(icici_ramayya_ac_details['Balance'])
            else:
                print("insuff")
            
    else:
        print("the pin number is incorrect")
else:
    print("please enter the 6 digits numbers")

table_number = int(input("enter the number : "))
for i in range (1,21):
    print(f"{table_number}x{i} = {table_number * i}")
'''
methods
-----------------
count(),capitalize(),join(),
strip(),replace(),split(),
casefold(),isalnum(),isalpha()
,isdigit(),isdecimal(),islower(),
isupper()
------------------
there are more methods , but this methods are used most in the programming  
'''

al = input("enter the string :")
count_u = 0
count_l = 0
for j in al :
    if j.isupper():
        count_u += 1
    elif j.islower():
        count_l += 1
print(f"there are total {count_u} cap L")
print(f"there are total {count_l} small l")
#------------------------------------------------------------------------------

ak = input("enter the string :")
Cap_L = []
small_L = []
for ch in ak :
    if ch.isupper():
        Cap_L.append(ch)
    elif ch.islower():
        small_L.append(ch)
print(f"{Cap_L} contains all the caps ")
print(f"{small_L} contains all the smalls")
#--------------------------------------------------------------------------------       
icici_ramayya_ac_details = {"Name":"Neduri jaichandra dasaradha ramayya",
                            "date-of-brith" : "15-06-2004",
                            "ATM PIN" : "113374"}
print("welcome to the icici bank")
print("please insert the ATM card")
icici_user_pin = input("please enter your 6 digits ATM pin : ")
if len(icici_user_pin) == 6:
    if icici_user_pin in icici_ramayya_ac_details['ATM PIN']:
        print("the pin number is correct")
    else:
        print("the pin number is incorrect")
else:
    print("please enter the 6 digits numbers")

#---------------------------------------------------------------------------------
# perfect number
per_num = int(input("enter the number : "))
fact_all = 0

for j in range(1, per_num):
    if per_num % j == 0:
        fact_all += j

if fact_all == per_num:
    print(f"{per_num} is a perfect number")
else:
    print(f"{per_num} is not a perfect number")

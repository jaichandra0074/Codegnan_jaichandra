'''
break --->this is used to 
'''
for i in range (1,10):
    print(i)
    if i == 5 :
        break
'''
list = [1,2,3,4,5]
for n in list :
    print(n)
    if n == 1:
        break
'''
'''
continue ---> this is used to skip that particular loop
and this methods is not used for multiple values
'''
for j in range(1,20):
    if j == 5:
        continue
    print(j)
    
list = [1,3,4,5,"neduri","jaichandra"]
for j in list:
    if j == "neduri":
        continue
    print(j)

ad = "neduri jaichandra dasaradha ramayya"
for j in ad:
    if j == "n":
        continue
    print(j)
    
'''
pass ---> this is called as space holder
incase any statement like (if, for, else, elif...) this should complete, if not we will get syntax error to avoid this we are using pass
'''
for i in range (1,100):
    pass
'''
else -- for
--------------
it will fall back to else block, when all loops are completed
'''
for m in range(1,10):
    print(m)
else :
    print("else block")

#while ---> this a combination for and if statements, if we did not end the loop in proper way it will run upto the memory space in the becomes empty
user_in = int(input("enter the limit : "))
num_1 = 0
num_2 = 1
print(num_1,num_2,end="")
for v in range(user_in+1):
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    print(num_3,end=" ")
              



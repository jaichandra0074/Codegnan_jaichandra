'''
recursive functions
---------------------
recursion is a programming technique where a function calls itself either directly or indirectly to solve a problem by breaking it into smaller, simpler subproblems.
recursion is especially useful for problems that can be divided into identical smaller tasks, such as mathematical or  calculation. tree traversals or divide-and-conquer algorithms
'''
'''
def validate_pin(self):
    while self.remaining_attempts > 0:
        user_pin = input("enter 4 digit pin: ")
        if len(user_pin) == 4 and user_pin == self.user_info["ATM PIN"]:
            print("welcome to the atm")
            return true
        else:
            self.remaining_attempts -= 1
            if self.remaining_attempts > 0:
                print("invalid pin, attempts left : {self.remaining_attempts}")
            else :
                print("card blocked")
                return false
'''

string = input("Enter the string: ")

def vowels_consonants(string):
    vowels = []
    consonants = []
    
    for i in string:
        if i.isalpha():
            if i in "aeiouAEIOU":
                vowels.append(i)
            else:
                consonants.append(i)
    
    print(f"{vowels} these are all vowels in the string")
    
    print("Number of vowels:", len(vowels))

    print(f"{consonants} these are all consonants in the string")
    
    print("Number of consonants:", len(consonants))

vowels_consonants(string)

#prime check
num = int(input("Enter the number: "))
def prime(num):
    if num <= 1:
        print(f"{num} is not a prime number")
        return  
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            return
    print(f"{num} is a prime number")
prime(num)

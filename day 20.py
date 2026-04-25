
'''
file Handling ---> file handler is an object used to perform operations on files such as
creating, reading, writing, updating and deleting files

How to open a file
--------------------------
1. open() ---> This function takes 2 parameters and we must close the file using close()

1. file name
2. mode

example:
file = open("dummy.txt","r")
file.close()

--------------------------
2. with open()
--------------------------
This method automatically closes the file (best method)

example:
with open("dummy.txt","r") as file:
    print(file.read())

--------------------------
modes ("r","w","a","x","t")
--------------------------

------>
1. "r" ---> read
to read the file. If file does not exist, it throws error

example:
file = open("dummy.txt","r")
print(file.read())
file.close()

--------------------------

------>
2. "w" ---> write
to write data into file. It creates file if not exist and deletes old data

example:
file = open("dummy.txt","w")
file.write("I'm learning python")
file.close()

--------------------------

------>
3. "a" ---> append
to add data into file. It will not delete old data

example:
file = open("dummy.txt","a")
file.write("This is new line")
file.close()

--------------------------

------>
4. "x" ---> create
to create new file. If file already exists, it gives error

example:
file = open("newfile.txt","x")
file.close()

--------------------------

to read a file
--------------------------

1. read()
----------- 
this method reads entire file

example:
file = open("dummy.txt","r")
print(file.read())
file.close()

--------------------------

2. readline()
--------------- 
this method reads only one line

example:
file = open("dummy.txt","r")
print(file.readline())
file.close()

--------------------------

3. readlines()
----------------
this method reads all lines and returns list

example:
file = open("dummy.txt","r")
print(file.readlines())
file.close()

--------------------------

correct program (your code fixed)
--------------------------

# append data
file = open("chandu.txt","a")
file.write("this is line 4\n")
file.close()

# read data
file = open("chandu.txt","r")
print(file.read())
file.close()

--------------------------

best method (recommended)
--------------------------

with open("chandu.txt","a") as file:
    file.write("this is line 4\n")

with open("chandu.txt","r") as file:
    print(file.read())

'''
import os

filename = "chandu.txt"

# 1. CREATE FILE (x mode)
try:
    file = open(filename, "x")
    file.write("File created successfully\n")
    file.close()
    print("File created")
except FileExistsError:
    print("File already exists")

# 2. WRITE TO FILE (w mode - overwrites)
file = open(filename, "w")
file.write("Line 1: I'm learning Python\n")
file.write("Line 2: File handling is easy\n")
file.close()
print("Data written successfully")

# 3. APPEND DATA (a mode)
file = open(filename, "a")
file.write("Line 3: This is appended line\n")
file.write("Line 4: Adding more content\n")
file.close()
print("Data appended successfully")

# 4. READ FULL FILE (r mode)
file = open(filename, "r")
print("\n--- Full File Content ---")
print(file.read())
file.close()

# 5. READ LINE BY LINE (readline)
file = open(filename, "r")
print("\n--- First Line ---")
print(file.readline())
file.close()

# 6. READ ALL LINES AS LIST (readlines)
file = open(filename, "r")
print("\n--- All Lines as List ---")
print(file.readlines())
file.close()

# 7. USING WITH OPEN (Best Practice)
print("\n--- Using with open() ---")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())

# 8. CHECK FILE EXISTS
print("\n--- Checking File Exists ---")
if os.path.exists(filename):
    print("File exists")
else:
    print("File does not exist")

# 9. DELETE FILE (optional)
# Uncomment below lines if you want to delete file
"""
if os.path.exists(filename):
    os.remove(filename)
    print("File deleted")
else:
    print("File not found")
"""

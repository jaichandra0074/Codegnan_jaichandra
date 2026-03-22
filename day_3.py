
# day 3 of my python journey ,here by learning previous concepts like variables, literals ,typecasting.
#I'm creating my own case study including all those in my own way.


#Today i built a small program for taking user information regarding their academics.


student_id	=input("Enter your id 		     : " )
student_name	=input("Enter your name 	     : " )
branch		=input("Enter your branch 	     : " )
year		=input("Enter your year of studying  : " )
print("\n Enter each subjects marks \n")
python		=int(input("python marks: " ))
os		=int(input("os marks    : " ))
maths		=int(input("maths marks : " ))
dbms		=int(input("dbms marks  : " ))
print("\n\n")
print("___student_details___\n")
print("Student_Name  : ",student_name)
print("Student_Id    : ",student_id)
print("Branch	      : ",branch)
print("year_of_study : ",year)
print("Exam Results  : ")
subjects=["python","os","maths","dbms"]
marks=[python,os,maths,dbms]
for i in range(len(subjects)):
    if marks[i] > 40:
        print(f"        {subjects[i]} - Passed")
    else:
        print(f"        {subjects[i]} - Failed")
 


#Typeconversions

#working on conversions complex to remaining datatypes
#Complex ➝ str
x = 3 + 4j
s = str(x)
print(s)        # "(3+4j)"
print(type(s))  # <class 'str'> it works

#Complex ➝ boo
y=2 + 5j
print(type(y))
t = bool(y)
print(t)
print(type(t))

#Complex ➝ Extracting Parts(Even though direct conversion isn't allowed,
#you can do as below extract each part seperately and can convert to wanted type
z = 3 + 4j
print(x.real)   # 3.0
print(x.imag)   # 4.0
print(type(int(z.real)))   # <class 'int'>
print(type(float(z.imag))) # <class 'float'>

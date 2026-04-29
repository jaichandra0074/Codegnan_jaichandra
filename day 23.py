'''
import re

def validate_name(name):
    pattern = r'[A-Za-z]{3,}$'
    return re.fullmatch(pattern, name)

def validate_email(email):
    pattern = r'[\w\.-]+@[\w\.-]+\.\w+$'
    return re.fullmatch(pattern, email)

def validate_phone(phone):
    pattern = r'^[0-9]{10}$'
    return re.fullmatch(pattern, phone)

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.fullmatch(pattern, password)

def main():
    name= input("enter name:")
    email=input("enter email:")
    phone=input("enter phone number:")
    password=input("enter password:")

    if not validate_name(name):
        print("Invalid Name")
    elif not validate_email(email):
        print("Invalid email")
    elif not validate_phone(phone):
        print("Invalid phone number")
    elif not validate_password(password):
        print("Invalid password")
    else:
        print("All inputs are valid! form submitted successfully")

if __name__ =="__main__":
        main()

'''

'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------DATA ANALYSIS-------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
WHY THIS IS NEED ?
--------------------
Data analysis helps you:
Understand patterns (trends, growth, decline)
Make better decisions (business, projects, etc.)
Visualize data (graphs make things clearer)

1. Bar Graph

A bar graph is used to compare different categories. It represents data using rectangular bars, where the height or length of each bar shows the value.

2. Line Graph

A line graph shows trends over a period of time. Data points are connected with lines to display increases or decreases.

3. Pie Chart

A pie chart represents data as parts of a whole. The circle is divided into slices, where each slice shows a percentage or proportion.

4. Histogram

A histogram displays the frequency distribution of continuous data. It groups data into intervals and shows how often each range occurs.

5. Scatter Plot

A scatter plot shows the relationship between two variables. Data is represented as points on a graph to identify patterns or correlations.

6. Area Graph

An area graph is similar to a line graph but the area below the line is filled. It is used to show the magnitude of values over time.


'''
import matplotlib.pyplot as plt

labels = ["A", "B", "C", "D"]
values = [200, 40, 60, 80]

plt.bar(labels, values)
plt.title("Bar Graph")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [200, 40, 60, 80]

plt.plot(x, y, marker='o')
plt.title("Line Graph")
plt.show()

import matplotlib.pyplot as plt

values = [200, 40, 60, 80]
labels = ["A", "B", "C", "D"]

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

import matplotlib.pyplot as plt

data = [10, 20, 20, 30, 40, 40, 40, 50]

plt.hist(data)
plt.title("Histogram")
plt.show()


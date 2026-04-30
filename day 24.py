import matplotlib.pyplot as plt

# Bar Chart
plt.bar([2024,2025,2026],[67,89,50])
plt.title("Car Sales")
plt.xlabel("Years")
plt.ylabel("Number of Cars sold")
plt.show()

# Scatter Plot
plt.scatter([1,2,3,4],[200,400,100,800], color="yellow", s=100)
plt.title("Swift Car Sales")
plt.xlabel("Years")
plt.ylabel("Number of Sales")
plt.show()

# Fixed Bar Chart
plt.bar([2024,2025,2026],[67,89,50], color="gray")
plt.title("Car Sales")
plt.xlabel("Years")
plt.ylabel("Number of cars sold")
plt.show()

# Pie Chart
values = [40, 15, 35, 20]
labels = ["Backend (Python)","Frontend (HTML, CSS)","Framework (Flask)","Library (NumPy, Pandas, Matplotlib)"]
plt.pie(values, labels=labels)
plt.title("ATM Application (Project)")
plt.legend(["Sai", "Niral", "Abdul", "Teja"])
plt.show()

# web scraping

import requests
from bs4 import BeautifulSoup
url = "http://books.toscrape.com/"

try:
    response = requests.get(url)
    response.encoding = 'utf-8'
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
    exit()
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.find("p", class_="star-rating")["class"][1]
    
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Rating: {rating}")
    print("-" * 40)

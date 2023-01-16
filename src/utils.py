import requests
from bs4 import BeautifulSoup
url = "https://www.starwars.com/databank/luke-skywalker"
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")

if __name__ == "__main__":
    temp = soup.find_all(class_="stats-container cols-9")

    # temp_1 = temp.find(class_="heading")
    # print(temp_1)
    print(temp)

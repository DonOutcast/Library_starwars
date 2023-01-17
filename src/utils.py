import requests
from bs4 import BeautifulSoup
from lxml import etree

HEADERS = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
url = "https://www.starwars.com/databank/luke-skywalker"
response = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(response.content, "html.parser")

if __name__ == "__main__":
    # print(soup.prettify())
    weapons = []
    temp = soup.find_all("div", class_="category")
    # print(temp[6].text)
    for i in temp:
        if "Weapons" in i.text:
            weapons = i.find_all("div", class_="property-name")
    for j in weapons:
        print(j.text)
    # dom = etree.HTML(str(soup))
    # print(dom.xpath('//*[@id="ref-1-6"]/div/div/div[7]/ul/li')[0])

#ref-1-6 > div > div > div:nth-child(7) > ul

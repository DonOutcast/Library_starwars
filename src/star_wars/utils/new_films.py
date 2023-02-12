import requests
from bs4 import BeautifulSoup

class NewFilms:

    def __int__(self):
        # self.response = requests.get("")
        ...

    def get_all_films(self):
        response = requests.get("https://www.starwars.com/films")
        soup = BeautifulSoup(response.content, "html.parser")
        print(soup.select("#ref-1-5 > div.bound.vertical > div.blocks-bound > div > ul > li:nth-child(1) > div > div > div > div > div.image-wrapper > div > a > img"))
        # print(soup.find("div", {"class": "blocks-container ref-1-5"}).find_all("img", {"class": "thumb reserved-ratio"}))
        all_a = soup.find("div", {"class": "blocks-container ref-1-5"}).find_all("div", {
            "class": "aspect lazy-deferred lazy-load placeholder"})
        # for i in all_a:
        # print(i.find("a")["href"])
        # print(i.find("img")["alt"])
        # print(i.find("img")["data-src"])

if __name__ == "__main__":
    temp = NewFilms()
    temp.get_all_films()
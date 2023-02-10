import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://www.starwars.com/films/star-wars-episode-iv-a-new-hope"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup.find("section", {"id": "ref-1-6"}))
    # print(soup.find_all("div", {"class": "module_header filters_header has-list has-dropdown"}))
    # print(soup.select("#ref-1-6 > div.bound.vertical.peeking"))
    r_1 = requests.get("https://www.starwars.com/_grill/filter/films/star-wars-episode-iv-a-new-hope?filter=Characters&mod=6")
    r_2 = requests.get("https://www.starwars.com/_grill/filter/films/star-wars-episode-iv-a-new-hope?filter=Creatures&mod=6")
    temp = r_2.json()
    print(temp)
    # for i in temp["data"]:
    #     if i["slug"] == "databank/boba-fett":
    #         print(i)
        # print(i["id"], i["slug"],  i["desktop_square_thumb"])

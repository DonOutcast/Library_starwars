try:
    import requests
    from bs4 import BeautifulSoup
    from lxml import etree
    from exceptions import ResourceDoesNotExists
    import sys
except (Exception,) as e:
    print(sys.exc_info())
HEADERS = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
url = "https://www.starwars.com/databank/luke-skywalker"
new_url = "https://www.starwars.com/databank/Leia-Organa"
response = requests.get(new_url, headers=HEADERS)
soup = BeautifulSoup(response.content, "html.parser")


def get_url_image(url_person: str, in_soup: BeautifulSoup) -> str:
    result = in_soup.find("div", class_="image-wrapper").find("img").get("data-src")
    print(type(result))
    return result


def save_image(person_name: str, path_to_image) -> bool:
    """Save the image to your directory

    :param person_name: The file location and name
    :type person_name: str
    :param path_to_image: A file link to
    :type path_to_image: str
    :returns: If the file saved successfully True else False
    :rtype: bool
    """
    try:
        with open(person_name + ".png", "wb") as f:
            f.write(requests.get(path_to_image).content)
    except Exception as error:
        print(error)
        return False
    else:
        return True


# if __name__ == "__main__":
#     path = get_url_image("sss", soup)
#     print(save_image("siste", path))
# print(soup.prettify())
# weapons = []
# temp = soup.find_all("div", class_="category")
# # print(temp[6].text)
# for i in temp:
#     if "Weapons" in i.text:
#         weapons = i.find_all("div", class_="property-name")
# if weapons:
#     print(weapons)

# print(soup.select("#ref-1-6 > div > div > div:nth-child(7)"))
# status = soup.find_all("div", class_="stats-container")
# print(status)
# dom = etree.HTML(str(status))
# print(dom.xpath('//*[@class="category"][6]/ul/li/a/div/text()'))

# images = soup.select("img")[2].attrs
# dom = etree.HTML(str(soup))
# with open("image.png", 'wb') as f:
#     f.write(requests.get(images.get("data-src")).content)

import json
import requests
from settings import Config
import telebot


class StarWars:
    """
    Class for all names and ids in world Star Wars.
        Usage:

    .. code-block:: python3
        :caption: Creating instance of StarWars

        from star_wars import star_wars
        jedi = StarWars(
        # and use jedi methods.
    """

    def __init__(self):
        self.__url_people = Config.get_url_api() + Config.get_people()
        self.__url_planets = Config.get_url_api() + Config.get_planets()
        self.__url_films = Config.get_url_api() + Config.get_films()
        self.__url_species = Config.get_url_api() + Config.get_species()
        self.__url_vehicles = Config.get_url_api() + Config.get_vehicles()
        self.__url_starships = Config.get_url_api() + Config.get_starships()

    @staticmethod
    def get_response(url_path: str, name_key: str) -> dict[str, int]:
        """ Return a response to url
         :param: url_path str
         :type: str
         :param: name_key this is a key of value
         :type: str
         :returns: Response to url in a dictionary
         :type: dict[str, int]
        """
        running = True
        names = {}
        while running:
            my_response = requests.get(url_path)
            if my_response.status_code != 200:
                raise ResourceDoesNotExists
            json_data = json.loads(my_response.content)
            for resource in json_data["results"]:
                names[resource.get(name_key)] = resource.get("url").split("/")[-2]
            if bool(json_data.get("next")):
                url_path = json_data["next"]
            else:
                running = False
        return names

    def get_people_names(self):
        """ Return all names and ids of people
         :returns: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self.get_response(self.__url_people, name_key="name")

    def get_planets_names(self):
        """ Return all names and ids of planets
         :returns: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self.get_response(self.__url_planets, name_key="name")

    def get_films_names(self):
        """ Return all names and ids of films
         :returns: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self.get_response(self.__url_films, name_key="title")

    def get_species_names(self):
        """ Return all names and ids of species
         :returns: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self.get_response(self.__url_species, name_key="name")

    def get_vehicles_names(self):
        """ Return all names and ids of vehicles
         :returns: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self.get_response(self.__url_vehicles, name_key="name")

    def get_starships_names(self):
        """ Return all names and ids of starships
         :returns: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self.get_response(self.__url_starships, name_key="name")


if __name__ == "__main__":
    temp = StarWars()
    print(temp.get_films_names())

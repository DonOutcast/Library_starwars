import time
from typing import List, Any

try:
    import requests
    from bs4 import BeautifulSoup
    from lxml import etree
    from exceptions import ResourceDoesNotExists
    import sys
except (Exception,) as e:
    print(sys.exc_info())


# HEADERS = {
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
# url = "https://www.starwars.com/databank/luke-skywalker"
# new_url = "https://www.starwars.com/databank/Leia-Organa"
# response = requests.get(new_url, headers=HEADERS)
# soup = BeautifulSoup(response.content, "html.parser")


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
from utils_1 import query
from settings import Config


class BaseRequest:
    """
    The Class generate response with json
    :param id_search: id of people or starships or planets or films or species or vehicles
    :type id_search: :obj: `int`
    :param url_path: the path from Config
    :type url_path: :obj: `str`
    :return: If status code request is 200 a json data or Exception
    :type: :obj: `json`
    """

    def __init__(self, id_search: int, url_path: str) -> None:
        response_json = query("{0}/{1}".format(url_path, id_search))
        self.json_data = response_json.json()

    # @staticmethod
    def _check_status_code(self, url_path):
        status = requests.get(url_path)
        if status != 200:
            raise ResourceDoesNotExists
        return status

    def _get_items_of_json(self, key_class: str, key_tag, url_path: str) -> list[Any]:
        """ Return all pilots of the starship
            :param key_class: Word for search example  starships, films
            :type key_class: :obj: `str`
            :param key_tag: Word for search in json example name, title
            :type key_tag: :obj: `str`
            :param url_path: Url for page in API
            :type url_path: :obj: `str`
            :param search_id: ID for ship
            :type search_id: :obj: `int`
            :return: List of names
            :type: list[str]
        """
        running = True
        names = []
        while running:
            my_response = requests.get(url_path)
            if my_response.status_code != 200:
                raise ResourceDoesNotExists
            json_data = json.loads(my_response.content)
            for resource in json_data["results"]:
                for starship in resource.get(key_class):
                    if starship.split("/")[-2] == str(self.id):
                        names.append(resource.get(key_tag))
            if bool(json_data.get("next")):
                url_path = json_data["next"]
            else:
                running = False
        return names


class Starship(BaseRequest):
    """
    Class for all names and ids in world Star Wars.
        Usage:

    .. code-block:: python3
        :caption: Creating instance of StarWars

        from star_wars import star_wars
        jedi = StarWars(
        # and use jedi methods.

        :param id_starship: of a starship, should be obtained from StarWars
        :type id_starship: :obj: `int`
    """

    def __init__(self, id_starship: int):
        super(Starship, self).__init__(id_starship, Config.get_url_api() + Config.get_starships())
        self.image_path = None
        self.id = id_starship
        self.url_starship = Config.get_url_starships()

    def get_starship_json(self):
        """ Return all names and ids of planets
         :return: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self.json_data

    def get_pilots(self) -> list[Any]:
        """
            Return all pilots of the starships
            :return: Names of all pilots if haves
            :type: :obj: `List[str]`
        """
        pilot_names = self._get_items_of_json("starships", "name", Config.get_url_api() + Config.get_people())
        return pilot_names

    def get_films(self) -> list[Any]:
        """
            Return all films with the starship
            :return: Names of all films with the starship
            :type: :obj: `list[str]`
        :return:
        """
        films_names = self._get_items_of_json("starships", "title", Config.get_url_api() + Config.get_films())
        return films_names

    def get_name(self):
        """
            Return a name of the starship
            :return: Name
            :type: :obj: `str`
        """
        return  self.json_data.get("name")
    def get_descriptions(self, name: str) -> str:
        """ Return a descriptions of the ship
            :return: `obj` str
            :type:
        """
        my_response = requests.get(self.url_starship + name.replace(" ", "_"))
        my_soup = BeautifulSoup(my_response.content, "lxml").select("div.mw-parser-output > p")
        result = ""
        for p in my_soup:
            if "<aside" in str(p):
                continue
            else:
                result = p.text
                break
        return result.strip()

    def get_photo_ship(self, name: str) -> str:
        """ Return a descriptions of the ship
            :return: `obj` str
            :type:
        """
        my_response = requests.get(self.url_starship + name.replace(" ", "_"))
        my_soup = BeautifulSoup(my_response.content, "lxml").select("div.mw-parser-output > p")
        result = ""
        for p in my_soup:
            if "<aside" in str(p):
                result = p.select_one("img.pi-image-thumbnail").get("src")
                break
            else:
                result = my_soup.select_one("img.thumbimage").get("data-src")
                break
        self.image_path = result
        return result

    def download_image(self, path: str) -> None:
        """ The function save  image on your machine
            :param path: Name and path to save
            :type path: `obj` str
        """
        if BaseRequest._check_status_code(self.image_path) == 200:
            with open("image.png", 'wb') as file:
                file.write(requests.get(self.image_path).content)


# def test_find():
#     url_path = "https://starwars.fandom.com/wiki/"
#     response = requests.get(url_path + name.replace(" ", "_"))
#     print(response.status_code)
#     soup = BeautifulSoup(response.content, "lxml")
#     soup_1 = soup.find("div", class_="page-content").find("div", {"id": "mw-content-text"})
#     print(soup_1.select("div > p:nth-child(6)"))


def all_pages(url_path, m_list):
    response = requests.get(url_path)
    json_data = response.json()
    if json_data.get("next"):
        url_path = json_data.get("next")
        m_list.append(json_data)
        return all_pages(url_path, m_list)


def get_pilots(m_jsons, id_starship):
    for json in id_starship:
        if json.get("results"):
            ...


# def get_pilots():
#     my_list = []
#     results = []
#     all_pages("https://swapi.dev/api/people/", my_list)
#     for json in my_list:
#         names = json.get("results")
#         for pilot in names:
#             # print(pilot.get("starships"))
#             for starship in pilot.get("starships"):
#                 print(starship)
#                 # print(starship.split("/"))
#                 if int(starship.split("/")[-2]) == 10:
#                     results.append(pilot.get("name"))
#     print(results)

if __name__ == "__main__":
    temp = Starship(10)
    print(temp.get_pilots())
    # f = temp.get_films()
    # print(temp.get_descriptions("Millennium Falcon"))

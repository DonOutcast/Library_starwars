try:
    import sys
    import json
    import os.path
    import requests
    from lxml import etree
    from typing import List, Any
    from bs4 import BeautifulSoup
    from src.star_wars.utils_1 import query
    from src.star_wars.settings import Config
    from src.star_wars.exceptions import ResourceDoesNotExists
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
        self.all_jsons = []
        self.all_pages(url_path)

    # @staticmethod
    @staticmethod
    def _check_status_code(url_path):
        """
        The function a check status code of get or post requests
        :param url_path: Url path
        :type: :obj:  `str`
        :return: True if status code == 200 else raise
        :type: :obj: `bool`
        """
        status = requests.get(url_path)
        if status.status_code != 200:
            raise ResourceDoesNotExists
        return True

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

    def all_pages(self, url_path) -> None:
        """

        :param url_path:
        :return:
        """
        self._check_status_code(url_path)
        response = requests.get(url_path)
        json_data = response.json()
        if json_data.get("next"):
            url_path = json_data.get("next")
            self.all_jsons.append(json_data)
            return BaseRequest.all_pages(self, url_path)


class Starship(BaseRequest):
    """
    Class for all names and ids in world Star Wars.
        Usage:

    .. code-block:: python3
        :caption: Creating instance of StarWars

        from star_wars import star_wars
        jedi = StarWars
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
        return self.json_data.get("name")

    def get_model(self):
        """
         Return a model of the starship
         :return: Model
         :type: :obj: `str`
        :return:
        """
        return self.json_data.get("model")

    def get_manufacture(self):
        """
        Return a manufacture of the starship
        :return: Manufacture
        :type: :obj: `str`
        """
        return self.json_data.get("manufacturer")

    def get_cost_in_credits(self):
        """
        Return a Cost in credits
        :return: Cost in credits
        :type: :obj: `str`
        """
        return self.json_data.get("cost_in_credits")

    def get_length(self) -> str:
        """
        Return a length  of the starships'
        :return: length
        :type: :obj: `str`
        """
        return self.json_data.get("length")

    def get_max_atmosphering_speed(self) -> str:
        """
        Return a max atmospherins speed  of the starships'
        :return: Max speed
        :type: :obj: `str`
        """
        return self.json_data.get('max_atmosphering_speed')

    def get_crew(self) -> str:
        """
        Return a crew of the starship
        :return: Crew
        :type: :obj: `str`
        """
        return self.json_data.get("crew")

    def get_passengers(self) -> str:
        """
        Return a passengers of the starship
        :return: Passengers
        :type: :obj: `str`
        """
        return self.json_data.get("passengers")

    def get_cargo_capacity(self) -> str:
        """
        Return a cargo capacity of the starship
        :return: Capacity
        :type: :obj: `str`
        """
        return self.json_data.get("cargo_capacity")

    def get_consumables(self) -> str:
        """
        Return a consumables of the starship
        :return: Consumables
        :type: :obj: `str`
        """
        return self.json_data.get("consumables")

    def get_hyperdrive_rating(self) -> str:
        """
        Return a hyperdrive_rating of the starship
        :return: Hyperdrive rating
        :type: :obj: `str`
        """
        return self.json_data.get("hyperdrive_rating")

    def get_mglt(self):
        """
        Return a MGLT of the starship
        :return: MGLT
        :type: :obj: `str`
        """
        return self.json_data.get("MGLT")

    def get_starship_class(self) -> str:
        """
        Return a class of the starship
        :return: Class
        :type: :obj: `str`
        """
        return self.json_data.get("starship_class")

    def get_date_created(self) -> str:
        """
        Return a date for created the starship
        :return: Date
        :type: :obj: `str`
        """
        return self.json_data.get("created")

    def get_date_edited(self):
        """
        Return a date for edited the starship
        :return: Date
        :type: :obj: `str`
        """
        return self.json_data.get("edited")

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

    def download_image(self, path_photo: str) -> bool:
        """ The function save  image on your machine
            :param url_path: Name and path to save
            :type url_path: `obj` str
        """
        self.get_photo_ship(self.get_name())
        if BaseRequest._check_status_code(self.image_path):
            with open(path_photo, 'wb') as file:
                file.write(requests.get(self.image_path).content)
            return os.path.exists(path_photo)


if __name__ == "__main__":
    temp = Starship(10)
    print(temp.download_image("test.png"))

try:
    import sys
    import json
    import os.path
    import requests
    from typing import List, Any
    from bs4 import BeautifulSoup
    from src.star_wars.settings import Config
    from star_wars.models.baserequest import BaseRequest
except (Exception,) as e:
    print(sys.exc_info())


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
        self.url_starship = Config.get_url_wiki()

    def get_starship_json(self):
        """ Return all  information about a planet
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
        """
        Return a photo of the starship
            :return: `obj` str
            :type: :obj: `str`
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
            :param path_photo: Name and path to save
            :type path_photo: `obj` str
        """
        self.get_photo_ship(self.get_name())
        if BaseRequest._check_status_code(self.image_path):
            with open(path_photo, 'wb') as file:
                file.write(requests.get(self.image_path).content)
            return os.path.exists(path_photo)

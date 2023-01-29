try:
    import sys
    import json
    import os.path
    import requests
    from lxml import etree
    from typing import List, Any
    from bs4 import BeautifulSoup
    from src.star_wars.settings import Config
    from src.star_wars.utils.baserequest import BaseRequest
except (Exception,) as e:
    print(sys.exc_info())


class People(BaseRequest):
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

    def __init__(self, id_people: int):
        super(People, self).__init__(id_people, Config.get_url_api() + Config.get_people())
        self.image_path = None
        self.id = id_people

    def get_people_json(self):
        """ Return all names and ids of planets of the people
         :return: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self.json_data

    def get_starships(self):
        """
                Return all starships of the people
                :return: Names of all pilots if haves
                :type: :obj: `List[str]`
            """

        starships_names = self._get_items_of_json("pilots", "name", Config.get_url_api() + Config.get_starships())
        return starships_names

    def get_films(self):
        """
            Return all films with the people
            :return: Names of all films with the people
            :type: :obj: `list[str]`
        :return:
        """
        films_names = self._get_items_of_json("characters", "title", Config.get_url_api() + Config.get_films())
        return films_names

    def get_name(self):
        """
            Return a name of the people
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("name")

    def get_height(self):
        """
            Return a height of the people
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("height")

    def get_mass(self):
        """
            Return a mass of the people
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("mass")

    def get_hair_color(self):
        """
            Return a hair color of the people
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("hair_color")

    def get_skin_color(self):
        """
            Return a hair color of the people
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("skin_color")

    def get_eye_color(self):
        """
            Return a eye color of the people
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("eye_color")

    def get_birth_year(self):
        """
            Return a birth year of the people
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("birth_year")

    def get_gender(self):
        """
            Return a gender of the people
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("gender")

    def get_species(self):
        """
            Return a species of the people
            :return: Name
            :type: :obj: `str`
        """
        return self._get_items_of_json("people", "name", Config.get_url_api() + Config.get_species())

    def get_vehicles(self):
        """
            Return a vehicles of the people
            :return: Name
            :type: :obj: `str`
        """
        return self._get_items_of_json("pilots", "name", Config.get_url_api() + Config.get_vehicles())

    def get_date_created(self) -> str:
        """
        Return a date for created the people
        :return: Date
        :type: :obj: `str`
        """
        return self.json_data.get("created")

    def get_date_edited(self):
        """
        Return a date for edited the people
        :return: Date
        :type: :obj: `str`
        """
        return self.json_data.get("edited")

    def get_home_world(self):
        """
        Return a home world the people
        :return: Date
        :type: :obj: `str`
        """
        home = requests.get(self.json_data.get("homeworld")).json().get("name")
        return home


if __name__ == "__main__":
    temp = People(10)
    print(temp.get_vehicles())

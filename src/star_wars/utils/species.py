try:
    import sys
    import json
    import os.path
    import requests
    from typing import List, Any
    from bs4 import BeautifulSoup
    from src.star_wars.settings import Config
    from src.star_wars.models.wiki import Wiki
    from src.star_wars.models.history import History
    from src.star_wars.models.baserequest import BaseRequest
except (Exception,) as e:
    print(sys.exc_info())


class Specie(BaseRequest):
    """
        Class for all specie in world Star Wars.
            Usage:

        .. code-block:: python3
            :caption: Creating instance of StarWars

            from star_wars import star_wars
            specie = Specie(1)
            # and use jedi methods.

            :param: id_specie of a specie, should be obtained from StarWars
            :type id_specie: :obj: `int`
        """

    def __init__(self, id_specie):
        super(Specie, self).__init__(id_specie, Config.get_url_api() + Config.get_species())
        self.id = id_specie
        self.__wiki = Wiki(self.get_name())

    def get_specie_json(self) -> str:
        """ Return all information about a specie
         :return: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self.json_data

    def get_name(self) -> str:
        """
            Return a name of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("name")

    def get_classification(self) -> str:
        """
            Return a classification of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("classification")

    def get_designation(self) -> str:
        """
            Return a designation of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("designation")

    def get_average_height(self) -> str:
        """
            Return  average height of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("average_height")

    def get_skin_colors(self) -> str:
        """
            Return  skin colors of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("skin_colors")

    def get_hair_colors(self) -> str:
        """
            Return  hair colors of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("hair_colors")

    def get_eye_colors(self) -> str:
        """
            Return  eye colors of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("eye_colors")

    def get_average_lifespan(self) -> str:
        """
            Return  average lifespan of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("average_lifespan")

    def get_language(self) -> str:
        """
            Return  language of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("language")

    def get_home_world(self):
        """
        Return a home world the people
        :return: Date
        :type: :obj: `str`
        """
        home = None
        if self.json_data.get("homeworld") is not None:
            home = requests.get(self.json_data.get("homeworld")).json().get("name")
        return home

    def get_date_created(self) -> str:
        """
        Return a date for created the specie
        :return: Date
        :type: :obj: `str`
        """
        return self.json_data.get("created")

    def get_date_edited(self) -> str:
        """
        Return a date for edited the specie
        :return: Date
        :type: :obj: `str`
        """
        return self.json_data.get("edited")

    def get_people(self) -> list[Any]:
        """
            Return all pilots of the starships
            :return: Names of all pilots if haves
            :type: :obj: `List[str]`
        """
        pilot_names = self._get_items_of_json("species", "name", Config.get_url_api() + Config.get_people())
        return pilot_names

    def get_films(self) -> list[Any]:
        """
            Return all films with the starship
            :return: Names of all films with the starship
            :type: :obj: `list[str]`
        :return:
        """
        films_names = self._get_items_of_json("species", "title", Config.get_url_api() + Config.get_films())
        return films_names

    def save_image(self, path_photo="") -> dict[str:bool]:
        """
        The function save image on your machine
        :param path_photo: Path to save default = ""
        :return: Name photo and True is photo saved else False
        :type: :obj: `dic[str:bool]`
        """
        return self.__wiki.download_image(path_photo)
    def get_description(self) -> str:
        """
        The function get your description about the specie
        :return: Description
        :type: :obj: `str`
        """
        return  self.__wiki.get_descriptions()


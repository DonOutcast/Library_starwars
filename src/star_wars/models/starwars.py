import requests

try:
    import sys
    import time
    import json
    from src.star_wars.settings import Config
    from src.star_wars.exceptions import ResourceDoesNotExists
    from src.star_wars.utils_1 import query, all_resource_urls
except (Exception,):
    print(sys.exc_info())


class StarWars:
    """
    Class for all names and ids in world Star Wars.
        Usage:

    .. code-block:: python3
        :caption: Creating instance of StarWars

        from star_wars import star_wars
        jedi = StarWars
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
    def _get_response(url_path: str, name_key: str) -> dict[str, int]:
        """ Return a response to url
         :param: url_path
         :type: :obj: `str`
         :param: name_key this is a key of value
         :type: :obj: `str`
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
        return self._get_response(self.__url_people, name_key="name")

    def get_planets_names(self):
        """ Return all names and ids of planets
         :returns: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self._get_response(self.__url_planets, name_key="name")

    def get_films_names(self):
        """ Return all names and ids of films
         :returns: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self._get_response(self.__url_films, name_key="title")

    def get_species_names(self):
        """ Return all names and ids of species
         :returns: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self._get_response(self.__url_species, name_key="name")

    def get_vehicles_names(self):
        """ Return all names and ids of vehicles
         :returns: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self._get_response(self.__url_vehicles, name_key="name")

    def get_starships_names(self):
        """ Return all names and ids of starships
         :returns: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self._get_response(self.__url_starships, name_key="name")

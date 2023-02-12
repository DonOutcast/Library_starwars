try:
    import sys
    import json
    import os.path
    import requests
    from typing import List, Any
    from bs4 import BeautifulSoup
    from src.star_wars.settings import Config
    from src.star_wars.models.wiki import Wiki
    from src.star_wars.utils.people import People
    from src.star_wars.models.history import History
    from src.star_wars.models.baserequest import BaseRequest
except (Exception,) as e:
    print(sys.exc_info())


class Film(BaseRequest):
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
        super(Film, self).__init__(id_specie, Config.get_url_api() + Config.get_films())
        self.id = id_specie
        # self.__wiki = Wiki(self.get_name())

    def get_characters(self) -> list[str]:
        """
        The function get all characters in the films
        :return: Names characters
        :type: :obj: `str`
        """
        return self._get_items_of_json("films", "name", Config.get_url_api() + Config.get_people())

    def get_starships(self) -> list[str]:
        """
        The function get all starshps in the films
        :return: Names characters
        :type: :obj: `str`
        """
        return self._get_items_of_json("films", "name", Config.get_url_api() + Config.get_starships())

    def get_vehicles(self) -> list[str]:
        """
        The function get all vehicles in the films
        :return: Names of vehicles
        :type: :obj: `str`
        """
        # return self._get_items_of_json("films", "name", Config.get_url_api() + Config.get_vehicles())
        return self._search_items("vehicles", "name")

    def get_species(self) -> list[str]:
        """
        The function get all vehicles in the films
        :return: Names of species
        :type: :obj: `str`
        """
        # return self._get_items_of_json("films", "name", Config.get_url_api() + Config.get_species())
        return self._search_items("species", "name")

    def get_planets(self) -> list[str]:
        """
        The function get all characters in the planets
        :return: Names characters
        :type: :obj: `str`
        """

        # return self._get_items_of_json("films", "name", Config.get_url_api() + Config.get_planets())
        return self._search_items("planets", "name")

    def get_name(self) -> str:
        """
        The function get a name of film
        :return: Name of film
        :type: :obj: `str`
        """
        return self.json_data.get("title")

    def get_episode(self) -> str:
        """
        The function get a episode of film
        :return: Episode of film
        :type: :obj: `str`
        """
        return self.json_data.get("episode_id")

    def get_opening_crawl(self) -> str:
        """
        The function get a opening crawl of film
        :return: Episode of film
        :type: :obj: `str`
        """
        return self.json_data.get("opening_crawl")

    def get_director(self) -> str:
        """
        The function get a director of film
        :return: Director of film
        :type: :obj: `str`
        """
        return self.json_data.get("director")

    def get_producer(self) -> str:
        """
        The function get a producer of film
        :return: Director of film
        :type: :obj: `str`
        """
        return self.json_data.get("producer")

    def get_release_date(self) -> str:
        """
        The function get a release date of film
        :return: Director of film
        :type: :obj: `str`
        """
        return self.json_data.get("release_date")

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
    from src.star_wars.utils.baserequest import BaseRequest
except (Exception,) as e:
    print(sys.exc_info())


class Vehicles(BaseRequest):
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
        super(Vehicles, self).__init__(id_specie, Config.get_url_api() + Config.get_vehicles())
        self.id = id_specie
        # self.__wiki = Wiki(self.get_name())

    def get_vehicle_json(self):

        return self.json_data
    def get_films(self) -> list[str]:
        """
        The function get all characters in the films
        :return: Names characters
        :type: :obj: `str`
        """
        return self._search_items("films", "title")

    def get_pilots(self) -> list[str]:
        """
        The function get all pilots
        :return: Names characters
        :type: :obj: `str`
        """
        # return self._get_items_of_json("vehicles", "name", Config.get_url_api() + Config.get_people())
        return self._search_items("pilots", "name")




if __name__ == "__main__":
    vehicles = Vehicles(14)
    print(vehicles.get_films())
    print(vehicles.get_pilots())

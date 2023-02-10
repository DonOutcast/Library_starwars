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
        self.__wiki = Wiki(self.get_name())

    def get_vehicle_json(self):

        return self.json_data

    def get_name(self):
        """
            Return a name of the vehicle
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("name")

    def get_model(self):
        """
            Return a name of the model
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("model")

    def get_manufacturer(self):
        """
            Return a name of the manufacturer
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("manufacturer")

    def get_cost_in_credits(self):
        """
            Return a name of the cost in credits
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("cost_in_credits")
    def get_length(self):
        """
            Return a name of the length
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("length")

    def get_max_atmosphering_speed(self):
        """
            Return a name of the max atmosphering speed
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("max_atmosphering_speed")

    def get_crew(self):
        """
            Return a name of the crew
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("crew")
    def get_passengers(self):
        """
            Return a name of the passengers
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("passengers")

    def get_cargo_capacity(self):
        """
            Return a name of the cargo_capacity
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("cargo_capacity")

    def get_consumables(self):
        """
            Return a name of the cargo_capacity
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("consumables")

    def get_vehicle_class(self):
        """
            Return a name of the vehicle class
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("vehicle_class")

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
        return self._search_items("pilots", "name")

    def get_date_created(self) -> str:
        """
        Return a date for created
        :return: Date
        :type: :obj: `str`
        """
        return self.json_data.get("created")

    def get_date_edited(self):
        """
        Return a date for edited
        :return: Date
        :type: :obj: `str`
        """
        return self.json_data.get("edited")

    def get_descriptions(self) -> str:
        """
        This function get a description of the vehicle
        :return: Description
        :type: :obj: `str`
        """
        return self.__wiki.get_descriptions()

if __name__ == "__main__":
    vehicles = Vehicles(14)
    print(vehicles.get_descriptions())


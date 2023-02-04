try:
    import sys
    import json
    import os.path
    import requests
    from lxml import etree
    from typing import List, Any
    from bs4 import BeautifulSoup
    from src.star_wars.settings import Config
    from src.star_wars.models.history import History
    from src.star_wars.utils.baserequest import BaseRequest
except (Exception,) as e:
    print(sys.exc_info())

class Planet(BaseRequest):
    """
            Class for all planets in world Star Wars.
                Usage:

            .. code-block:: python3
                :caption: Creating instance of StarWars

                from star_wars import star_wars
                planet = Planet(1)
                # and use jedi methods.

                :param id_planet: of a starship, should be obtained from StarWars
                :type id_planet: :obj: `int`
            """
    def __init__(self, id_planet):
        super(Planet, self).__init__(id_planet, Config.get_url_api() + Config.get_planets())
        self.id = id_planet
        self.photos_of_history = []
        self.__history = History(self.get_name())

    def get_planet_json(self) -> str:
        """ Return all information about a planet
         :return: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self.json_data
    def get_name(self) -> str:
        """
            Return a name of the planet
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("name")

    def get_rotation_period(self) -> str:
        """
            Return a  rotation period in planet of planet
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("rotation_period")
    def get_orbital_period(self) -> str:
        """
            Return a  rotation orbital period of planet
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("orbital_period")

    def get_diameter(self) -> str:
        """
            Return a  diameter of planet
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("diameter")

    def get_climate(self) -> str:
        """
            Return a  diameter of planet
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("climate")

    def get_gravity(self) -> str:
        """
            Return a  gravity of planet
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("gravity")

    def get_terrain(self) -> str:
        """
            Return a  terrain of planet
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("terrain")
    def get_surface_water(self) -> str:
        """
            Return  surface water of planet
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("surface_water")

    def get_population(self) -> str:
        """
            Return  population of planet
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("population")

    def get_residents(self) -> list[Any]:
        """
            Return  residents of planet
            :return: Name
            :type: :obj: `str`
        """
        residents_names = self._get_items_of_json("homeworld", "name", Config.get_url_api() + Config.get_people())
        return residents_names

    def get_films(self) -> list[Any]:
        """
            Return all films with the starship
            :return: Names of all films with the starship
            :type: :obj: `list[str]`
        :return:
        """
        films_names = self._get_items_of_json("planets", "title", Config.get_url_api() + Config.get_films())
        return films_names

    def get_date_created(self) -> str:
        """
        Return a date for created the planet
        :return: Date
        :type: :obj: `str`
        """
        return self.json_data.get("created")

    def get_date_edited(self) -> str:
        """
        Return a date for edited the planet
        :return: Date
        :type: :obj: `str`
        """
        return self.json_data.get("edited")

    def save_image(self, path_to_image="") -> bool:
        """Save the image to your directory
        :param path_to_image: A file link to
        :type path_to_image: str
        :returns: If the file saved successfully True else False
        :rtype: bool
        """
        return self.__history.save_image(path_to_image)

if __name__ == "__main__":
    planet = Planet(9)
    print(planet.get_films())
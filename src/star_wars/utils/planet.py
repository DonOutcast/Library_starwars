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
if __name__ == "__main__":
    planet = Planet(9)
    print(planet.get_population())
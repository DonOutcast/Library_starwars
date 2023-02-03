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
        super(Planet, self).__init__(id_planet, Config.get_url_api() + Config.get_species())
        self.id = id_planet

    def get_planet_json(self) -> str:
        """ Return all information about a planet
         :return: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self.json_data
if __name__ == "__main__":
    planet = Planet(9)
    print(planet.get_planet_json())
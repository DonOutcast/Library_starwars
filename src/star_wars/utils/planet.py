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
            Class for all names and ids in world Star Wars.
                Usage:

            .. code-block:: python3
                :caption: Creating instance of StarWars

                from star_wars import star_wars
                planet = Planet(1)
                # and use jedi methods.

                :param id_starship: of a starship, should be obtained from StarWars
                :type id_starship: :obj: `int`
            """

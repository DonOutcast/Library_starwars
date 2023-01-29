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


if __name__ == "__main__":
    temp = People(10)
    print(temp.get_people_json())
    print(len(temp.all_jsons))

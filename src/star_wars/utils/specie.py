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


class Specie(BaseRequest):
    """
        Class for all specie world Star Wars.
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

    def get_specie_json(self):
        """ Return all information about a specie
         :return: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self.json_data

    def get_name(self):
        """
            Return a name of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("name")

    def get_classification(self):
        """
            Return a classification of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("classification")

    def get_designation(self):
        """
            Return a designation of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("designation")

    def get_average_height(self):
        """
            Return  average height of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("average_height")

    def get_skin_colors(self):
        """
            Return  skin colors of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("skin_colors")

    def get_hair_colors(self):
        """
            Return  hair colors of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("hair_colors")

    def get_eye_colors(self):
        """
            Return  eye colors of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("eye_colors")

    def get_average_lifespan(self):
        """
            Return  average lifespan of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("average_lifespan")

    def get_language(self):
        """
            Return  language of the specie
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("language")


if __name__ == "__main__":
    temp = Specie(2)
    print(temp.get_language())

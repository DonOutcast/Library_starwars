try:
    import sys
    import json
    import os.path
    import requests
    from lxml import etree
    from typing import List, Any
    from bs4 import BeautifulSoup
    from src.star_wars.settings import Config
    from src.star_wars.models.starwars import StarWars
    from src.star_wars.utils.baserequest import BaseRequest
except (Exception,) as e:
    print(sys.exc_info())


class Wiki:

    def __init__(self, name_for_searching: str, url_path: str):
        self.name_for_searching = name_for_searching
        self.url_path = url_path

    def get_descriptions(self, name: str) -> str:
        """ Return a descriptions of the ship
            :return: `obj` str
            :type:
        """
        my_response = requests.get(self.url_starship + name.replace(" ", "_"))
        my_soup = BeautifulSoup(my_response.content, "lxml").select("div.mw-parser-output > p")
        result = ""
        for p in my_soup:
            if "<aside" in str(p):
                continue
            else:
                result = p.text
                break
        return result.strip()

    def get_photo_ship(self, name: str) -> str:
        """
        Return a photo of the starship
            :return: `obj` str
            :type: :obj: `str`
        """
        my_response = requests.get(self.url_starship + name.replace(" ", "_"))
        my_soup = BeautifulSoup(my_response.content, "lxml").select("div.mw-parser-output > p")
        result = ""
        for p in my_soup:
            if "<aside" in str(p):
                result = p.select_one("img.pi-image-thumbnail").get("src")
                break
            else:
                result = my_soup.select_one("img.thumbimage").get("data-src")
                break
        self.image_path = result
        return result

    def download_image(self, path_photo: str) -> bool:
        """ The function save  image on your machine
            :param path_photo: Name and path to save
            :type path_photo: `obj` str
        """
        self.get_photo_ship(self.get_name())
        if BaseRequest._check_status_code(self.image_path):
            with open(path_photo, 'wb') as file:
                file.write(requests.get(self.image_path).content)
            return os.path.exists(path_photo)

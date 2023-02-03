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

    def __init__(self, name_for_searching: str):
        self.name_for_searching = self.replace_name(name_for_searching)
        self.url_path = Config.get_url_wiki()


    @staticmethod
    def replace_name(name) -> str:
        """
        The function change a name to actually name in url
        :name_for_change: Any name
        :type: :obj: `str`
        :return Name
        :type: :obj: `str`
        """
        return name.replace(" ", "_")

    def get_descriptions(self) -> str:
        """ Return a descriptions of the ship
            :return: `obj` str
            :type:
        """
        my_response = requests.get(self.url_path + self.name_for_searching)
        my_soup = BeautifulSoup(my_response.content, "lxml").select("div.mw-parser-output > p")
        result = ""
        for p in my_soup:
            if "<aside" in str(p):
                continue
            else:
                result = p.text
                break
        return result.strip()

    def get_photo_wiki(self) -> str:
        """
        Return a photo of the starship
            :return: `obj` str
            :type: :obj: `str`
        """
        my_response = requests.get(self.url_path + self.name_for_searching)
        if self.name_for_searching == "Droid":
            my_soup = BeautifulSoup(my_response.content, "html.parser")
        else:
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

    def get_specie_photo(self):
        my_response = requests.get(self.url_path + self.name_for_searching)
        # my_soup = BeautifulSoup(my_response.content, "lxml")
        my_soup = BeautifulSoup(my_response.content, "html.parser")
        result = []
        for p in my_soup:
            if "<aside" in str(p):
                result.append(p.select_one("img.pi-image-thumbnail").get("src"))
                break
            else:
                result.append(my_soup.select_one("img.thumbimage").get("data-src"))
                break
        self.image_path = result
        return result
    def download_image(self, path_photo: str = "") -> bool:
        """ The function save  image on your machine
            :param path_photo: Name and path to save
            :type path_photo: `obj` str
        """
        self.get_photo_wiki()
        if BaseRequest._check_status_code(self.image_path):
            with open(path_photo, 'wb') as file:
                file.write(requests.get(self.image_path).content)
            return os.path.exists(path_photo)


if __name__ == "__main__":
    # payload = {"search_q": "Pau'an"}
    # response = requests.get("https://www.starwars.com/search?q=Droid")
    # soup = BeautifulSoup(response.content, "html.parser")
    # for element in soup.find_all('div', {'class': 'title'}):
    #     print(element.a)
    # wiki = Wiki("Y-wing")
    wiki = Wiki("Droid")
    # wiki = Wiki("Wookie")
    # wiki = Wiki("Pau'an")
    print(wiki.get_photo_wiki())

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


class History:

    def __init__(self, name_for_searching):
        self.name_for_searching = self.replace_name(name_for_searching)
        self.photos_of_history = []
        self.history_text_after_photo = []
        self.byte_code_of_photos = []
        response = requests.get(Config.get_url_star_wars() + self.name_for_searching)
        self.soup = BeautifulSoup(response.content, "html.parser")

    @staticmethod
    def replace_name(name) -> str:
        """
        The function change a name to actually name in url
        :name_for_change: Any name
        :type: :obj: `str`
        :return Name
        :type: :obj: `str`
        """
        return name.replace(" ", "-")

    def get_description(self) -> list:
        """
        The function search
        :return:
        """
        return self.soup.find("p", {"class": "desc"}).text

    def get_after_photo(self):
        self.soup.find("div", {"class": "rich-text-output"}).find_all("div", {"class": "media-image-inline"})
        for i in self.soup.find("div", {"class": "rich-text-output"}).find_all("p"):
            if i.text != "":
                self.history_text_after_photo.append(i.text)
        return self.history_text_after_photo

    def search_history_photo(self) -> None:
        """
        The function search all photo in history block about a people
        :return: None
        :type: :obj: `None`
        """
        for i in self.soup.find("div", {"class": "rich-text-output"}).find_all("div", {"class": "media-image-inline"}):
            self.photos_of_history.append(i.find("img").get("src"))

    def get_photos_of_history(self) -> list:
        """
        Return all photos at history people in url path
        :return: Url paths
        :type: :obj: `list`
        """
        self.search_history_photo()
        return self.photos_of_history

    def save_history_photos(self, path="") -> list[bool]:
        """
        The function save all photos at block history
        :return: None
        :type: :obj: `None`
        """
        count = 0
        result = []
        for i in self.get_photos_of_history():
            path_photo = path + self.name_for_searching + str(count) + ".png"
            try:
                with open(path_photo, "wb") as f:
                    f.write(requests.get(i).content)
                    result.append(os.path.exists(path_photo))
            except Exception as error:
                print(error)
            count += 1
        return result

    def _generation_byte_code_photos(self) -> None:
        """
        The function a generation all byte code of photo
        :return: None
        :type: :obj: `None`
        """
        try:
            for bytes_photo in self.get_photos_of_history():
                self.byte_code_of_photos.append(requests.get(bytes_photo).content)
        except Exception as error:
            print(error)

    def get_byte_code_of_photos(self) -> list[Any]:
        """
        Retturn a byte  code of photo
        :return: Bytes
        :type: :obj: `list[Any]`
        """
        self._generation_byte_code_photos()
        return self.byte_code_of_photos


if __name__ == "__main__":
    temp = History("Leia Organa")
    print(len(temp.get_byte_code_of_photos()))
    # print(temp.save_history_photos(""))

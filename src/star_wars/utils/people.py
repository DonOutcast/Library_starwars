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


class People(BaseRequest):
    """
        Class for all people in world Star Wars.
            Usage:

        .. code-block:: python3
            :caption: Creating instance of StarWars

            from star_wars import star_wars
            people = People(2)
            # and use jedi methods.

            :param: id_people of a people, should be obtained from StarWars
            :type id_people: :obj: `int`
        """

    def __init__(self, id_people: int):
        super(People, self).__init__(id_people, Config.get_url_api() + Config.get_people())
        self.image_path = None
        self.id = id_people
        self.photos_of_history = []
        self.__history = History(self.get_name())

    def get_people_json(self):
        """ Return all names and ids of planets of the people
         :return: Response to url in a dictionary
         :type: dict[str, int]
        """
        return self.json_data

    def get_starships(self):
        """
                Return all starships of the people
                :return: Names of all pilots if haves
                :type: :obj: `List[str]`
            """

        starships_names = self._get_items_of_json("pilots", "name", Config.get_url_api() + Config.get_starships())
        return starships_names

    def get_films(self):
        """
            Return all films with the people
            :return: Names of all films with the people
            :type: :obj: `list[str]`
        :return:
        """
        films_names = self._get_items_of_json("characters", "title", Config.get_url_api() + Config.get_films())
        return films_names

    def get_name(self):
        """
            Return a name of the people
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("name")

    def get_height(self):
        """
            Return a height of the people
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("height")

    def get_mass(self):
        """
            Return a mass of the people
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("mass")

    def get_hair_color(self):
        """
            Return a hair color of the people
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("hair_color")

    def get_skin_color(self):
        """
            Return a hair color of the people
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("skin_color")

    def get_eye_color(self):
        """
            Return a eye color of the people
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("eye_color")

    def get_birth_year(self):
        """
            Return a birth year of the people
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("birth_year")

    def get_gender(self):
        """
            Return a gender of the people
            :return: Name
            :type: :obj: `str`
        """
        return self.json_data.get("gender")

    def get_species(self):
        """
            Return a species of the people
            :return: Name
            :type: :obj: `str`
        """
        return self._get_items_of_json("people", "name", Config.get_url_api() + Config.get_species())

    def get_vehicles(self):
        """
            Return a vehicles of the people
            :return: Name
            :type: :obj: `str`
        """
        return self._get_items_of_json("pilots", "name", Config.get_url_api() + Config.get_vehicles())

    def get_date_created(self) -> str:
        """
        Return a date for created the people
        :return: Date
        :type: :obj: `str`
        """
        return self.json_data.get("created")

    def get_date_edited(self):
        """
        Return a date for edited the people
        :return: Date
        :type: :obj: `str`
        """
        return self.json_data.get("edited")

    def get_home_world(self):
        """
        Return a home world the people
        :return: Date
        :type: :obj: `str`
        """
        home = None
        if self.json_data.get("homeworld") is not None:
            home = requests.get(self.json_data.get("homeworld")).json().get("name")
        return home

    @staticmethod
    def get_url_image(url_person: str) -> str:
        new_url = Config.get_url_star_wars() + url_person.replace(' ', '-')
        response = requests.get(new_url)
        soup = BeautifulSoup(response.content, "html.parser")
        result = soup.find("div", class_="image-wrapper").find("img").get("data-src")
        return result

    def save_image(self, person_name: str, path_to_image) -> bool:
        """Save the image to your directory
        :param person_name: The file location and name
        :type person_name: str
        :param path_to_image: A file link to
        :type path_to_image: str
        :returns: If the file saved successfully True else False
        :rtype: bool
        """
        try:
            with open(person_name + ".png", "wb") as f:
                f.write(requests.get(path_to_image).content)
        except Exception as error:
            print(error)
            return False
        else:
            return True

    def get_description(self) -> list[Any]:
        """
        The function search
        :return:
        """
        return self.__history.get_description()

    def get_after_photo(self) -> list[Any]:
        return self.__history.get_after_photo()

    def get_photos_of_history(self) -> list:
        """
        Return all photos at history people in url path
        :return: Url paths
        :type: :obj: `list`
        """
        return self.__history.get_photos_of_history()

    def save_history_photos(self, path="") -> list[bool]:
        """
        The function save all photos at block history
        :return: None
        :type: :obj: `None`
        """
        return self.__history.save_history_photos(path)

# if __name__ == "__main__":
#     temp = People(2)
# print(temp.save_image(temp.get_name(), temp.get_url_image(temp.get_name())))

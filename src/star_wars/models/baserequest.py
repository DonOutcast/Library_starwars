try:
    import sys
    import json
    import requests
    from typing import List, Any
    from src.star_wars.exceptions import ResourceDoesNotExists
except (Exception,) as e:
    print(sys.exc_info())


class BaseRequest:
    """
    The Class generate response with json
    :param id_search: id of people or starships or planets or films or species or vehicles
    :type id_search: :obj: `int`
    :param url_path: the path from Config
    :type url_path: :obj: `str`
    :return: If status code request is 200 a json data or Exception
    :type: :obj: `json`
    """

    def __init__(self, id_search: int, url_path: str) -> None:
        response_json = self.__query("{0}/{1}".format(url_path, id_search))
        self.json_data = response_json.json()
        self.url_path = url_path
        self.all_jsons = []
        # self.all_pages(url_path)

    def __query(self, query):
        headers = {'User-Agent': 'swapi-python'}
        response = requests.get(query, headers=headers)
        if response.status_code != 200:
            raise ResourceDoesNotExists
        return response

    @staticmethod
    def _check_status_code(url_path):
        """
        The function a check status code of get or post requests
        :param url_path: Url path
        :type: :obj:  `str`
        :return: True if status code == 200 else raise
        :type: :obj: `bool`
        """
        status = requests.get(url_path)
        if status.status_code != 200:
            raise ResourceDoesNotExists
        return True

    def _get_items_of_json(self, key_class: str, key_tag, url_path: str) -> list[Any]:
        """ Return all pilots of the starship
            :param key_class: Word for search example  starships, films
            :type key_class: :obj: `str`
            :param key_tag: Word for search in json example name, title
            :type key_tag: :obj: `str`
            :param url_path: Url for page in API
            :type url_path: :obj: `str`
            :return: List of names
            :type: list[str]
        """
        running = True
        names = []
        while running:
            my_response = requests.get(url_path)
            if my_response.status_code != 200:
                raise ResourceDoesNotExists
            json_data = json.loads(my_response.content)
            for resource in json_data["results"]:
                if not isinstance(resource.get(key_class), list):
                    if resource.get(key_class).split("/")[-2] == str(self.id):
                        names.append(resource.get(key_tag))
                else:
                    for starship in resource.get(key_class):
                        if starship.split("/")[-2] == str(self.id):
                            names.append(resource.get(key_tag))
            if bool(json_data.get("next")):
                url_path = json_data["next"]
            else:
                running = False
        return names

    def _all_pages(self, url_path) -> None:
        """

        :param url_path:
        :return:
        """
        self._check_status_code(url_path)
        response = requests.get(url_path)
        json_data = response.json()
        if json_data.get("next"):
            url_path = json_data.get("next")
            self.all_jsons.append(json_data)
            return BaseRequest._all_pages(self, url_path)

    def get_all_jsons(self) -> list:
        """
        Get jsons date
        :return: All jsons
        :type: :obj: `list`
        """
        self._all_pages(self.url_path)
        return self.all_jsons

    def _search_items(self, key_one, key_two):
        my_list = []
        for url_i in self.json_data.get(key_one):
            if self._check_status_code(url_i):
                my_response = requests.get(url_i).json()
                my_list.append(my_response.get(key_two))
        return my_list

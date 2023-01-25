import requests

try:
    import sys
    import time
    import json
    from src.star_wars.settings import Config
    from src.star_wars.exceptions import ResourceDoesNotExists
    from src.star_wars.utils_1 import query, all_resource_urls
except (Exception,):
    print(sys.exc_info())


class BaseModel:
    """The class convert your byte string to json """

    def __init__(self, raw_data: bytes) -> None:
        """The base constructor add to all keys and values to attribute of class
        :param: raw_data bytes
        :type: bytes
        :returns: None
        :type: None
        """
        json_data = json.loads(raw_data)
        setattr(self, "json", json_data)
        for key, value in json_data.items():
            # print(key, value)
            setattr(self, key, value)


class BaseQuerySet:
    def __init__(self):
        self.items = []

    def order_by(self, order_attribute):
        result = []
        for i in sorted(self.items, key=lambda i: getattr(i, order_attribute)):
            result.append(i)
        return result

    def count(self):
        return len(self.items)

    def iter(self):
        for i in self.items:
            yield i


class StarshipQuerySet(BaseQuerySet):

    def __init__(self, list_of_urls):
        super(StarshipQuerySet, self).__init__()
        for url in list_of_urls:
            response = query(url)
            self.items.append(Starship(response.content))

    def __repr__(self):
        return "StarshipQuerySet - {0}".format(str(len(self.items)))


def _get(id, type, conf):
    ''' Return a single person '''
    result = query("{0}/{1}/{2}/".format(
        conf.get_url_api(),
        type,
        str(id))
    )
    return result


def get_starship(starship_id, conf):
    """ Return a single starship """
    result = _get(starship_id, conf.get_starships(), conf)
    return Starship(result.content)


class Starship(BaseModel):

    def __init__(self, raw_data):
        super(Starship, self).__init__(raw_data)

    def get_json(self):
        """The function is a return json"""
        return self.json

    def __repr__(self):
        return '<Starship - {0}>'.format(self.name)

    # def get_films(self):
    # return FilmQuerySet(self.films)
    #
    # def get_pilots(self):
    # return PeopleQuerySet(self.pilots)


def get_all(resource):
    """ Return all of a single resource """
    query_sets = {
        # conf.get_people(): PeopleQuerySet,
        # conf.get_planets(): PlanetQuerySet,
        conf.get_starships(): StarshipQuerySet,
        # conf.get_vehicles(): VehicleQuerySet,
        # conf.get_species(): SpeciesQuerySet,
        # conf.get_films(): FilmQuerySet
    }
    urls = all_resource_urls(
        "{0}/{1}/".format(conf.get_url_api(), resource)
    )

    return query_sets[resource](urls)


conf = Config()


# temp = get_starship(2, conf)
# print(temp.get_json())

# ships = get_all("starships")
# all_resource_urls("{0}/{1}/".format(conf.get_url_api(), "people"))


# order = ships.iter()
# print(type(ships))
# def get_all_names_and_id(query):
#     running = True
#     names = {}
#     while running:
#         response = requests.get(query)
#         json_data = json.loads(response.content)
#         for resource in json_data["results"]:
#             names[resource["name"]] = resource["url"].split("/")[-2]
#         if bool(json_data["next"]):
#             query = json_data["next"]
#         else:
#             running = False
#     return names
#
#
# print(get_all_names_and_id("{0}/{1}/".format(conf.get_url_api(), "people")))
def _get(id, type, conf):
    ''' Return a single person '''
    result = query("{0}/{1}/{2}/".format(
        conf.get_url_api(),
        type,
        str(id))
    )
    return result


def get_starship(starship_id, conf):
    """ Return a single starship """
    result = _get(starship_id, conf.get_starships(), conf)
    return Starship(result.content)



# class T:
#     def __init__(self, name):
#         name += '3'
#         self.name = name
#
#
# class A(T):
#     def __init__(self, name):
#         super(A, self).__init__(name)
#         self.tem = name
#
#
# a = A("Shamil")
# print(a.tem)

# READY
# import json
# import requests
# from settings import Config
#
#
#
# class StarWars:
#     """
#     Class for all names and ids in world Star Wars.
#         Usage:
#
#     .. code-block:: python3
#         :caption: Creating instance of StarWars
#
#         from star_wars import star_wars
#         jedi = StarWars(
#         # and use jedi methods.
#     """
#
#     def __init__(self):
#         self.__url_people = Config.get_url_api() + Config.get_people()
#         self.__url_planets = Config.get_url_api() + Config.get_planets()
#         self.__url_films = Config.get_url_api() + Config.get_films()
#         self.__url_species = Config.get_url_api() + Config.get_species()
#         self.__url_vehicles = Config.get_url_api() + Config.get_vehicles()
#         self.__url_starships = Config.get_url_api() + Config.get_starships()
#
#     @staticmethod
#     def get_response(url_path: str, name_key: str) -> dict[str, int]:
#         """ Return a response to url
#          :param: url_path str
#          :type: str
#          :param: name_key this is a key of value
#          :type: str
#          :returns: Response to url in a dictionary
#          :type: dict[str, int]
#         """
#         running = True
#         names = {}
#         while running:
#             my_response = requests.get(url_path)
#             if my_response.status_code != 200:
#                 raise ResourceDoesNotExists
#             json_data = json.loads(my_response.content)
#             for resource in json_data["results"]:
#                 names[resource.get(name_key)] = resource.get("url").split("/")[-2]
#             if bool(json_data.get("next")):
#                 url_path = json_data["next"]
#             else:
#                 running = False
#         return names
#
#     def get_people_names(self):
#         """ Return all names and ids of people
#          :returns: Response to url in a dictionary
#          :type: dict[str, int]
#         """
#         return self.get_response(self.__url_people, name_key="name")
#
#     def get_planets_names(self):
#         """ Return all names and ids of planets
#          :returns: Response to url in a dictionary
#          :type: dict[str, int]
#         """
#         return self.get_response(self.__url_planets, name_key="name")
#
#     def get_films_names(self):
#         """ Return all names and ids of films
#          :returns: Response to url in a dictionary
#          :type: dict[str, int]
#         """
#         return self.get_response(self.__url_films, name_key="title")
#
#     def get_species_names(self):
#         """ Return all names and ids of species
#          :returns: Response to url in a dictionary
#          :type: dict[str, int]
#         """
#         return self.get_response(self.__url_species, name_key="name")
#
#     def get_vehicles_names(self):
#         """ Return all names and ids of vehicles
#          :returns: Response to url in a dictionary
#          :type: dict[str, int]
#         """
#         return self.get_response(self.__url_vehicles, name_key="name")
#
#     def get_starships_names(self):
#         """ Return all names and ids of starships
#          :returns: Response to url in a dictionary
#          :type: dict[str, int]
#         """
#         return self.get_response(self.__url_starships, name_key="name")

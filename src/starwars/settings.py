import sys

try:
    import sys
    from dataclasses import dataclass
    from typing import Optional
except (Exception,):
    print(sys.exc_info())


@dataclass
class Config:
    """The class for base settings of parser"""
    __base_url_api: Optional[str] = "https://swapi.dev/api/"
    __base_url_star_wars: Optional[str] = "https://www.starwars.com/databank/"
    __people: Optional[str] = "people"
    __planets: Optional[str] = "planets"
    __starships: Optional[str] = "starships"
    __vehicles: Optional[str] = "vehicles"
    __films: Optional[str] = "films"
    __species: Optional[str] = "species"

    @staticmethod
    def get_url_api() -> str:
        """Getting a base url star_wars
        :returns: Url
        :rtype: str
        """
        return Config.__base_url_api

    @staticmethod
    def get_url_star_wars() -> str:
        """Getting a base url star_wars
        :returns: Url
        :rtype: str
        """
        return Config.__base_url_star_wars

    @staticmethod
    def get_people() -> str:
        """Getting a base url star_wars
        :returns: People
        :rtype: str
        """
        return Config.__people

    @staticmethod
    def get_planets() -> str:
        """Getting a base url star_wars
        :returns: Planets
        :rtype: str
        """
        return Config.__planets

    @staticmethod
    def get_starships() -> str:
        """Getting a base url star_wars
        :returns: Starships
        :rtype: str
        """
        return Config.__starships

    @staticmethod
    def get_vehicles() -> str:
        """Getting a base url star_wars
        :returns: Vehicles
        :rtype: str
        """
        return Config.__vehicles

    @staticmethod
    def get_films() -> str:
        """Getting a base url star_wars
        :returns: Films
        :rtype: str
        """
        return Config.__films

    @staticmethod
    def get_species() -> str:
        """Getting a base url star_wars
        :returns: species
        :rtype: str
        """
        return Config.__species

    def __str__(self):
        return f"In This class all variables to parse "

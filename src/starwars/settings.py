import sys

try:
    import sys
    from pydantic import BaseModel
    from typing import Optional
except (Exception,):
    print(sys.exc_info())


class Config(BaseModel):
    """The class for base settings of parser"""
    __base_url_api: Optional[str] = "https://swapi.dev/api"
    __base_url_star_wars: Optional[str] = "https://www.starwars.com/databank/"
    __people: Optional[str] = "people"
    __planets: Optional[str] = "planets"
    __starships: Optional[str] = "starships"
    __vehicles: Optional[str] = "vehicles"
    __films: Optional[str] = "films"
    __species: Optional[str] = "species"

    def get_url_api(self) -> str:
        """Getting a base url star_wars
        :returns: Url
        :rtype: str
        """
        return self.__base_url_api

    def get_url_star_wars(self) -> str:
        """Getting a base url star_wars
        :returns: Url
        :rtype: str
        """
        return self.__base_url_star_wars

    def get_people(self) -> str:
        """Getting a base url star_wars
        :returns: People
        :rtype: str
        """
        return self.__people

    def get_planets(self) -> str:
        """Getting a base url star_wars
        :returns: Planets
        :rtype: str
        """
        return self.__planets

    def get_starships(self) -> str:
        """Getting a base url star_wars
        :returns: Starships
        :rtype: str
        """
        return self.__starships

    def get_vehicles(self) -> str:
        """Getting a base url star_wars
        :returns: Vehicles
        :rtype: str
        """
        return self.__vehicles

    def get_films(self) -> str:
        """Getting a base url star_wars
        :returns: Films
        :rtype: str
        """
        return self.__films

    def get_species(self) -> str:
        """Getting a base url star_wars
        :returns: species
        :rtype: str
        """
        return self.__species

    def __str__(self):
        return f"In This class all variables to parse "

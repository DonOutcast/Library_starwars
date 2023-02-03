import unittest
from src.star_wars.utils.planet import Planet

class StarWarsTest(unittest.TestCase):

    def test_planet(self):
        planet = Planet(9)
        self.assertEqual(planet.get_planet_json(), {'name': 'Coruscant', 'rotation_period': '24', 'orbital_period': '368', 'diameter': '12240', 'climate': 'temperate', 'gravity': '1 standard', 'terrain': 'cityscape, mountains', 'surface_water': 'unknown', 'population': '1000000000000', 'residents': ['https://swapi.dev/api/people/34/', 'https://swapi.dev/api/people/55/', 'https://swapi.dev/api/people/74/'], 'films': ['https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'], 'created': '2014-12-10T11:54:13.921000Z', 'edited': '2014-12-20T20:58:18.432000Z', 'url': 'https://swapi.dev/api/planets/9/'}
,
                         "should {'name': 'Coruscant', 'rotation_period': '24', 'orbital_period': '368', 'diameter': '12240', 'climate': 'temperate', 'gravity': '1 standard', 'terrain': 'cityscape, mountains', 'surface_water': 'unknown', 'population': '1000000000000', 'residents': ['https://swapi.dev/api/people/34/', 'https://swapi.dev/api/people/55/', 'https://swapi.dev/api/people/74/'], 'films': ['https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'], 'created': '2014-12-10T11:54:13.921000Z', 'edited': '2014-12-20T20:58:18.432000Z', 'url': 'https://swapi.dev/api/planets/9/'}")
        self.assertEqual(planet.get_name(), "Coruscant", "should Coruscant")
        self.assertEqual(planet.get_rotation_period(), "24", "should 24")
        self.assertEqual(planet.get_orbital_period(), "368", "should 368")
        self.assertEqual(planet.get_diameter(), "12240", "should 12240")
        self.assertEqual(planet.get_climate(), "temperate", "should temperate")
        self.assertEqual(planet.get_gravity(), "1 standard", "should 1 standard")
        self.assertEqual(planet.get_terrain(), "cityscape, mountains", "should cityscape, mountains")


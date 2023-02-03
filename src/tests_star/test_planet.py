import unittest
from src.star_wars.utils.planet import Planet

class StarWarsTest(unittest.TestCase):

    def test_planet(self):
        planet = Planet(9)
        self.assertEqual(planet.get_planet_json(), {'name': 'Ewok', 'classification': 'mammal', 'designation': 'sentient', 'average_height': '100', 'skin_colors': 'brown', 'hair_colors': 'white, brown, black', 'eye_colors': 'orange, brown', 'average_lifespan': 'unknown', 'homeworld': 'https://swapi.dev/api/planets/7/', 'language': 'Ewokese', 'people': ['https://swapi.dev/api/people/30/'], 'films': ['https://swapi.dev/api/films/3/'], 'created': '2014-12-18T11:22:00.285000Z', 'edited': '2014-12-20T21:36:42.155000Z', 'url': 'https://swapi.dev/api/species/9/'},
                         "should {'name': 'Ewok', 'classification': 'mammal', 'designation': 'sentient', 'average_height': '100', 'skin_colors': 'brown', 'hair_colors': 'white, brown, black', 'eye_colors': 'orange, brown', 'average_lifespan': 'unknown', 'homeworld': 'https://swapi.dev/api/planets/7/', 'language': 'Ewokese', 'people': ['https://swapi.dev/api/people/30/'], 'films': ['https://swapi.dev/api/films/3/'], 'created': '2014-12-18T11:22:00.285000Z', 'edited': '2014-12-20T21:36:42.155000Z', 'url': 'https://swapi.dev/api/species/9/'}")
        self.assertEqual(planet.get_name(), "Ewok", "should Ewok")

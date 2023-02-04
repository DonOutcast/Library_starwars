import unittest
from src.star_wars.utils.planet import Planet


class StarWarsTest(unittest.TestCase):

    def test_planet(self):
        planet = Planet(9)
        self.assertEqual(planet.get_planet_json(),
                         {'name': 'Coruscant', 'rotation_period': '24', 'orbital_period': '368', 'diameter': '12240',
                          'climate': 'temperate', 'gravity': '1 standard', 'terrain': 'cityscape, mountains',
                          'surface_water': 'unknown', 'population': '1000000000000',
                          'residents': ['https://swapi.dev/api/people/34/', 'https://swapi.dev/api/people/55/',
                                        'https://swapi.dev/api/people/74/'],
                          'films': ['https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/',
                                    'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'],
                          'created': '2014-12-10T11:54:13.921000Z', 'edited': '2014-12-20T20:58:18.432000Z',
                          'url': 'https://swapi.dev/api/planets/9/'}
                         ,
                         "should {'name': 'Coruscant', 'rotation_period': '24', 'orbital_period': '368', 'diameter': '12240', 'climate': 'temperate', 'gravity': '1 standard', 'terrain': 'cityscape, mountains', 'surface_water': 'unknown', 'population': '1000000000000', 'residents': ['https://swapi.dev/api/people/34/', 'https://swapi.dev/api/people/55/', 'https://swapi.dev/api/people/74/'], 'films': ['https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'], 'created': '2014-12-10T11:54:13.921000Z', 'edited': '2014-12-20T20:58:18.432000Z', 'url': 'https://swapi.dev/api/planets/9/'}")
        self.assertEqual(planet.get_name(), "Coruscant", "should Coruscant")
        self.assertEqual(planet.get_rotation_period(), "24", "should 24")
        self.assertEqual(planet.get_orbital_period(), "368", "should 368")
        self.assertEqual(planet.get_diameter(), "12240", "should 12240")
        self.assertEqual(planet.get_climate(), "temperate", "should temperate")
        self.assertEqual(planet.get_gravity(), "1 standard", "should 1 standard")
        self.assertEqual(planet.get_terrain(), "cityscape, mountains", "should cityscape, mountains")
        self.assertEqual(planet.get_surface_water(), "unknown", "should unknown")
        self.assertEqual(planet.get_population(), "1000000000000", "should 1000000000000")
        self.assertEqual(planet.get_residents(), ['Finis Valorum', 'Adi Gallia', 'Jocasta Nu'],
                         "should ['Finis Valorum', 'Adi Gallia', 'Jocasta Nu']")
        self.assertEqual(planet.get_films(),
                         ['Return of the Jedi', 'The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith'],
                         "should ['Return of the Jedi', 'The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith']")
        self.assertEqual(planet.get_date_created(), "2014-12-10T11:54:13.921000Z", "should 2014-12-10T11:54:13.921000Z")
        self.assertEqual(planet.get_date_edited(), "2014-12-20T20:58:18.432000Z", "should 2014-12-20T20:58:18.432000Z")
        self.assertEqual(planet.save_image(), True, "should True")
        self.assertEqual(planet.get_description(),
                         "Coruscant is the vibrant heart and capital of the galaxy during the age of the Empire, featuring a diverse mix of cultures and citizens spread over hundreds of levels. Once the home of the main Jedi Temple -- the central hub of Jedi training and learning for over a thousand generations and the repository of the Jedi Archives -- these traditions ended when the planet bore witness to Order 66.",
                         "should Coruscant is the vibrant heart and capital of the galaxy during the age of the Empire, featuring a diverse mix of cultures and citizens spread over hundreds of levels. Once the home of the main Jedi Temple -- the central hub of Jedi training and learning for over a thousand generations and the repository of the Jedi Archives -- these traditions ended when the planet bore witness to Order 66.")
        self.assertEqual(len(planet.get_history_description()), 12, "should 12")
        self.assertEqual(len(planet.get_photos_of_history()), 10, "should 10")


if __name__ == "__main__":
    unittest.main()

import unittest
from src.star_wars.utils.specie import Specie


class StarWarsTest(unittest.TestCase):
    def test_specie(self):
        specie = Specie(2)
        self.assertEqual(specie.get_specie_json(),
                         {'name': 'Droid', 'classification': 'artificial', 'designation': 'sentient',
                          'average_height': 'n/a', 'skin_colors': 'n/a', 'hair_colors': 'n/a', 'eye_colors': 'n/a',
                          'average_lifespan': 'indefinite', 'homeworld': None, 'language': 'n/a',
                          'people': ['https://swapi.dev/api/people/2/', 'https://swapi.dev/api/people/3/',
                                     'https://swapi.dev/api/people/8/', 'https://swapi.dev/api/people/23/'],
                          'films': ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/',
                                    'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/',
                                    'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'],
                          'created': '2014-12-10T15:16:16.259000Z', 'edited': '2014-12-20T21:36:42.139000Z',
                          'url': 'https://swapi.dev/api/species/2/'},
                         "should {'name': 'Droid', 'classification': 'artificial', 'designation': 'sentient', "
                         "'average_height': 'n/a', 'skin_colors': 'n/a', 'hair_colors': 'n/a', 'eye_colors': 'n/a', "
                         "'average_lifespan': 'indefinite', 'homeworld': None, 'language': 'n/a', 'people': ["
                         "'https://swapi.dev/api/people/2/', 'https://swapi.dev/api/people/3/', "
                         "'https://swapi.dev/api/people/8/', 'https://swapi.dev/api/people/23/'], 'films': ["
                         "'https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', "
                         "'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/', "
                         "'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'], 'created': "
                         "'2014-12-10T15:16:16.259000Z', 'edited': '2014-12-20T21:36:42.139000Z', "
                         "'url': 'https://swapi.dev/api/species/2/'}"
                         )
        self.assertEqual(specie.get_name(), "Droid", "should Droid")
        self.assertEqual(specie.get_classification(), "artificial", "should artificial")
        self.assertEqual(specie.get_designation(), "sentient", "should sentient")
        self.assertEqual(specie.get_average_height(), "n/a", "should n/a")
        self.assertEqual(specie.get_skin_colors(), "n/a", "should n/a")
        self.assertEqual(specie.get_hair_colors(), "n/a", "should n/a")
        self.assertEqual(specie.get_eye_colors(), "n/a", "should n/a")
        self.assertEqual(specie.get_average_lifespan(), "indefinite", "should indefinite")
        self.assertEqual(specie.get_language(), "n/a", "should n/a")
        self.assertEqual(specie.get_home_world(), None, "should None")
        self.assertEqual(specie.get_date_created(), "2014-12-10T15:16:16.259000Z", "should 2014-12-10T15:16:16.259000Z")
        self.assertEqual(specie.get_date_edited(), "2014-12-20T21:36:42.139000Z", "should 2014-12-20T21:36:42.139000Z")
        self.assertEqual(specie.get_films(),
                         ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi', 'The Phantom Menace',
                          'Attack of the Clones', 'Revenge of the Sith']
                         ,
                         "should ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi', 'The Phantom "
                         "Menace', 'Attack of the Clones', 'Revenge of the Sith']")
        self.assertEqual(specie.get_people(), ['C-3PO', 'R2-D2', 'R5-D4', 'IG-88'],
                         "should ['C-3PO', 'R2-D2', 'R5-D4', 'IG-88']")
        self.assertEqual(specie.save_image(), {'Droid.png': True}, "should {'Droid.png': True}")
        self.assertEqual(specie.get_description(),
                         "Droids, less commonly known as robots and automatons, were mechanical beings that possessed artificial intelligence. They were used in a variety of roles and environments, often those considered too menial or too dangerous for other species, but also in fields that required extensive specialization and knowledge.",
                         "should Droids, less commonly known as robots and automatons, were mechanical beings that possessed artificial intelligence. They were used in a variety of roles and environments, often those considered too menial or too dangerous for other species, but also in fields that required extensive specialization and knowledge.")


if __name__ == "__main__":
    unittest.main()

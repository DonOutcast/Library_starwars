import unittest
from src.star_wars.utils.people import People


class StarWarsTest(unittest.TestCase):

    def test_people(self):
        people = People(10)
        self.assertEqual(people.get_people_json(),
                         {'name': 'Obi-Wan Kenobi', 'height': '182', 'mass': '77', 'hair_color': 'auburn, white',
                          'skin_color': 'fair', 'eye_color': 'blue-gray', 'birth_year': '57BBY', 'gender': 'male',
                          'homeworld': 'https://swapi.dev/api/planets/20/',
                          'films': ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/',
                                    'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/',
                                    'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'],
                          'species': [],
                          'vehicles': ['https://swapi.dev/api/vehicles/38/'],
                          'starships': ['https://swapi.dev/api/starships/48/',
                                        'https://swapi.dev/api/starships/59/',
                                        'https://swapi.dev/api/starships/64/',
                                        'https://swapi.dev/api/starships/65/',
                                        'https://swapi.dev/api/starships/74/'],
                          'created': '2014-12-10T16:16:29.192000Z', 'edited': '2014-12-20T21:17:50.325000Z',
                          'url': 'https://swapi.dev/api/people/10/'},
                         "should {'name': 'Obi-Wan Kenobi', 'height': '182', 'mass': '77', 'hair_color': 'auburn, white', 'skin_color': 'fair', 'eye_color': 'blue-gray', 'birth_year': '57BBY', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/20/', 'films': ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'], 'species': [], 'vehicles': ['https://swapi.dev/api/vehicles/38/'], 'starships': ['https://swapi.dev/api/starships/48/', 'https://swapi.dev/api/starships/59/', 'https://swapi.dev/api/starships/64/', 'https://swapi.dev/api/starships/65/', 'https://swapi.dev/api/starships/74/'], 'created': '2014-12-10T16:16:29.192000Z', 'edited': '2014-12-20T21:17:50.325000Z', 'url': 'https://swapi.dev/api/people/10/'}")
        self.assertEqual(len(people.get_all_jsons()), 8, "should 8")
        self.assertEqual(people.get_starships(),
                         ['Jedi starfighter', 'Trade Federation cruiser', 'Naboo star skiff', 'Jedi Interceptor',
                          'Belbullab-22 starfighter'],
                         "should ['Jedi starfighter', 'Trade Federation cruiser', 'Naboo star skiff', 'Jedi Interceptor', 'Belbullab-22 starfighter']")
        self.assertEqual(people.get_films(),
                         ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi', 'The Phantom Menace',
                          'Attack of the Clones', 'Revenge of the Sith'],
                         "should ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi', 'The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith']")
        self.assertEqual(people.get_name(), "Obi-Wan Kenobi", "should Obi-Wan Kenobi")
        self.assertEqual(people.get_height(), "182", "should 182")
        self.assertEqual(people.get_mass(), "77", "should 77")
        self.assertEqual(people.get_hair_color(), "auburn, white", "should auburn, white")
        self.assertEqual(people.get_skin_color(), "fair", "should fair")
        self.assertEqual(people.get_eye_color(), "blue-gray", "should blue-gray")
        self.assertEqual(people.get_birth_year(), "57BBY", "should 57BBY")
        self.assertEqual(people.get_gender(), "male", "should male")
        self.assertEqual(people.get_species(), [], "should  []")
        self.assertEqual(people.get_date_created(), "2014-12-10T16:16:29.192000Z",
                         "should 2014-12-10T16:16:29.192000Z")
        self.assertEqual(people.get_date_edited(), "2014-12-20T21:17:50.325000Z",
                         "should 2014-12-20T21:17:50.325000Z")
        self.assertEqual(people.get_vehicles(), ['Tribubble bongo'], "should ['Tribubble bongo']")
        self.assertEqual(people.get_home_world(), "Stewjon", "should Stewjon")
        self.assertEqual(people.get_description(),
                         "A legendary Jedi Master, Obi-Wan Kenobi was a noble man and gifted in the ways of the Force. He trained Anakin Skywalker, served as a general in the Republic Army during the Clone Wars, and guided Luke Skywalker as a mentor.",
                         "A legendary Jedi Master, Obi-Wan Kenobi was a noble man and gifted in the ways of the Force. He trained Anakin Skywalker, served as a general in the Republic Army during the Clone Wars, and guided Luke Skywalker as a mentor.")
        self.assertEqual(len(people.get_photos_of_history()), 10, "should 10")
        self.assertEqual(people.save_image(), True, "should True")


if __name__ == "__main__":
    unittest.main()

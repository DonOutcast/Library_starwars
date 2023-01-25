import unittest
from src.star_wars.utils.starships import Starship


class StarWarsTest(unittest.TestCase):
    def test_starships(self):
        starship = Starship(10)
        self.assertEqual(starship.id, 10, "should 2")
        self.assertListEqual(starship.get_pilots(), ['Chewbacca', 'Han Solo', 'Lando Calrissian', 'Nien Nunb'],
                             "should 4")
        self.assertListEqual(starship.get_films(), ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi'])
        self.assertEqual(starship.get_name(), "Millennium Falcon", "Should Millennium Falcon")
        self.assertEqual(starship.get_model(), "YT-1300 light freighter", "Should YT-1300 light freighter")


if __name__ == "__main__":
    unittest.main()

# temp = [{
#     "name": "Millennium Falcon",
#     "model": "YT-1300 light freighter",
#     "manufacturer": "Corellian Engineering Corporation",
#     "cost_in_credits": "100000",
#     "length": "34.37",
#     "max_atmosphering_speed": "1050",
#     "crew": "4",
#     "passengers": "6",
#     "cargo_capacity": "100000",
#     "consumables": "2 months",
#     "hyperdrive_rating": "0.5",
#     "MGLT": "75",
#     "starship_class": "Light freighter",
#     "pilots": [
#         "https://swapi.dev/api/people/13/",
#         "https://swapi.dev/api/people/14/",
#         "https://swapi.dev/api/people/25/",
#         "https://swapi.dev/api/people/31/"
#     ],
#     "films": [
#         "https://swapi.dev/api/films/1/",
#         "https://swapi.dev/api/films/2/",
#         "https://swapi.dev/api/films/3/"
#     ],
#     "created": "2014-12-10T16:59:45.094000Z",
#     "edited": "2014-12-20T21:23:49.880000Z",
#     "url": "https://swapi.dev/api/starships/10/"
#          ]
# }

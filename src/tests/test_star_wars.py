import unittest
from utils.starships import Starship


class StarWarsTest(unittest.TestCase):
    def test_starships(self):
        starship = Starship(10)
        self.assertEqual(starship.id, 10, "should 2")
        self.assertListEqual(starship.get_pilots(), ['Chewbacca', 'Han Solo', 'Lando Calrissian', 'Nien Nunb'],
                             "should 4")
        self.assertListEqual(starship.get_films(), ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi'])
        self.assertEqual(starship.get_name(), "Millennium Falcon", "Should Millennium Falcon")

if __name__ == "__main__":
    unittest.main()
temp = {
    "count": 36,
    "next": "https://swapi.dev/api/starships/?page=3",
    "previous": "https://swapi.dev/api/starships/?page=1",
    "results": [
        {
            "name": "Slave 1",
            "model": "Firespray-31-class patrol and attack",
            "manufacturer": "Kuat Systems Engineering",
            "cost_in_credits": "unknown",
            "length": "21.5",
            "max_atmosphering_speed": "1000",
            "crew": "1",
            "passengers": "6",
            "cargo_capacity": "70000",
            "consumables": "1 month",
            "hyperdrive_rating": "3.0",
            "MGLT": "70",
            "starship_class": "Patrol craft",
            "pilots": [
                "https://swapi.dev/api/people/22/"
            ],
            "films": [
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/5/"
            ],
            "created": "2014-12-15T13:00:56.332000Z",
            "edited": "2014-12-20T21:23:49.897000Z",
            "url": "https://swapi.dev/api/starships/21/"
        } ]
}
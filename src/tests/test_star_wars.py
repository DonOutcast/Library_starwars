import unittest
from utils.starships import Starship


class StarWarsTest(unittest.TestCase):
    def test_starships(self):
        starship = Starship(10)
        self.assertEqual(starship.id, 10, "should 2")
        self.assertListEqual(starship.get_pilots(), ['Chewbacca', 'Han Solo', 'Lando Calrissian', 'Nien Nunb'],
                             "should 4")
        self.assertListEqual(starship.get_films(), ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi'])


if __name__ == "__main__":
    unittest.main()

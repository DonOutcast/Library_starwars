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
        self.assertEqual(starship.get_manufacture(), "Corellian Engineering Corporation",
                         "should Corellian Engineering Corporation")
        self.assertEqual(starship.get_cost_in_credits(), "100000", "should 100000")
        self.assertEqual(starship.get_length(), "34.37", "should 34.37")
if __name__ == "__main__":
    unittest.main()

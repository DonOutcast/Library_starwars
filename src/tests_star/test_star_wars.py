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
        self.assertEqual(starship.get_max_atmosphering_speed(), "1050", "should 1050")
        self.assertEqual(starship.get_crew(), "4", "should 4")
        self.assertEqual(starship.get_passengers(), "6", "should 6")
        self.assertEqual(starship.get_cargo_capacity(), "100000", "should 100000")
        self.assertEqual(starship.get_consumables(), "2 months", "should 2 months")
        self.assertEqual(starship.get_hyperdrive_rating(), "0.5", "should 0.5")
        self.assertEqual(starship.get_mglt(), "75", "should 75")
        self.assertEqual(starship.get_starship_class(), "Light freighter", "should Light freighter")
        self.assertEqual(starship.get_date_created(), "2014-12-10T16:59:45.094000Z",
                         "should 2014-12-10T16:59:45.094000Z")
        self.assertEqual(starship.get_date_edited(), "2014-12-20T21:23:49.880000Z",
                         "should 2014-12-20T21:23:49.880000Z")
        self.assertEqual(len(starship.all_jsons), 3, "should 3")
        self.assertEqual(starship.get_photo_ship("Millennium Falcon"),
                         "https://static.wikia.nocookie.net/starwars/images/5/52/Millennium_Falcon_Fathead_TROS.png/revision/latest/scale-to-width-down/500?cb=20221029015218",
                         "should https://static.wikia.nocookie.net/starwars/images/5/52/Millennium_Falcon_Fathead_TROS.png/revision/latest/scale-to-width-down/500?cb=20221029015218")
        self.assertTrue(starship.download_image("test.png"))


if __name__ == "__main__":
    unittest.main()

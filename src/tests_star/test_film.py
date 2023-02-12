import unittest
from src.star_wars.utils.films import Film


class StarWarsTest(unittest.TestCase):
    def test_film_a_new_hope(self):
        film = Film(1)
        self.assertEqual(film.get_name(), "A New Hope", "should A New Hope")
        self.assertEqual(film.get_episode(), 4, "should 4")
        self.assertEqual(len(film.get_opening_crawl()), 522, "should 522")
        self.assertEqual(film.get_director(), "George Lucas", "should George Lucas")
        self.assertEqual(film.get_producer(), "Gary Kurtz, Rick McCallum", "should Gary Kurtz, Rick McCallum")
        self.assertEqual(film.get_release_date(), "1977-05-25", "should 1977-05-25")
        self.assertEqual(film.get_planets(), {'Tatooine': '1', 'Alderaan': '2', 'Yavin IV': '3'}, "should {'Tatooine': '1', 'Alderaan': '2', 'Yavin IV': '3'}")
        self.assertEqual(film.get_species(), {'Human': '1', 'Droid': '2', 'Wookie': '3', 'Rodian': '4', 'Hutt': '5'}, "should {'Human': '1', 'Droid': '2', 'Wookie': '3', 'Rodian': '4', 'Hutt': '5'}")

        # self.assertEqual(len(film.get_characters()), 20, "should 20")


if __name__ == "__main__":
    unittest.main()

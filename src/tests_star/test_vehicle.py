import unittest
from src.star_wars.utils.vehicle import Vehicles


class StarWarsTest(unittest.TestCase):
    def test_specie(self):
        vehicle = Vehicles(2)
        self.assertEqual(vehicle.get_films(), ['The Empire Strikes Back'], "should ['The Empire Strikes Back']")
        self.assertEqual(vehicle.get_pilots(), ['Luke Skywalker', 'Wedge Antilles'], "should ['Luke Skywalker', 'Wedge Antilles']")


if __name__ == "__main__":
    unittest.main()

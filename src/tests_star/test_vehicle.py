import unittest
from src.star_wars.utils.vehicle import Vehicles


class StarWarsTest(unittest.TestCase):
    def test_specie(self):
        vehicle = Vehicles(14)
        self.assertEqual(vehicle.get_films(), ['The Empire Strikes Back'], "should ['The Empire Strikes Back']")
        self.assertEqual(vehicle.get_pilots(), ['Luke Skywalker', 'Wedge Antilles'], "should ['Luke Skywalker', 'Wedge Antilles']")
        self.assertEqual(vehicle.get_name(), "Snowspeeder", "should Snowspeeder")
        self.assertEqual(vehicle.get_model(), "t-47 airspeeder", "should t-47 airspeeder")
        self.assertEqual(vehicle.get_manufacturer(), "Incom corporation", "should Incom corporation")
        self.assertEqual(vehicle.get_cost_in_credits(), "unknown", "should unknown")
        self.assertEqual(vehicle.get_length(), "4.5", "should 4.5")
        self.assertEqual(vehicle.get_max_atmosphering_speed(), "650", "should 650")
        self.assertEqual(vehicle.get_crew(), "2", "should 2")
        self.assertEqual(vehicle.get_passengers(), "0", "should 0")

if __name__ == "__main__":
    unittest.main()

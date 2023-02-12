import unittest
from src.star_wars.utils.vehicles import Vehicles


class StarWarsTest(unittest.TestCase):
    def test_specie(self):
        vehicle = Vehicles(14)
        self.assertEqual(vehicle.get_films(), ['The Empire Strikes Back'], "should ['The Empire Strikes Back']")
        self.assertEqual(vehicle.get_pilots(), ['Luke Skywalker', 'Wedge Antilles'],
                         "should ['Luke Skywalker', 'Wedge Antilles']")
        self.assertEqual(vehicle.get_name(), "Snowspeeder", "should Snowspeeder")
        self.assertEqual(vehicle.get_model(), "t-47 airspeeder", "should t-47 airspeeder")
        self.assertEqual(vehicle.get_manufacturer(), "Incom corporation", "should Incom corporation")
        self.assertEqual(vehicle.get_cost_in_credits(), "unknown", "should unknown")
        self.assertEqual(vehicle.get_length(), "4.5", "should 4.5")
        self.assertEqual(vehicle.get_max_atmosphering_speed(), "650", "should 650")
        self.assertEqual(vehicle.get_crew(), "2", "should 2")
        self.assertEqual(vehicle.get_passengers(), "0", "should 0")
        self.assertEqual(vehicle.get_cargo_capacity(), "10", "should 10")
        self.assertEqual(vehicle.get_consumables(), "none", "should none")
        self.assertEqual(vehicle.get_vehicle_class(), "airspeeder", "should airspeeder")
        self.assertEqual(vehicle.get_date_edited(), "2014-12-20T21:30:21.672000Z", "should 2014-12-20T21:30:21.672000Z")
        self.assertEqual(vehicle.get_date_created(), "2014-12-15T12:22:12Z", "should 2014-12-15T12:22:12Z")
        self.assertEqual(vehicle.get_descriptions(),
                         "The snowspeeder was a type of T-47 airspeeder manufactured by Incom Corporation and modified by the Rebel Alliance.[1] They saw use during the Battle of Hoth against the Galactic Empire, taking down Imperial All Terrain Armored Transports with their tow cables.[3]",
                         "should The snowspeeder was a type of T-47 airspeeder manufactured by Incom Corporation and modified by the Rebel Alliance.[1] They saw use during the Battle of Hoth against the Galactic Empire, taking down Imperial All Terrain Armored Transports with their tow cables.[3]")
        self.assertEqual(vehicle.download_image(), {'Snowspeeder.png': True}, "should {'Snowspeeder.png': True}")

if __name__ == "__main__":
    unittest.main()

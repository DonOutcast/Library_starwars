import unittest
from src.star_wars.models.history import History

class StarWarsTest(unittest.TestCase):
    def test_history(self):
        history = History("Leia Organa")
        self.assertEqual(history.name_for_searching, "Leia-Organa", "shoud Leia-Organa")
        self.assertEqual(len(history.get_after_photo()), 22, "should 22")
        self.assertEqual(len(history.get_photos_of_history()), 14, "should 14")
        self.assertEqual(history.get_description(),
                         "Princess Leia Organa was one of the greatest leaders of the Rebel Alliance, fearless on the battlefield and dedicated to ending the Empire’s tyranny. Daughter of Padmé Amidala and Anakin Skywalker, sister of Luke Skywalker, and with a soft spot for scoundrels, Leia ranked among the galaxy’s great heroes. But life under the New Republic proved difficult for her. Sidelined by a new generation of political leaders, she struck out on her own to oppose the First Order as founder of the Resistance. These setbacks in her political career were accompanied by more personal losses, which she endured with her seemingly inexhaustible will.",
                         "Princess Leia Organa was one of the greatest leaders of the Rebel Alliance, fearless on the battlefield and dedicated to ending the Empire’s tyranny. Daughter of Padmé Amidala and Anakin Skywalker, sister of Luke Skywalker, and with a soft spot for scoundrels, Leia ranked among the galaxy’s great heroes. But life under the New Republic proved difficult for her. Sidelined by a new generation of political leaders, she struck out on her own to oppose the First Order as founder of the Resistance. These setbacks in her political career were accompanied by more personal losses, which she endured with her seemingly inexhaustible will.")
        self.assertEqual(history.save_history_photos(),
                         {'Leia-Organa0.png': True, 'Leia-Organa1.png': True, 'Leia-Organa2.png': True,
                          'Leia-Organa3.png': True, 'Leia-Organa4.png': True, 'Leia-Organa5.png': True,
                          'Leia-Organa6.png': True, 'Leia-Organa7.png': True, 'Leia-Organa8.png': True,
                          'Leia-Organa9.png': True, 'Leia-Organa10.png': True, 'Leia-Organa11.png': True,
                          'Leia-Organa12.png': True, 'Leia-Organa13.png': True}                         ,
                         "should {'Leia-Organa0.png': True, 'Leia-Organa1.png': True, 'Leia-Organa2.png': True, 'Leia-Organa3.png': True, 'Leia-Organa4.png': True, 'Leia-Organa5.png': True, 'Leia-Organa6.png': True, 'Leia-Organa7.png': True, 'Leia-Organa8.png': True, 'Leia-Organa9.png': True, 'Leia-Organa10.png': True, 'Leia-Organa11.png': True, 'Leia-Organa12.png': True, 'Leia-Organa13.png': True}")
        self.assertEqual(len(history.get_byte_code_of_photos()), 14, "should 14")
        self.assertEqual(history.get_url_image() , "https://lumiere-a.akamaihd.net/v1/images/leia-organa-feature-image_d0f5e9_056d9177.jpeg?region=0%2C0%2C1280%2C720&width=320", "should https://lumiere-a.akamaihd.net/v1/images/leia-organa-feature-image_d0f5e9_056d9177.jpeg?region=0%2C0%2C1280%2C720&width=320")
        self.assertEqual(history.save_image(), True, "should True")



if __name__ == "__main__":
    unittest.main()

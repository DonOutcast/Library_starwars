import unittest
from src.star_wars.utils.people import People
from src.star_wars.utils.specie import Specie
from src.star_wars.models.history import History
from src.star_wars.models.starwars import StarWars
from src.star_wars.utils.starships import Starship


class StarWarsTest(unittest.TestCase):
    # def test_star_wars(self):
    #     star_wars_test = StarWars()
    #     self.assertEqual(star_wars_test.get_people_names(),
    #                      {'Luke Skywalker': '1', 'C-3PO': '2', 'R2-D2': '3', 'Darth Vader': '4', 'Leia Organa': '5',
    #                       'Owen Lars': '6', 'Beru Whitesun lars': '7', 'R5-D4': '8', 'Biggs Darklighter': '9',
    #                       'Obi-Wan Kenobi': '10', 'Anakin Skywalker': '11', 'Wilhuff Tarkin': '12', 'Chewbacca': '13',
    #                       'Han Solo': '14', 'Greedo': '15', 'Jabba Desilijic Tiure': '16', 'Wedge Antilles': '18',
    #                       'Jek Tono Porkins': '19', 'Yoda': '20', 'Palpatine': '21', 'Boba Fett': '22', 'IG-88': '23',
    #                       'Bossk': '24', 'Lando Calrissian': '25', 'Lobot': '26', 'Ackbar': '27', 'Mon Mothma': '28',
    #                       'Arvel Crynyd': '29', 'Wicket Systri Warrick': '30', 'Nien Nunb': '31', 'Qui-Gon Jinn': '32',
    #                       'Nute Gunray': '33', 'Finis Valorum': '34', 'Padmé Amidala': '35', 'Jar Jar Binks': '36',
    #                       'Roos Tarpals': '37', 'Rugor Nass': '38', 'Ric Olié': '39', 'Watto': '40', 'Sebulba': '41',
    #                       'Quarsh Panaka': '42', 'Shmi Skywalker': '43', 'Darth Maul': '44', 'Bib Fortuna': '45',
    #                       'Ayla Secura': '46', 'Ratts Tyerel': '47', 'Dud Bolt': '48', 'Gasgano': '49',
    #                       'Ben Quadinaros': '50', 'Mace Windu': '51', 'Ki-Adi-Mundi': '52', 'Kit Fisto': '53',
    #                       'Eeth Koth': '54', 'Adi Gallia': '55', 'Saesee Tiin': '56', 'Yarael Poof': '57',
    #                       'Plo Koon': '58', 'Mas Amedda': '59', 'Gregar Typho': '60', 'Cordé': '61',
    #                       'Cliegg Lars': '62', 'Poggle the Lesser': '63', 'Luminara Unduli': '64',
    #                       'Barriss Offee': '65', 'Dormé': '66', 'Dooku': '67', 'Bail Prestor Organa': '68',
    #                       'Jango Fett': '69', 'Zam Wesell': '70', 'Dexter Jettster': '71', 'Lama Su': '72',
    #                       'Taun We': '73', 'Jocasta Nu': '74', 'R4-P17': '75', 'Wat Tambor': '76', 'San Hill': '77',
    #                       'Shaak Ti': '78', 'Grievous': '79', 'Tarfful': '80', 'Raymus Antilles': '81',
    #                       'Sly Moore': '82', 'Tion Medon': '83'},
    #                      "should  {'Luke Skywalker': '1', 'C-3PO': '2', 'R2-D2': '3', 'Darth Vader': '4', "
    #                      "'Leia Organa': '5', 'Owen Lars': '6', 'Beru Whitesun lars': '7', 'R5-D4': '8', "
    #                      "'Biggs Darklighter': '9', 'Obi-Wan Kenobi': '10', 'Anakin Skywalker': '11', "
    #                      "'Wilhuff Tarkin': '12', 'Chewbacca': '13', 'Han Solo': '14', 'Greedo': '15', "
    #                      "'Jabba Desilijic Tiure': '16', 'Wedge Antilles': '18', 'Jek Tono Porkins': '19', "
    #                      "'Yoda': '20', 'Palpatine': '21', 'Boba Fett': '22', 'IG-88': '23', 'Bossk': '24', "
    #                      "'Lando Calrissian': '25', 'Lobot': '26', 'Ackbar': '27', 'Mon Mothma': '28', "
    #                      "'Arvel Crynyd': '29', 'Wicket Systri Warrick': '30', 'Nien Nunb': '31', 'Qui-Gon Jinn': "
    #                      "'32', 'Nute Gunray': '33', 'Finis Valorum': '34', 'Padmé Amidala': '35', 'Jar Jar Binks': "
    #                      "'36', 'Roos Tarpals': '37', 'Rugor Nass': '38', 'Ric Olié': '39', 'Watto': '40', "
    #                      "'Sebulba': '41', 'Quarsh Panaka': '42', 'Shmi Skywalker': '43', 'Darth Maul': '44', "
    #                      "'Bib Fortuna': '45', 'Ayla Secura': '46', 'Ratts Tyerel': '47', 'Dud Bolt': '48', "
    #                      "'Gasgano': '49', 'Ben Quadinaros': '50', 'Mace Windu': '51', 'Ki-Adi-Mundi': '52', "
    #                      "'Kit Fisto': '53', 'Eeth Koth': '54', 'Adi Gallia': '55', 'Saesee Tiin': '56', "
    #                      "'Yarael Poof': '57', 'Plo Koon': '58', 'Mas Amedda': '59', 'Gregar Typho': '60', "
    #                      "'Cordé': '61', 'Cliegg Lars': '62', 'Poggle the Lesser': '63', 'Luminara Unduli': '64', "
    #                      "'Barriss Offee': '65', 'Dormé': '66', 'Dooku': '67', 'Bail Prestor Organa': '68', "
    #                      "'Jango Fett': '69', 'Zam Wesell': '70', 'Dexter Jettster': '71', 'Lama Su': '72', "
    #                      "'Taun We': '73', 'Jocasta Nu': '74', 'R4-P17': '75', 'Wat Tambor': '76', 'San Hill': '77', "
    #                      "'Shaak Ti': '78', 'Grievous': '79', 'Tarfful': '80', 'Raymus Antilles': '81', 'Sly Moore': "
    #                      "'82', 'Tion Medon': '83'}")
    #     self.assertEqual(star_wars_test.get_planets_names(),
    #                      {'Tatooine': '1', 'Alderaan': '2', 'Yavin IV': '3', 'Hoth': '4', 'Dagobah': '5', 'Bespin': '6',
    #                       'Endor': '7', 'Naboo': '8', 'Coruscant': '9', 'Kamino': '10', 'Geonosis': '11',
    #                       'Utapau': '12', 'Mustafar': '13', 'Kashyyyk': '14', 'Polis Massa': '15', 'Mygeeto': '16',
    #                       'Felucia': '17', 'Cato Neimoidia': '18', 'Saleucami': '19', 'Stewjon': '20', 'Eriadu': '21',
    #                       'Corellia': '22', 'Rodia': '23', 'Nal Hutta': '24', 'Dantooine': '25', 'Bestine IV': '26',
    #                       'Ord Mantell': '27', 'unknown': '28', 'Trandosha': '29', 'Socorro': '30', 'Mon Cala': '31',
    #                       'Chandrila': '32', 'Sullust': '33', 'Toydaria': '34', 'Malastare': '35', 'Dathomir': '36',
    #                       'Ryloth': '37', 'Aleen Minor': '38', 'Vulpter': '39', 'Troiken': '40', 'Tund': '41',
    #                       'Haruun Kal': '42', 'Cerea': '43', 'Glee Anselm': '44', 'Iridonia': '45', 'Tholoth': '46',
    #                       'Iktotch': '47', 'Quermia': '48', 'Dorin': '49', 'Champala': '50', 'Mirial': '51',
    #                       'Serenno': '52', 'Concord Dawn': '53', 'Zolan': '54', 'Ojom': '55', 'Skako': '56',
    #                       'Muunilinst': '57', 'Shili': '58', 'Kalee': '59', 'Umbara': '60'},
    #                      "should {'Tatooine': '1', 'Alderaan': '2', 'Yavin IV': '3', 'Hoth': '4', 'Dagobah': '5', "
    #                      "'Bespin': '6', 'Endor': '7', 'Naboo': '8', 'Coruscant': '9', 'Kamino': '10', 'Geonosis': "
    #                      "'11', 'Utapau': '12', 'Mustafar': '13', 'Kashyyyk': '14', 'Polis Massa': '15', 'Mygeeto': "
    #                      "'16', 'Felucia': '17', 'Cato Neimoidia': '18', 'Saleucami': '19', 'Stewjon': '20', "
    #                      "'Eriadu': '21', 'Corellia': '22', 'Rodia': '23', 'Nal Hutta': '24', 'Dantooine': '25', "
    #                      "'Bestine IV': '26', 'Ord Mantell': '27', 'unknown': '28', 'Trandosha': '29', 'Socorro': "
    #                      "'30', 'Mon Cala': '31', 'Chandrila': '32', 'Sullust': '33', 'Toydaria': '34', 'Malastare': "
    #                      "'35', 'Dathomir': '36', 'Ryloth': '37', 'Aleen Minor': '38', 'Vulpter': '39', 'Troiken': "
    #                      "'40', 'Tund': '41', 'Haruun Kal': '42', 'Cerea': '43', 'Glee Anselm': '44', 'Iridonia': "
    #                      "'45', 'Tholoth': '46', 'Iktotch': '47', 'Quermia': '48', 'Dorin': '49', 'Champala': '50', "
    #                      "'Mirial': '51', 'Serenno': '52', 'Concord Dawn': '53', 'Zolan': '54', 'Ojom': '55', "
    #                      "'Skako': '56', 'Muunilinst': '57', 'Shili': '58', 'Kalee': '59', 'Umbara': '60'}"
    #                      )
    #     self.assertEqual(star_wars_test.get_starships_names(),
    #                      {'CR90 corvette': '2', 'Star Destroyer': '3', 'Sentinel-class landing craft': '5',
    #                       'Death Star': '9', 'Millennium Falcon': '10', 'Y-wing': '11', 'X-wing': '12',
    #                       'TIE Advanced x1': '13', 'Executor': '15', 'Rebel transport': '17', 'Slave 1': '21',
    #                       'Imperial shuttle': '22', 'EF76 Nebulon-B escort frigate': '23', 'Calamari Cruiser': '27',
    #                       'A-wing': '28', 'B-wing': '29', 'Republic Cruiser': '31', 'Droid control ship': '32',
    #                       'Naboo fighter': '39', 'Naboo Royal Starship': '40', 'Scimitar': '41',
    #                       'J-type diplomatic barge': '43', 'AA-9 Coruscant freighter': '47', 'Jedi starfighter': '48',
    #                       'H-type Nubian yacht': '49', 'Republic Assault ship': '52', 'Solar Sailer': '58',
    #                       'Trade Federation cruiser': '59', 'Theta-class T-2c shuttle': '61',
    #                       'Republic attack cruiser': '63', 'Naboo star skiff': '64', 'Jedi Interceptor': '65',
    #                       'arc-170': '66', 'Banking clan frigte': '68', 'Belbullab-22 starfighter': '74',
    #                       'V-wing': '75'},
    #                      "should {'CR90 corvette': '2', 'Star Destroyer': '3', 'Sentinel-class landing craft': '5', "
    #                      "'Death Star': '9', 'Millennium Falcon': '10', 'Y-wing': '11', 'X-wing': '12', 'TIE Advanced "
    #                      "x1': '13', 'Executor': '15', 'Rebel transport': '17', 'Slave 1': '21', 'Imperial shuttle': "
    #                      "'22', 'EF76 Nebulon-B escort frigate': '23', 'Calamari Cruiser': '27', 'A-wing': '28', "
    #                      "'B-wing': '29', 'Republic Cruiser': '31', 'Droid control ship': '32', 'Naboo fighter': "
    #                      "'39', 'Naboo Royal Starship': '40', 'Scimitar': '41', 'J-type diplomatic barge': '43', "
    #                      "'AA-9 Coruscant freighter': '47', 'Jedi starfighter': '48', 'H-type Nubian yacht': '49', "
    #                      "'Republic Assault ship': '52', 'Solar Sailer': '58', 'Trade Federation cruiser': '59', "
    #                      "'Theta-class T-2c shuttle': '61', 'Republic attack cruiser': '63', 'Naboo star skiff': "
    #                      "'64', 'Jedi Interceptor': '65', 'arc-170': '66', 'Banking clan frigte': '68', 'Belbullab-22 "
    #                      "starfighter': '74', 'V-wing': '75'}"
    #                      )
    #     self.assertEqual(star_wars_test.get_vehicles_names(),
    #                      {'Sand Crawler': '4', 'T-16 skyhopper': '6', 'X-34 landspeeder': '7',
    #                       'TIE/LN starfighter': '8', 'Snowspeeder': '14', 'TIE bomber': '16', 'AT-AT': '18',
    #                       'AT-ST': '19', 'Storm IV Twin-Pod cloud car': '20', 'Sail barge': '24',
    #                       'Bantha-II cargo skiff': '25', 'TIE/IN interceptor': '26', 'Imperial Speeder Bike': '30',
    #                       'Vulture Droid': '33', 'Multi-Troop Transport': '34', 'Armored Assault Tank': '35',
    #                       'Single Trooper Aerial Platform': '36', 'C-9979 landing craft': '37', 'Tribubble bongo': '38',
    #                       'Sith speeder': '42', 'Zephyr-G swoop bike': '44', 'Koro-2 Exodrive airspeeder': '45',
    #                       'XJ-6 airspeeder': '46', 'LAAT/i': '50', 'LAAT/c': '51', 'AT-TE': '53', 'SPHA': '54',
    #                       'Flitknot speeder': '55', 'Neimoidian shuttle': '56', 'Geonosian starfighter': '57',
    #                       'Tsmeu-6 personal wheel bike': '60', 'Emergency Firespeeder': '62', 'Droid tri-fighter': '67',
    #                       'Oevvaor jet catamaran': '69', 'Raddaugh Gnasp fluttercraft': '70', 'Clone turbo tank': '71',
    #                       'Corporate Alliance tank droid': '72', 'Droid gunship': '73', 'AT-RT': '76'}
    #                      ,
    #                      "should {'Sand Crawler': '4', 'T-16 skyhopper': '6', 'X-34 landspeeder': '7', 'TIE/LN "
    #                      "starfighter': '8', 'Snowspeeder': '14', 'TIE bomber': '16', 'AT-AT': '18', 'AT-ST': '19', "
    #                      "'Storm IV Twin-Pod cloud car': '20', 'Sail barge': '24', 'Bantha-II cargo skiff': '25', "
    #                      "'TIE/IN interceptor': '26', 'Imperial Speeder Bike': '30', 'Vulture Droid': '33', "
    #                      "'Multi-Troop Transport': '34', 'Armored Assault Tank': '35', 'Single Trooper Aerial "
    #                      "Platform': '36', 'C-9979 landing craft': '37', 'Tribubble bongo': '38', 'Sith speeder': "
    #                      "'42', 'Zephyr-G swoop bike': '44', 'Koro-2 Exodrive airspeeder': '45', 'XJ-6 airspeeder': "
    #                      "'46', 'LAAT/i': '50', 'LAAT/c': '51', 'AT-TE': '53', 'SPHA': '54', 'Flitknot speeder': "
    #                      "'55', 'Neimoidian shuttle': '56', 'Geonosian starfighter': '57', 'Tsmeu-6 personal wheel "
    #                      "bike': '60', 'Emergency Firespeeder': '62', 'Droid tri-fighter': '67', 'Oevvaor jet "
    #                      "catamaran': '69', 'Raddaugh Gnasp fluttercraft': '70', 'Clone turbo tank': '71', "
    #                      "'Corporate Alliance tank droid': '72', 'Droid gunship': '73', 'AT-RT': '76'}")
    #     self.assertEqual(star_wars_test.get_species_names(),
    #                      {'Human': '1', 'Droid': '2', 'Wookie': '3', 'Rodian': '4', 'Hutt': '5', "Yoda's species": '6',
    #                       'Trandoshan': '7', 'Mon Calamari': '8', 'Ewok': '9', 'Sullustan': '10', 'Neimodian': '11',
    #                       'Gungan': '12', 'Toydarian': '13', 'Dug': '14', "Twi'lek": '15', 'Aleena': '16',
    #                       'Vulptereen': '17', 'Xexto': '18', 'Toong': '19', 'Cerean': '20', 'Nautolan': '21',
    #                       'Zabrak': '22', 'Tholothian': '23', 'Iktotchi': '24', 'Quermian': '25', 'Kel Dor': '26',
    #                       'Chagrian': '27', 'Geonosian': '28', 'Mirialan': '29', 'Clawdite': '30', 'Besalisk': '31',
    #                       'Kaminoan': '32', 'Skakoan': '33', 'Muun': '34', 'Togruta': '35', 'Kaleesh': '36',
    #                       "Pau'an": '37'}
    #                      ,
    #                      """should {'Human': '1', 'Droid': '2', 'Wookie': '3', 'Rodian': '4', 'Hutt': '5',
    #                      "Yoda's species": '6', 'Trandoshan': '7', 'Mon Calamari': '8', 'Ewok': '9', 'Sullustan':
    #                      '10', 'Neimodian': '11', 'Gungan': '12', 'Toydarian': '13', 'Dug': '14', "Twi'lek": '15',
    #                      'Aleena': '16', 'Vulptereen': '17', 'Xexto': '18', 'Toong': '19', 'Cerean': '20',
    #                      'Nautolan': '21', 'Zabrak': '22', 'Tholothian': '23', 'Iktotchi': '24', 'Quermian': '25',
    #                      'Kel Dor': '26', 'Chagrian': '27', 'Geonosian': '28', 'Mirialan': '29', 'Clawdite': '30',
    #                      'Besalisk': '31', 'Kaminoan': '32', 'Skakoan': '33', 'Muun': '34', 'Togruta': '35',
    #                      'Kaleesh': '36', "Pau'an": '37'}""")
    #
    # def test_history(self):
    #     history = History("Leia Organa")
    #     self.assertEqual(history.name_for_searching, "Leia-Organa", "shoud Leia-Organa")
    #     self.assertEqual(len(history.get_after_photo()), 22, "should 22")
    #     self.assertEqual(len(history.get_photos_of_history()), 14, "should 14")
    #     self.assertEqual(history.get_description(),
    #                      "Princess Leia Organa was one of the greatest leaders of the Rebel Alliance, fearless on the battlefield and dedicated to ending the Empire’s tyranny. Daughter of Padmé Amidala and Anakin Skywalker, sister of Luke Skywalker, and with a soft spot for scoundrels, Leia ranked among the galaxy’s great heroes. But life under the New Republic proved difficult for her. Sidelined by a new generation of political leaders, she struck out on her own to oppose the First Order as founder of the Resistance. These setbacks in her political career were accompanied by more personal losses, which she endured with her seemingly inexhaustible will.",
    #                      "Princess Leia Organa was one of the greatest leaders of the Rebel Alliance, fearless on the battlefield and dedicated to ending the Empire’s tyranny. Daughter of Padmé Amidala and Anakin Skywalker, sister of Luke Skywalker, and with a soft spot for scoundrels, Leia ranked among the galaxy’s great heroes. But life under the New Republic proved difficult for her. Sidelined by a new generation of political leaders, she struck out on her own to oppose the First Order as founder of the Resistance. These setbacks in her political career were accompanied by more personal losses, which she endured with her seemingly inexhaustible will.")
    #     self.assertEqual(history.save_history_photos(),
    #                      [True, True, True, True, True, True, True, True, True, True, True, True, True, True],
    #                      "should [True, True, True, True, True, True, True, True, True, True, True, True, True, True]")
    #     self.assertEqual(len(history.get_byte_code_of_photos()), 14, "should 14")
    #
    # def test_starships(self):
    #     starship = Starship(10)
    #     self.assertEqual(starship.id, 10, "should 2")
    #     self.assertListEqual(starship.get_pilots(), ['Chewbacca', 'Han Solo', 'Lando Calrissian', 'Nien Nunb'],
    #                          "should 4")
    #     self.assertListEqual(starship.get_films(), ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi'])
    #     self.assertEqual(starship.get_name(), "Millennium Falcon", "Should Millennium Falcon")
    #     self.assertEqual(starship.get_model(), "YT-1300 light freighter", "Should YT-1300 light freighter")
    #     self.assertEqual(starship.get_manufacture(), "Corellian Engineering Corporation",
    #                      "should Corellian Engineering Corporation")
    #     self.assertEqual(starship.get_cost_in_credits(), "100000", "should 100000")
    #     self.assertEqual(starship.get_length(), "34.37", "should 34.37")
    #     self.assertEqual(starship.get_max_atmosphering_speed(), "1050", "should 1050")
    #     self.assertEqual(starship.get_crew(), "4", "should 4")
    #     self.assertEqual(starship.get_passengers(), "6", "should 6")
    #     self.assertEqual(starship.get_cargo_capacity(), "100000", "should 100000")
    #     self.assertEqual(starship.get_consumables(), "2 months", "should 2 months")
    #     self.assertEqual(starship.get_hyperdrive_rating(), "0.5", "should 0.5")
    #     self.assertEqual(starship.get_mglt(), "75", "should 75")
    #     self.assertEqual(starship.get_starship_class(), "Light freighter", "should Light freighter")
    #     self.assertEqual(starship.get_date_created(), "2014-12-10T16:59:45.094000Z",
    #                      "should 2014-12-10T16:59:45.094000Z")
    #     self.assertEqual(starship.get_date_edited(), "2014-12-20T21:23:49.880000Z",
    #                      "should 2014-12-20T21:23:49.880000Z")
    #     self.assertEqual(len(starship.get_all_jsons()), 3, "should 3")
    #     self.assertEqual(starship.get_photo_ship("Millennium Falcon"),
    #                      "https://static.wikia.nocookie.net/starwars/images/5/52/Millennium_Falcon_Fathead_TROS.png/revision/latest/scale-to-width-down/500?cb=20221029015218",
    #                      "should https://static.wikia.nocookie.net/starwars/images/5/52/Millennium_Falcon_Fathead_TROS.png/revision/latest/scale-to-width-down/500?cb=20221029015218")
    #     self.assertTrue(starship.download_image("test.png"))
    #
    # def test_people(self):
    #     people = People(10)
    #     self.assertEqual(people.get_people_json(),
    #                      {'name': 'Obi-Wan Kenobi', 'height': '182', 'mass': '77', 'hair_color': 'auburn, white',
    #                       'skin_color': 'fair', 'eye_color': 'blue-gray', 'birth_year': '57BBY', 'gender': 'male',
    #                       'homeworld': 'https://swapi.dev/api/planets/20/',
    #                       'films': ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/',
    #                                 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/',
    #                                 'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'],
    #                       'species': [],
    #                       'vehicles': ['https://swapi.dev/api/vehicles/38/'],
    #                       'starships': ['https://swapi.dev/api/starships/48/',
    #                                     'https://swapi.dev/api/starships/59/',
    #                                     'https://swapi.dev/api/starships/64/',
    #                                     'https://swapi.dev/api/starships/65/',
    #                                     'https://swapi.dev/api/starships/74/'],
    #                       'created': '2014-12-10T16:16:29.192000Z', 'edited': '2014-12-20T21:17:50.325000Z',
    #                       'url': 'https://swapi.dev/api/people/10/'},
    #                      "should {'name': 'Obi-Wan Kenobi', 'height': '182', 'mass': '77', 'hair_color': 'auburn, white', 'skin_color': 'fair', 'eye_color': 'blue-gray', 'birth_year': '57BBY', 'gender': 'male', 'homeworld': 'https://swapi.dev/api/planets/20/', 'films': ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'], 'species': [], 'vehicles': ['https://swapi.dev/api/vehicles/38/'], 'starships': ['https://swapi.dev/api/starships/48/', 'https://swapi.dev/api/starships/59/', 'https://swapi.dev/api/starships/64/', 'https://swapi.dev/api/starships/65/', 'https://swapi.dev/api/starships/74/'], 'created': '2014-12-10T16:16:29.192000Z', 'edited': '2014-12-20T21:17:50.325000Z', 'url': 'https://swapi.dev/api/people/10/'}")
    #     self.assertEqual(len(people.get_all_jsons()), 8, "should 8")
    #     self.assertEqual(people.get_starships(),
    #                      ['Jedi starfighter', 'Trade Federation cruiser', 'Naboo star skiff', 'Jedi Interceptor',
    #                       'Belbullab-22 starfighter'],
    #                      "should ['Jedi starfighter', 'Trade Federation cruiser', 'Naboo star skiff', 'Jedi Interceptor', 'Belbullab-22 starfighter']")
    #     self.assertEqual(people.get_films(),
    #                      ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi', 'The Phantom Menace',
    #                       'Attack of the Clones', 'Revenge of the Sith'],
    #                      "should ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi', 'The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith']")
    #     self.assertEqual(people.get_name(), "Obi-Wan Kenobi", "should Obi-Wan Kenobi")
    #     self.assertEqual(people.get_height(), "182", "should 182")
    #     self.assertEqual(people.get_mass(), "77", "should 77")
    #     self.assertEqual(people.get_hair_color(), "auburn, white", "should auburn, white")
    #     self.assertEqual(people.get_skin_color(), "fair", "should fair")
    #     self.assertEqual(people.get_eye_color(), "blue-gray", "should blue-gray")
    #     self.assertEqual(people.get_birth_year(), "57BBY", "should 57BBY")
    #     self.assertEqual(people.get_gender(), "male", "should male")
    #     self.assertEqual(people.get_species(), [], "should  []")
    #     self.assertEqual(people.get_date_created(), "2014-12-10T16:16:29.192000Z",
    #                      "should 2014-12-10T16:16:29.192000Z")
    #     self.assertEqual(people.get_date_edited(), "2014-12-20T21:17:50.325000Z",
    #                      "should 2014-12-20T21:17:50.325000Z")
    #     self.assertEqual(people.get_vehicles(), ['Tribubble bongo'], "should ['Tribubble bongo']")
    #     self.assertEqual(people.get_home_world(), "Stewjon", "should Stewjon")
    #     self.assertEqual(people.get_description(),
    #                      "A legendary Jedi Master, Obi-Wan Kenobi was a noble man and gifted in the ways of the Force. He trained Anakin Skywalker, served as a general in the Republic Army during the Clone Wars, and guided Luke Skywalker as a mentor.",
    #                      "A legendary Jedi Master, Obi-Wan Kenobi was a noble man and gifted in the ways of the Force. He trained Anakin Skywalker, served as a general in the Republic Army during the Clone Wars, and guided Luke Skywalker as a mentor.")
    #     self.assertEqual(len(people.get_photos_of_history()), 10, "should 10")
    def test_specie(self):
        specie = Specie(2)
        self.assertEqual(specie.get_specie_json(),
                         {'name': 'Droid', 'classification': 'artificial', 'designation': 'sentient',
                          'average_height': 'n/a', 'skin_colors': 'n/a', 'hair_colors': 'n/a', 'eye_colors': 'n/a',
                          'average_lifespan': 'indefinite', 'homeworld': None, 'language': 'n/a',
                          'people': ['https://swapi.dev/api/people/2/', 'https://swapi.dev/api/people/3/',
                                     'https://swapi.dev/api/people/8/', 'https://swapi.dev/api/people/23/'],
                          'films': ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/',
                                    'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/',
                                    'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'],
                          'created': '2014-12-10T15:16:16.259000Z', 'edited': '2014-12-20T21:36:42.139000Z',
                          'url': 'https://swapi.dev/api/species/2/'},
                         "should {'name': 'Droid', 'classification': 'artificial', 'designation': 'sentient', "
                         "'average_height': 'n/a', 'skin_colors': 'n/a', 'hair_colors': 'n/a', 'eye_colors': 'n/a', "
                         "'average_lifespan': 'indefinite', 'homeworld': None, 'language': 'n/a', 'people': ["
                         "'https://swapi.dev/api/people/2/', 'https://swapi.dev/api/people/3/', "
                         "'https://swapi.dev/api/people/8/', 'https://swapi.dev/api/people/23/'], 'films': ["
                         "'https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', "
                         "'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/', "
                         "'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'], 'created': "
                         "'2014-12-10T15:16:16.259000Z', 'edited': '2014-12-20T21:36:42.139000Z', "
                         "'url': 'https://swapi.dev/api/species/2/'}"
                         )
        self.assertEqual(specie.get_name(), "Droid", "should Droid")
        self.assertEqual(specie.get_classification(), "artificial", "should artificial")


if __name__ == "__main__":
    unittest.main()

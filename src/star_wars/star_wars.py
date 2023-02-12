try:
    import sys
    from src.star_wars.utils.people import People
    from src.star_wars.utils.planets import Planet
    from src.star_wars.utils.films import Film
    from src.star_wars.utils.species import Specie
    from src.star_wars.utils.vehicles import Vehicle
    from src.star_wars.utils.starships import Starship

except (Exception,) as e:
    print(sys.exc_info())
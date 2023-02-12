try:
    import sys
    from src.star_wars.utils import people, films, planets, vehicles, species, starships

except (Exception,) as e:
    print(sys.exc_info())
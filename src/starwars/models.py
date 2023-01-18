try:
    import sys
    import time
    import json
    from utils import query, all_resource_urls
    from settings import Config
except (Exception,):
    print(sys.exc_info())


class BaseModel:
    """The class convert your byte string to json """
    def __init__(self, raw_data: bytes) -> None:
        """The base constructor add to all keys and values to attribute of class
        :param: raw_data bytes
        :type: bytes
        :returns: None
        :type: None
        """
        json_data = json.loads(raw_data)
        for key, value in json_data.items():
            print(key, value)
            setattr(self, key, value)


class BaseQuerySet:
    def __init__(self):
        self.items = []

    def order_by(self, order_attribute):
        result = []
        for i in sorted(self.items, key=lambda i: getattr(i, order_attribute)):
            result.append(i)
        return result

    def count(self):
        return len(self.items)

    def iter(self):
        for i in self.items:
            yield i


class StarshipQuerySet(BaseQuerySet):

    def __init__(self, list_of_urls):
        super(StarshipQuerySet, self).__init__()
        for url in list_of_urls:
            response = query(url)
            self.items.append(Starship(response.content))

    def __repr__(self):
        return "StarshipQuerySet - {0}".format(str(len(self.items)))


class Starship(BaseModel):

    def __init__(self, raw_data):
        super(Starship, self).__init__(raw_data)

    def __repr__(self):
        return '<Starship - {0}>'.format(self.name)




    # def get_films(self):
    # return FilmQuerySet(self.films)

    # def get_pilots(self):
    # return PeopleQuerySet(self.pilots)

def get_all(resource):
    ''' Return all of a single resource '''
    QUERYSETS = {
        # conf.get_people(): PeopleQuerySet,
        # conf.get_planets(): PlanetQuerySet,
        conf.get_starships(): StarshipQuerySet,
        # conf.get_vehicles(): VehicleQuerySet,
        # conf.get_species(): SpeciesQuerySet,
        # conf.get_films(): FilmQuerySet
    }
    urls = all_resource_urls(
        "{0}/{1}/".format(conf.get_url_api(), resource)
    )

    return QUERYSETS[resource](urls)


def _get(id, type, conf):
    ''' Return a single person '''
    result = query("{0}/{1}/{2}/".format(
        conf.get_url_api(),
        type,
        str(id))
    )
    return result


def get_starship(starship_id, conf):
    ''' Return a single starship '''
    result = _get(starship_id, conf.get_starships(), conf)
    print(Starship(result.content))
    exit()
    return Starship(result.content)


conf = Config()
# print(get_starship(2, conf))
ships = get_all("starships")
print(ships)
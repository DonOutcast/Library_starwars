try:
    import sys
    import json
    import requests
    import fake_useragent
    from src.star_wars.exceptions import ResourceDoesNotExists
except (Exception,):
    print(sys.exc_info())


def query(query):
    headers = {'User-Agent': 'swapi-python'}
    response = requests.get(query, headers=headers)
    if response.status_code != 200:
        raise ResourceDoesNotExists
    return response


def all_resource_urls(query):
    # print(query)
    # exit()
    """
    Get all the URLs for every resource
    """
    urls = []
    running = True
    while running:
        response = requests.get(query)
        json_data = json.loads(response.content)
        for resource in json_data['results']:
            urls.append(resource['url'])
        if bool(json_data['next']):
            query = json_data['next']
        else:
            running = False
    return urls

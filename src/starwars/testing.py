try:
    import requests
    from bs4 import BeautifulSoup
    from lxml import etree
    from exceptions import ResourceDoesNotExists
    import sys
except (Exception,) as e:
    print(sys.exc_info())
HEADERS = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
url = "https://www.starwars.com/databank/luke-skywalker"
new_url = "https://www.starwars.com/databank/Leia-Organa"
response = requests.get(new_url, headers=HEADERS)
soup = BeautifulSoup(response.content, "html.parser")


def get_url_image(url_person: str, in_soup: BeautifulSoup) -> str:
    result = in_soup.find("div", class_="image-wrapper").find("img").get("data-src")
    print(type(result))
    return result


def save_image(person_name: str, path_to_image) -> bool:
    """Save the image to your directory

    :param person_name: The file location and name
    :type person_name: str
    :param path_to_image: A file link to
    :type path_to_image: str
    :returns: If the file saved successfully True else False
    :rtype: bool
    """
    try:
        with open(person_name + ".png", "wb") as f:
            f.write(requests.get(path_to_image).content)
    except Exception as error:
        print(error)
        return False
    else:
        return True


# if __name__ == "__main__":
#     path = get_url_image("sss", soup)
#     print(save_image("siste", path))
# print(soup.prettify())
# weapons = []
# temp = soup.find_all("div", class_="category")
# # print(temp[6].text)
# for i in temp:
#     if "Weapons" in i.text:
#         weapons = i.find_all("div", class_="property-name")
# if weapons:
#     print(weapons)

# print(soup.select("#ref-1-6 > div > div > div:nth-child(7)"))
# status = soup.find_all("div", class_="stats-container")
# print(status)
# dom = etree.HTML(str(status))
# print(dom.xpath('//*[@class="category"][6]/ul/li/a/div/text()'))

# images = soup.select("img")[2].attrs
# dom = etree.HTML(str(soup))
# with open("image.png", 'wb') as f:
#     f.write(requests.get(images.get("data-src")).content)





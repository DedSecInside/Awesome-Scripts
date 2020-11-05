from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import json

# Create Dictionary element for each hotel entry
def prepareEntry(job_elem):
    """
    Prepare the json job.

    Args:
        job_elem: (todo): write your description
    """
    name = job_elem.find(
        "h3", class_="listingHotelDescription__hotelName d-textEllipsis"
    ).text.strip()

    rating = extractValue(str(job_elem.find(attrs={"itemprop": "ratingValue"})))

    address = job_elem.find(attrs={"itemprop": "streetAddress"}).text.strip()

    distance = job_elem.find(
        "span", class_="listingHotelDescription__distanceText"
    ).text.strip()

    image = extractValue(str(job_elem.find(attrs={"itemprop": "image"})))

    url = extractValue(str(job_elem.find(attrs={"itemprop": "url"})))

    return {
        "name": name,
        "rating": rating,
        "address": address,
        "distance": distance,
        "image": image,
        "url": url,
    }

# Extract urls from tags
def extractValue(s):
    """
    Extracts the string

    Args:
        s: (str): write your description
    """
    s = s[1 : len(s) - 2]
    arr = s.split()
    for i in arr:
        if i[0:7] == "content":
            return i[9:-1]

# Scrap the url 
def getHotels(url):
    """
    Return a list of hotels.

    Args:
        url: (str): write your description
    """
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    webpage = urlopen(req).read()
    page = soup(webpage, "html.parser")
    results = page.find(id="root")
    job_elems = results.find_all("div", class_="hotelCardListing__descriptionWrapper")
    list_hotels = []
    for job_elem in job_elems:
        list_hotels.append(prepareEntry(job_elem))
    return list_hotels

url = "https://www.oyorooms.com/search/?location=Around%20me&latitude=28.5132131&longitude=77.3755908&city=&searchType=locality"
hotel_list = getHotels(url)
print(json.dumps(hotel_list, indent=4, sort_keys=True))


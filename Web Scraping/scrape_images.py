import json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve


def save(url, filename):
    """
    Save the given url.

    Args:
        url: (str): write your description
        filename: (str): write your description
    """
    # This function inputs the image link and the name with which
    # the image needs to be saved, and thus downloads that image
    urlretrieve(url, filename)


def scrape(q):
    """
    Scrape the given query

    Args:
        q: (str): write your description
    """
    # This function scrapes the google images for the particular keyword
    # and saves the first picture related to it.
    url = "https://www.google.com/search?q={}&source=lnms&tbm=isch".format(q)

    # default header for any browser
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
    }

    # instantiating a bs4 object
    soup = BeautifulSoup(urlopen(Request(url,headers=header)),'html.parser')
    
    # finding all links and storing the first one
    # we can download all images by iterating over the list
    # the links of each image are present inside a div with the class: rg_meta notranslate
    a = soup.find_all("div", {"class": "rg_meta notranslate"})[0]
    link = json.loads(a.text)["ou"]
    
    # downloads the photo
    save(link, "{}.jpg".format(q.replace('+', ' ')))
    print('Image of {} downloaded.'.format(q.replace('+', ' ')))


if __name__ == '__main__':
    search = input("Enter a keyword: ").split()
    search = '+'.join(search)
    scrape(search)

#!/usr/bin/env python3

# Created by `Fenil Gandhi`
# 20 October, 2018

"""
A simple script that prints location of user based on active internet connection
"""
import requests


def getLocationInfo():
    """
    Returns the location information

    Args:
    """
    try:
        response = requests.get('http://ip-api.com/json')
        return response.json()
    except Exception as e:
        print("Could not fetch location details. \nKindly check your internet connection.")
        return {}


def main():
    """
    Main function.

    Args:
    """
    print('Fetching your location details based on your isp.')
    data = getLocationInfo()
    print(
        '',
        '-----------------------------------------------------------------------',
        '%-12s : %24s' % ("GLOBAL IP", data.get("query")),
        '%-12s : %24s' % ("ISP", data.get("isp")),
        '%-12s : %24s' % ("ORG", data.get("org")),
        '%-12s : %24s' % ("CITY", data.get("city")),
        '%-12s : %24s' % ("COUNTRY", data.get("country")),
        '%-12s : %24s' % ("TIMEZONE", data.get("timezone")),
        '%-12s : %24s' % ("LATITUDE", data.get("lat")),
        '%-12s : %24s' % ("LONGITUDE", data.get("lon")),
        '%-12s : %24s' % ("TIMEZONE", data.get("timezone")),
        '-----------------------------------------------------------------------',
        sep="\n"
    )


if __name__ == '__main__':
    main()

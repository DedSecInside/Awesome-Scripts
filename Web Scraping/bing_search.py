#!/usr/bin/python
# -*- coding: utf-8 -*-
# python bing_search.py inurl:index.php?id=

import sys
import requests
from bs4 import BeautifulSoup

results = []

def main(query):
    """
    Main function.

    Args:
        query: (str): write your description
    """
    global page
    session = requests.Session()
    # * (Configuration)
    page = 1
    bing_url = 'https://www.bing.com/search?q={0}&first={1}'.format(query, str(page))
    # (If there is a next button for the next page)
    nextBtn_attrs = {
        'class': 'sw_next'
    }
    # (If there is no result)
    bing_no_result = 'There are no results for'

    # * (Bing Search Query)
    bing_search_request = session.get(bing_url)
    bing_soup = BeautifulSoup(bing_search_request.text, 'html.parser')

    # ? Is there a result?
    if bing_no_result not in bing_soup.prettify(): # YES
        # * Get All Results from first page
        links = bing_soup.find_all('li', attrs={'class':'b_algo'})
        for a in links:
            a = a.find('a')
            print (a['href'])
        
        # * Loop Search
        while True:
            # Next Button 
            nextBtn = bool(bing_soup.find('div', attrs=nextBtn_attrs))
            # Current Page
            currentPage = bing_soup.find('a', attrs={'class': 'sb_pagS sb_pagS_bp b_widePag sb_bp'}).get_text()
            # ? Is there a next button for the next page?
            if nextBtn == True: # YES
                # * Loop Bing Search Query
                page += 10
                bing_url = 'https://www.bing.com/search?q={0}&first={1}'.format(query, str(page))
                bing_search_request = session.get(bing_url)
                bing_soup = BeautifulSoup(bing_search_request.text, 'html.parser')
                try:
                    nextPage = bing_soup.find('a', attrs={'class': 'sb_pagS sb_pagS_bp b_widePag sb_bp'}).get_text()
                except:
                    break
                # If the current page did not increase
                if currentPage == nextPage:
                    break

                # * Loop Get All Results
                links = bing_soup.find_all('li', attrs={'class':'b_algo'})
                for a in links:
                    a = a.find('a')
                    results.append(a)
                    print (a['href'])
            elif nextBtn == False: # NO
                break
    elif bing_no_result in bing_soup.prettify(): # NO
        print ('{0} {1}'.format(bing_no_result, query))
        pass

if __name__ == '__main__':
    main(str(sys.argv[1]))
    # Statistics Tracking
    # Uncomment If Necessary
    #print ('\n\nTotal Links          : {}'.format(len(results)))
    #print ('Total Pages Searched : {}'.format(page))

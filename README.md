# Phone Number Scraper

This is a Python program that scrapes web pages for phone numbers and saves them to a file. It uses the requests library to fetch web pages, the BeautifulSoup library to parse HTML, and regular expressions to search for phone numbers.


This program requires Python 3 and the following Python libraries:

    requests
    beautifulsoup4

You can install these libraries using pip. For example:

    pip install requests
    pip install beautifulsoup4

Usage

To use the program, run the find_Phones function with a starting URL and a search string for URLs. For example:
  python phone_scraper.py 

Enter the Base URL:  <---- your url here

Enter the search string for url:   <----- your url search string here
  
  
    from phone_scraper import find_Phones

    # set the starting URL and the search string for URLs
      url = 'https://example.com'
      search_str = 'example'

    # scrape the web pages for phone numbers
      find_Phones(url, search_str)

The find_Phones function will crawl the web pages starting from the specified URL and follow any links that contain the search string. It will search for phone numbers in the text of each web page and save them to a file called phone_no.txt.

Once the program has finished running, you can use the filter_uniques function to filter out duplicate phone numbers and save the unique phone numbers to a new file. For example:

      from phone_scraper import filter_uniques

      # filter out duplicate phone numbers and save the unique numbers to a new file
      filter_uniques('phone_no.txt', 'filtered_phone_no.txt')

The filter_uniques function will read the phone numbers from phone_no.txt, filter out any duplicates, and save the unique phone numbers to a new file called filtered_phone_no.txt.

just run:
      
      filter_phone.py

"""
Target_Scraper.py   - Part of the CheapStaples program

    Scrapes Target's website for food prices & returns the prices
        in a list of pairs


Items Searched & Their net weights: (IN ORDER)
    Milk (1gal)
    Eggs (12)
    Bread (White)
    Staples (5000 staples)  # Because it's funny
    Butter (1lb)
    Ketchup (20oz)
    Mustard (20oz)
    Mayo (30oz)
    Apples (Honeycrisp single)
    Corn (15.25oz)
    Bananas (each)
    Cream Cheese (8oz)
    Peanut Butter (creamy 16oz)
    Pinto Beans (15oz)
    Black Beans (15.5oz)
    White Rice (5lbs)
    Marinara Sauce (23oz)
    Spaghetti (1lb)
    Chicken Breasts (boneless skinless per lb)
    Ground Beef (1lb 80/20)
    Bacon (1 lb)
    Baking Powder (8.1 oz)
    Baking Soda (1 lb)
    Vanilla Extract (1 oz)
    Sugar (4 oz)
    Flour (5 lb)
    Olive Oil (16.9 oz extra virgin)
    Salt (26 oz)
    Pepper (3 oz)
    Oats (42 oz)
    Tomatoes (13 oz 2 pack)
    Peanutes (16 oz)
    Vanilla Ice Cream (1.5 qt)
"""

# Use Beautiful Soup to use as web scraper
from bs4 import BeautifulSoup
import requests


def Target_Scrapper():
    """
    Desc:
        Scrape Target's website of all items within url_list and return
            the name, price pairs in a list.
        
        As for Net Weight of the products searched for, uses measurements specified in the file header comment
        
        Useful for handing data over to a database for storage

    Parameters:
        None

    Returns:
        staple_food     (List[Lists])   - List of length 2 lists, with (str), (int) pairs

                Example:
                        [["Milk", 3.99], ["Eggs", 1.48], ["Bread", 2.57]]
    
    """
    # List of all the urls that correspond to the list of staple foods (IN ORDER)
    url_list = ["https://www.target.com/p/vitamin-d-whole-milk-1gal-good-38-gather-8482/-/A-13276134#lnk=sametab",
                "https://www.target.com/p/grade-a-large-eggs-12ct-good-38-gather-8482-packaging-may-vary/-/A-14713534#lnk=sametab",
                "https://www.target.com/p/wonder-round-top-white-sliced-bread-20oz/-/A-15077154#lnk=sametab",
                "https://www.target.com/p/5000-standard-staples-up-38-up-8482/-/A-83901186#lnk=sametab",    # Actual staples cause it's funny
                "https://www.target.com/p/salted-butter-1lb-good-38-gather-8482/-/A-80796339#lnk=sametab",
                "https://www.target.com/p/ketchup-20oz-market-pantry-8482/-/A-14711236#lnk=sametab",
                "https://www.target.com/p/yellow-mustard-20oz-market-pantry-8482/-/A-14766257#lnk=sametab",
                "https://www.target.com/p/mayonnaise-30oz-market-pantry-8482/-/A-13007982#lnk=sametab",
                "https://www.target.com/p/honeycrisp-apple-each/-/A-31167786#lnk=sametab",
                "https://www.target.com/p/del-monte-golden-sweet-whole-kernel-corn-15-25oz/-/A-13204310#lnk=sametab",
                "https://www.target.com/p/banana-each/-/A-15013944#lnk=sametab",
                "https://www.target.com/p/plain-cream-cheese-spread-8oz-good-38-gather-8482/-/A-79694563#lnk=sametab",
                "https://www.target.com/p/creamy-peanut-butter-16oz-good-38-gather-8482/-/A-84067786#lnk=sametab",
                "https://www.target.com/p/organic-low-sodium-pinto-beans-15oz-good-38-gather-8482/-/A-78654175#lnk=sametab",
                "https://www.target.com/p/black-beans-15-5oz-good-38-gather-8482/-/A-78666524#lnk=sametab",
                "https://www.target.com/p/enriched-long-grain-white-rice-5lbs-good-38-gather-8482/-/A-54602336#lnk=sametab",
                "https://www.target.com/p/marinara-pasta-sauce-23oz-good-38-gather-8482/-/A-79507430#lnk=sametab",
                "https://www.target.com/p/spaghetti-16oz-good-38-gather-8482/-/A-78779052#lnk=sametab",
                "https://www.target.com/p/boneless-skinless-chicken-breast-1-5-3-2lbs-price-per-lb-good-38-gather-8482/-/A-52205815#lnk=sametab",
                "https://www.target.com/p/all-natural-80-20-ground-beef-1lb-good-38-gather-8482/-/A-13287606#lnk=sametab",
                "https://www.target.com/p/hardwood-smoked-bacon-16oz-market-pantry-8482/-/A-82553151#lnk=sametab",
                "https://www.target.com/p/double-acting-baking-powder-8-1oz-good-38-gather-8482/-/A-77754271#lnk=sametab",
                "https://www.target.com/p/arm-hammer-pure-baking-soda-1lb/-/A-15133726#lnk=sametab",
                "https://www.target.com/p/pure-vanilla-extract-1oz-good-38-gather-8482/-/A-82247560#lnk=sametab",
                "https://www.target.com/p/granulated-sugar-4lbs-good-38-gather-8482/-/A-78471310#lnk=sametab",
                "https://www.target.com/p/unbleached-all-purpose-flour-5lbs-good-38-gather-8482/-/A-77640693#lnk=sametab",
                "https://www.target.com/p/extra-virgin-olive-oil-16-9oz-good-38-gather-8482/-/A-77643078#lnk=sametab",
                "https://www.target.com/p/plain-salt-26oz-good-38-gather-8482/-/A-78140861#lnk=sametab",
                "https://www.target.com/p/ground-black-pepper-3oz-good-38-gather-8482/-/A-77585121#lnk=sametab",
                "https://www.target.com/p/old-fashioned-oats-42oz-good-38-gather-8482/-/A-79364999#lnk=sametab",
                "https://www.target.com/p/beefsteak-tomatoes-13oz-2ct-good-38-gather-8482-packaging-may-vary/-/A-82628083#lnk=sametab",
                "https://www.target.com/p/lightly-salted-dry-roasted-peanuts-16oz-good-38-gather-8482/-/A-78100370#lnk=sametab",
                "https://www.target.com/p/vanilla-bean-ice-cream-1-5qt-favorite-day-8482/-/A-81504855#lnk=sametab"]

    # List of lists of a string of the staple food name and their corresponding price that will be updated below
    staple_food = [["Milk", 0], ["Eggs", 0], ["Bread", 0], ["Staples", 0], ["Butter", 0], ["Ketchup", 0], ["Mustard", 0], ["Mayo", 0], ["Apples", 0], ["Corn", 0], ["Bananas", 0], ["Cream Cheese", 0], ["Peanut Butter", 0], ["Pinto Beans", 0],
                   ["Black Beans", 0], ["White rice", 0], ["Marinara Sauce", 0], ["Spaghetti", 0], ["Chicken Breasts", 0], ["Ground Beef", 0], ["Bacon", 0], ["Baking powder", 0], ["Baking soda", 0], ["Vanilla extract", 0],
                   ["Sugar", 0], ["Flour", 0], ["Olive oil", 0], ["Salt", 0], ["Pepper", 0], ["Oats", 0], ["Tomatoes", 0], ["Peanuts", 0], ["Vanilla ice cream", 0]]
    
    count = 0       # Used to index the staple food list
    
    for j in url_list:    # Iterate through the url list
        
        # Will be added to requests so that the web page believes that the scraper is not a robot
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
        html = requests.get(j, headers=headers)         # Scrapers the information of the webpage
        soup = BeautifulSoup(html.text, "html.parser")  # Uses beautiful soul to parse the web page data
        child_soup = soup.find('body')                  # The body is where the current price is
        for i in child_soup: # Because the body is made up of multiple parts, to find the current price you need to iterate through it
            if i.string != None: # The very first part of the body for each iteration is None, so there is a check for that here
                if i.string.find("$", 30000) != -1: # Check to see if it finds the dollar sign in the string
                    index = i.string.find("$", 30000)   # If find dollar sign, then get its index of the string that it is in
                    word = ""                           # Temp variable to store the price 
                    character = i.string[index]         # Get the first character in the string
                    index += 1                          # Update index
                    while character != "\\":                # Iterate through the string until it hits a backlash, adding all the characters to word
                        word += i.string[index]
                        index += 1
                        character = i.string[index]
                    staple_food[count][1] = word     # Once the price is in word, place it into the correct spot in staple list

                    count += 1 # Update count

    return staple_food   # Once staple food list is updated with the correct data, return it

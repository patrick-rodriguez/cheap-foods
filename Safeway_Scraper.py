"""
Safeway_Scraper.py   - Part of the CheapStaples program
Author: Garrett/Daniel
    Scrapes Safeway's website for food prices & returns the prices
        in a list of pairs


Ouput: list Food names and prices from Safeway website
"""

# Use Beautiful Soup to use as web scraper
from bs4 import BeautifulSoup
import requests


def scrape():
    """
    Desc:
        Scrape Safeway's website of all items within url_list and return
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
    url_list = ["https://www.safeway.com/shop/product-details.960038541.html",  # Milk
                "https://www.safeway.com/shop/product-details.970457016.html",  # Eggs
                "https://www.safeway.com/shop/product-details.960061807.html",  # Bread
                "https://www.safeway.com/shop/product-details.960185056.html",  # Staples
                "https://www.safeway.com/shop/product-details.960012160.html",  # Butter
                "https://www.safeway.com/shop/product-details.105010061.html",  # Ketchup
                "https://www.safeway.com/shop/product-details.105050250.html",  # Mustard
                "https://www.safeway.com/shop/product-details.106010122.html",  # Mayo
                "https://www.safeway.com/shop/product-details.184020020.html",  # Apple
                "https://www.safeway.com/shop/product-details.121150012.html",  # Corn
                "https://www.safeway.com/shop/product-details.184060007.html",  # Bananas
                "https://www.safeway.com/shop/product-details.137100658.html",  # Cream Cheese
                "https://www.safeway.com/shop/product-details.204100011.html",  # Peanut butter
                "https://www.safeway.com/shop/product-details.124150563.html",  # Pinto beans
                "https://www.safeway.com/shop/product-details.124150102.html",  # Black Beans
                "https://www.safeway.com/shop/product-details.126150030.html",  # White Rice
                "https://www.safeway.com/shop/product-details.960032035.html",  # Marinara
                "https://www.safeway.com/shop/product-details.128250110.html",  # Spaghetti
                "https://www.safeway.com/shop/product-details.960261971.html",  # Chicken Breast
                "https://www.safeway.com/shop/product-details.188100110.html",  # Ground Beef
                "https://www.safeway.com/shop/product-details.188530023.html",  # Bacon
                "https://www.safeway.com/shop/product-details.960531997.html",  # Baking Powder
                "https://www.safeway.com/shop/product-details.113450004.html",  # Baking Soda
                "https://www.safeway.com/shop/product-details.214010060.html",  # Vanilla Extract
                "https://www.safeway.com/shop/product-details.960041240.html",  # Sugar
                "https://www.safeway.com/shop/product-details.117100059.html",  # Flour
                "https://www.safeway.com/shop/product-details.115200002.html",  # Olive Oil
                "https://www.safeway.com/shop/product-details.114100007.html",  # Salt
                "https://www.safeway.com/shop/product-details.960136453.html",  # Pepper
                "https://www.safeway.com/shop/product-details.111050086.html",  # Oats
                "https://www.safeway.com/shop/product-details.960533757.html",  # Tomatoes
                "https://www.safeway.com/shop/product-details.960004954.html",  # Peanuts
                "https://www.safeway.com/shop/product-details.142100655.html"   # Vanilla Ice Cream
    ]

    # List of lists of a string of the staple food name and their corresponding price that will be updated below
    staple_food = [["Milk", 0], ["Eggs", 0], ["Bread", 0], ["Staples", 0], ["Butter", 0], ["Ketchup", 0],
                   ["Mustard", 0], ["Mayo", 0], ["Apples", 0], ["Corn", 0], ["Bananas", 0], ["Cream Cheese", 0],
                   ["Peanut Butter", 0], ["Pinto Beans", 0],
                   ["Black Beans", 0], ["White rice", 0], ["Marinara Sauce", 0], ["Spaghetti", 0],
                   ["Chicken Breasts", 0], ["Ground Beef", 0], ["Bacon", 0], ["Baking powder", 0], ["Baking soda", 0],
                   ["Vanilla extract", 0],
                   ["Sugar", 0], ["Flour", 0], ["Olive oil", 0], ["Salt", 0], ["Pepper", 0], ["Oats", 0],
                   ["Tomatoes", 0], ["Peanuts", 0], ["Vanilla ice cream", 0]]
    count = 0

    for i in url_list:  # Iterate through the url list
        # Will be added to requests so that the web page believes that the scraper is not a robot
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
        html = requests.get(i, headers=headers)  # Scrapers the information of the webpage
        soup = BeautifulSoup(html.text, "html.parser")  # Uses beautiful soul to parse the web page data
        product = str(soup.find_all(attrs={"class":"product-container-v2 product-container section"}))
        index = product.find('"price":') + 10
        char = product[index]
        word = ""
        while char != '"':
            word += char
            index += 1
            char = product[index]

        staple_food[count][1] = word
        count += 1
    return staple_food  # Once staple food list is updated with the correct data, return it
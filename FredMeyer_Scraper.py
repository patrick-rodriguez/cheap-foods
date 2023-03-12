"""
WebScraper for FredMeyer site
Author: Garrett Bunkers

Description: This program scrapes staple foods from the FredMeyer site using the Selenium webscraper package.

Output:
tuple(food_res, item_res)

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


food_list = [
    'https://www.fredmeyer.com/p/kroger-extra-large-white-eggs/0001111085429?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/fred-meyer-1-lowfat-milk/0001111041690?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/plugra-unsalted-butter-sticks/0001570021310?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/simple-truth-organic-tomato-ketchup/0001111085853?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-yellow-mustard/0001111081240?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-classic-mayonnaise/0001111001989?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/small-gala-apple/0000000004132?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-supersweet-whole-kernel-corn-cup/0001111087595?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/banana/0000000004011?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-original-sour-cream/0001111046235?fulfillment=PICKUP&searchType=suggestions',
    'https://www.fredmeyer.com/p/kroger-shredded-mexican-style-cheese-blend/0001111050204?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-gluten-free-creamy-peanut-butter/0001111008132?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-pinto-beans/0001111072565?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-black-beans/0001111072567?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-enriched-long-grain-white-rice/0001111089875?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-marinara-pasta-sauce/0001111001448?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-brand-spaghetti-pasta/0001111085004?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/boneless-skinless-chicken-breast-fresh-from-the-service-meat-counter-/0025065640000?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-1-lb-lean-ground-beef-chuck-roll-80-20/0001111097971?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-fully-cooked-hardwood-smoke-flavor-traditional-bacon/0001111097205?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-pure-baking-soda/0001111085451?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/smidge-and-spoon-imitation-vanilla-flavoring/0001111005471?fulfillment=PICKUP&searchType=suggestions',
    'https://www.fredmeyer.com/p/smidge-and-spoon-granulated-sugar/0001111083805?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-unbleached-all-purpose-enriched-flour/0001111086116?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-pure-vegetable-oil/0001111085607?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-iodized-salt/0001111004808?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/smidge-and-spoon-ground-black-pepper/0001111061041?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/mom-s-best-cereals-old-fashioned-oats/0088397815285?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/roma-tomato/0000000004087?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-salted-with-sea-salt-peanuts/0001111061315?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-enriched-white-bread/0001111008485?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/office-works-mini-standard-stapler-with-staples-blue/0001111038388?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-original-cream-cheese/0001111089202?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/simple-truth-organic-filtered-extra-virgin-olive-oil/0001111001120?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-baking-powder/0001111090765?fulfillment=PICKUP&searchType=default_search',
    'https://www.fredmeyer.com/p/kroger-deluxe-vividly-vanilla-ice-cream/0001111050729?fulfillment=PICKUP&searchType=default_search'
]


def merge(list1, list2):
    """
    Desc:
        Takes every element of two lists, put them in a tuple, and return a list of tuples

        Example:
            Input:
                list1 = ['a', 'b', 'c']
                list2 = [1, 2, 3]
            Output:
                merged_list = [('a', 1), ('b', 2), ('c', 3)]

    Parameters:
        list1   (list)  - A list
        list2   (list)  - A list

    Return:
        merged_list (List[Tuples])  - List of tuples on length 2
    """
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list


def scrape():
    """
    Desc:
        Scrapes global link_list and food_list for food prices, then
        sorts the prices into a list of tuples and returns that list.

    Parameters:
        None
        
    Returns:
        food_price_list (List[Tuples]) - List of food and prices in tuples in ("food", "price") format    
    """
    # Init lists
    price_res = []
    food_res = []

    # Selenium Scraper Options
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    # You will probably have to change the argurment below
    # Search "my user agent" on Google then C/P
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")

    # Get the website using the Chrome webbdriver
    real_price = 0
    for w in food_list:
        # Get the website using the Chrome webbdriver
        browser = webdriver.Chrome(options=options)
        browser.get(w)
        print("extracting from: " + w)
        # Scrape the food and price
        food = browser.find_element(By.TAG_NAME, "h1")
        time.sleep(10)
        price = browser.find_element(By.CLASS_NAME, "kds-Price")
        time.sleep(10)
        # Cleaning
        if len(price.text) > 17:
            real_price = price.text.replace("\n", "").replace("about", "").replace("each", "").replace(
                "discounted from", "").replace('$', "").replace('$', "")
            real_price = real_price[len(real_price) // 2:]
            price_res.append(float(real_price))
        # Store data in lists
        else:
            price_res.append(float(price.text.replace("\n", "").replace("about", "").replace("each", "").replace(
                "discounted from", "").replace('$', "").replace('$', "")))
        food_res.append(food.text)
        time.sleep(3)
        browser.close()
        browser.quit()

    food_price_list = merge(food_res, price_res)
    return food_price_list

if __name__ == '__main__':
    scrape()

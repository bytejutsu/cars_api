from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

automobile_url = "https://www.automobile.tn/fr/occasion?keyword="
affare_url = "https://www.affare.tn/petites-annonces/tunisie/voiture-neuve-occassion-prix-tayara-a-vendre?recherche="
baniola_url = "https://baniola.tn/search?q="

keywords = ["peugeot", "206"] # max 3


def delegate_search_url(url_base, keywords):
    return f"{url_base}{'+'.join(keywords)}"


def automobile_search(keywords):
    driver.get(delegate_search_url(automobile_url, keywords))
    articles = driver.find_element(By.CLASS_NAME, "articles").find_elements(By.CLASS_NAME, "occasion-item")

    for article in articles:
        details_wrapper = article.find_element(By.CLASS_NAME, "details-wrapper")
        image = details_wrapper.find_element(By.TAG_NAME, "picture").find_element(By.TAG_NAME, "img")
        thumb_caption = details_wrapper.find_element(By.CLASS_NAME, "thumb-caption")
        description = details_wrapper.find_element(By.TAG_NAME, "p")
        title = thumb_caption.find_element(By.TAG_NAME, "h2")
        price = thumb_caption.find_element(By.CLASS_NAME, "price")
        specs = article.find_element(By.CLASS_NAME, "specs-preview")
        year = specs.find_element(By.CLASS_NAME, "year").find_element(By.CLASS_NAME, "value")
        road = specs.find_element(By.CLASS_NAME, "road").find_element(By.CLASS_NAME, "value")
        map = specs.find_element(By.CLASS_NAME, "map").find_element(By.CLASS_NAME, "value")
        fuel = specs.find_element(By.CLASS_NAME, "fuel").find_element(By.CLASS_NAME, "value")
        gear = specs.find_element(By.CLASS_NAME, "boite").find_element(By.CLASS_NAME, "value")

        print(f'{title.text} : {price.text},\nyear: {year.text}, road: {road.text}, map: {map.text}, fuel: {fuel.text}, gear: {gear.text}\n{image.get_attribute("src")}\n{description.text}\n')


def affare_search(keywords):
    driver.get(delegate_search_url(affare_url, keywords))


def baniola_search(keywords):
    driver.get(delegate_search_url(baniola_url, keywords))


def launch_browser():
    automobile_search(keywords)


launch_browser()







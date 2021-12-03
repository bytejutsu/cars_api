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


def delegate_search(url_base, keywords):
    return f"{url_base}{'+'.join(keywords)}"


def automobile_search(keywords):
    return delegate_search(automobile_url, keywords)


def affare_search(keywords):
    return delegate_search(affare_url, keywords)


def baniola_search(keywords):
    return delegate_search(baniola_url, keywords)


def launch_browser():
    driver.get(baniola_search(keywords))


launch_browser()







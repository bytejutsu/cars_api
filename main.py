from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

automobile_url = "https://www.automobile.tn/fr/occasion/recherche"
autoplus_url = "https://www.auto-plus.tn/voitures-d-occasion.html"
affare_url = "https://www.affare.tn/petites-annonces/tunisie/voiture-neuve-occassion-prix-tayara-a-vendre"
baniola_url = "https://baniola.tn/"
binbincar_url = "https://www.binbincar.tn/vente-voiture/tunisie"
argusautomobile_url = "https://www.argusautomobile.tn/voiture-occasion-tunisie/"

keywords = ["peugeot", "206"] # max 3


with driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://google.com/ncr")
    driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
    first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3")))
    print(first_result.get_attribute("textContent"))

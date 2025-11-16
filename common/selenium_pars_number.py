import time

from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def search_number(link):

    def init_webdriver():
        driver = webdriver.Chrome()
        stealth(
            driver,
            languages=["en-Us", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine"
        )
        return driver


    driver = init_webdriver()
    driver.get(link)

    wait = WebDriverWait(driver, 10)
    time.sleep(5)
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-custom.btn-color-green.show-phone.width100.mb5']")))
    time.sleep(5)
    driver.execute_script("arguments[0].click();", button)

    html = driver.page_source
    print(html)

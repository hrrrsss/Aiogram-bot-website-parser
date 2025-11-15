import time

from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


#Для того чтобы быть скрытным
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

#Для того чтобы скролить 
def scrolldown(driver, deep):
    for _ in range(deep):
        driver.execute_script('window.scrollBy(0, 8)')
        time.sleep(0.1)

#скролим на вкладке рекомендации
driver = init_webdriver()
driver.get("https://avtokavkaza.ru")
scrolldown(driver, 30)
time.sleep(5)


#нажимем на вкладку свежее и скролим для полной прогрузки
wait = WebDriverWait(driver, 10)
tab_fresh = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-tab='fresh']")))
driver.execute_script("arguments[0].click();", tab_fresh)

scrolldown(driver, 30)

time.sleep(10)

#Загрузка спарсенных данных в файл =)
html = driver.page_source

with open("parsing/index.html", "w", encoding="utf-8") as file:
    file.write(html)

driver.quit()
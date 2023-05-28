from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = "https://bot.sannysoft.com/"
driver.get('https://abt.uz/university')
i = 1
while True:
    uni_name = driver.find_element(By.XPATH,
                                   f'/html/body/div[2]/div/article/div/div/div[1]/div[2]/div/div/table/tbody/tr[{i}]/td/a').text
    viloyat = driver.find_element(By.XPATH,
                                  f'/html/body/div[2]/div/article/div/div/div[1]/div[2]/div/div/table/tbody/tr[{i}]/td/div').text
    print(uni_name)
    print(viloyat)
    i += 1

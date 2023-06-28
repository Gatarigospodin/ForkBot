from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.youtube.com/"

with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver:
    driver.get(url)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def  fnd_elem_by_xpath(xpath):
    return driver.find_elements_by_xpath(xpath)

driver = webdriver.Chrome( "./chromedriver")

driver.get("http://google.com/")
fnd_elem_by_xpath('//input[@name="q"]')[0].send_keys('Python Tutorial',Keys.ENTER);

time.sleep(3)
linkList = fnd_elem_by_xpath('//div[@class="r"] //following::cite')
for link in linkList:
    print(link.get_attribute('innerHTML'));

time.sleep(3)
driver.quit();

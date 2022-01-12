from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Test")
driver.find_element(By.NAME,"email").send_keys("test@yopmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("test123")
driver.find_element(By.ID, "exampleCheck1").click()
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female") #When the dropdown options are visible
dropdown.select_by_index("0") #Index of the dropdown options
driver.find_element(By.CSS_SELECTOR,"input[name='inlineRadioOptions']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message
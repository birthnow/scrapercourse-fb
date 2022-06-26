from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time
from credentials


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://facebook.com/")

email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")

email.send_keys(credentials.email)
password.send_keys(credentials.pass)
password.submit()

time.sleep(60)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\\webdriver\\chromedriver.exe')
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

algun_resultado = driver.find_element_by_xpath('//*[@id="content"]/div/section/form/ul/li[2]/h3/a')
algun_resultado.click()

assert "No results found." not in driver.page_source
#driver.close()
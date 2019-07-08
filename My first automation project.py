from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:\chromedriver.exe')

driver.get('http://www.google.co.in/')
searchBar = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
searchBar.send_keys("What is google")
searchBar.send_keys(Keys.RETURN)




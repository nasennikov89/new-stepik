from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = ("http://suninjuly.github.io/selects1.html")
browser.get(link)

num1 = browser.find_element_by_id("num1").text
num2 = browser.find_element_by_id("num2").text
sum = int(num1) + int(num2)
sum = str(sum)

#browser.find_element_by_tag_name("select").click()
#time.sleep(2)
#browser.find_element_by_css_selector("[value='sum']").click()
#time.sleep(2)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(sum)

button = browser.find_element_by_css_selector("button.btn").click()
time.sleep(5)
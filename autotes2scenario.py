from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html" 
    browser = webdriver.Chrome()
    browser.get(link)

    #отправка первого кейса

    firstname = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
    firstname.send_keys("klen")
    lastname = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
    lastname.send_keys("eshe klen")
    email = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
    email.send_keys("enail@gmail.com")

    button =browser.find_element_by_css_selector("button.btn")
    button.click()
    
    #ждем загрузки и успешной регистрации
    time.sleep(1)
    #находим элемент содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    #проверка совпадения текста
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    #ожидание чтобы оценить результат
    time.sleep(5)
    browser.quit()

try:
    link = "http://suninjuly.github.io/registration2.html" 
    browser = webdriver.Chrome()
    browser.get(link)

    #отправка первого кейса

    firstname = browser.find_element_by_xpath("/html/body/div[1]/form/div[1]/div[1]/input")
    firstname.send_keys("klen")
    lastname = browser.find_element_by_xpath("/html/body/div[1]/form/div[1]/div[2]/input")
    lastname.send_keys("eshe klen")
    email = browser.find_element_by_xpath("/html/body/div[1]/form/div[1]/div[3]/input")
    email.send_keys("enail@gmail.com")

    button =browser.find_element_by_css_selector("button.btn")
    button.click()
    
    #ждем загрузки и успешной регистрации
    time.sleep(1)
    #находим элемент содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    #проверка совпадения текста
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    #ожидание чтобы оценить результат
    time.sleep(5)
    browser.quit()
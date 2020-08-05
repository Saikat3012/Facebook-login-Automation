from selenium import webdriver as wd
browser=wd.Chrome("chromedriver.exe")
browser.get("https://www.facebook.com/")
id=browser.find_element_by_id("email")
pas=browser.find_element_by_id("pass")
id.send_keys("Saikat")#instead of 'Saikat' just put your email or mobile number
pas.send_keys("password")#instead of 'password' just put your password
l=browser.find_element_by_id("u_0_b")
l.click()


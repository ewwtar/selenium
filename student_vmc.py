### script for vidyamandir student ### 

### script for vidyamandir student ### 

### script for vidyamandir student ### 
import time
from selenium import webdriver
browser = webdriver.Firefox()
 #driver to use
browser.get('http://student.vidyamandir.com/')
#landing page
#time.sleep(10)
browser.save_screenshot("home.png")

browser.get('http://student.vidyamandir.com/purchasable_course')
#landing page sample courses
#time.sleep(10)
#browser.save_screenshot("sample courses.png")



browser.get('http://student.vidyamandir.com/free_test')
#landing page free tests
#browser.save_screenshot("sample test .png")

#pre log in page
browser.get('http://student.vidyamandir.com/login')
#time.sleep(10)

browser.save_screenshot("prelogin page .png")
roll_number= browser.find_element_by_xpath("//input[@name='email_or_roll_number']")
 #print(roll_number.get_attribute("iit200001"))
roll_number.send_keys("iit200001")

password = browser.find_element_by_xpath("//input[@name='password']")
password.send_keys("123456")

login = browser.find_element_by_xpath("//button[@type='submit']")
login.click()

#forget_password = browser.find_elements_by_id("forget-password").click()



time.sleep(10)
#videos=browser.find_element_by_xpath("//a[@href='/video']")
videos=browser.find_element_by_css_selector('a').get_attribute('href')
print (videos)
videos.click()

#browser.save_screenshot("http://student.vidyamandir.com/dashboard")
#time.sleep(10)
#browser.save_screenshot("http://student.vidyamandir.com/notification/show_all")
#time.sleep(10)

browser.close()




from selenium import webdriver
browser = webdriver.Chrome()
# print(browser)
# browser.get("hhtps://codechef.com")
browser.get('https://www.codechef.com')
#now we know that login username has edit_name as id and login password has edit-password as id
# we use browser.find elemnt by id to find the particular id 
username_element = browser.find_element_by_id("edit-name")
#send key is used to send text to selected element
username_element.send_keys("username")
#now we send the username to slected field
#now we will enter password
password_element = browser.find_element_by_id("edit-pass")
password_element.send_keys("password")
#till now we send password also 
browser.find_element_by_id("edit-submit").click()
#.click() function is used to click the selected field
browser.get("https://www.codechef.com/submit/TEST")
#we got the problem submit page now we have to find the area where we have to submit our code
# browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()
with open ("codechef.cpp" , 'r') as f:
    code = f.read()
code_element = browser.find_element_by_id("edit-program")
#till now we have got our code and also got the place where we have to submit our code 
#now we will use send keys to submit our code
code_element.send_keys(code)
browser.find_element_by_xpath('//*[@id="edit-language"]/option[8]').click()
browser.find_element_by_id("edit-submit").click()




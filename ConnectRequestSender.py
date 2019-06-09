#! Python3

"""Program to web scrape www.linkedin.com search results of employees of 
a particular company whose URL is given and auto send requests to selected 
number of people along with a short note, using Selenium python binding"""

#Importing all necessary modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.linkedin.com/login/")
#driver.get("https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%22162479%22%5D&keywords=QA%20manager&origin=GLOBAL_SEARCH_HEADER")
assert "LinkedIn" in driver.title

"""
element = driver.find_element_by_class_name("sign-in-link")
element.click()

signin_link = driver.find_element_by_tag_name("a")
signin_link.click()
"""

#driver.implicitly_wait(10)
username = driver.find_element_by_id("username")
usrname = input("Please enther the username for this account: ")
username.clear()
username.send_keys(usrname)

password = driver.find_element_by_id("password")
pwd = input("Please type the password: ")
password.clear()
password.send_keys(pwd)

signin_button = driver.find_element_by_xpath("/html/body/div/main/div/form/div[3]/button")
signin_button.click()

driver.get("https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%22162479%22%5D&keywords=QA%20manager&origin=GLOBAL_SEARCH_HEADER")


connect_button1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[6]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li[1]/div/div/div[3]/div/button')));
connect_button1.click();

#//*[@id="ember4967"]/button
#driver.implicitly_wait(10)
#driver.switch_to_active_element('modal-content-wrapper')

#/html/body/div[5]/div[7]/div/div[1]/div/section/div/div[2]/button[1]

#//*[@id="ember150"]/html/body/div[5]/div[6]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li[1]/div/div/div[3]

addNote_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[7]/div/div[1]/div/section/div/div[2]/button[1]')));
addNote_button.click();

custom_message = driver.find_element_by_id('custom-message')
message = """Hi,
I am a Software Engineer with Python scripting and Automation expertise, highly interested in Software QA/ Test Automation Engineer roles. Would like to discuss my background and experience that may align the requirements of your team at Apple. Hoping to astound the world together. 
Sudha"""
#message = line1 + line2 + line3
#message = message.replace("\n", (Keys.SHIFT + Keys.ENTER))
custom_message.clear()
custom_message.send_keys(message)


##ember150 > button:nth-child(1)------/html/body/div[5]/div[6]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li[1]/div/div/div[3]/div/button
# '//*[@id="ember3402"]/button'

"""
for button in connect_buttons:
	print("Entered for loop")
	print(button.get_attribute("button"))
	"""


"""
search_box = driver.find_element_by_xpath("/html/body/header/div/form/div/div/div/artdeco-typeahead-deprecated/artdeco-typeahead-deprecated-input/input")
search_box.send_keys("Apple")
search_box.send_keys(Keys.RETURN)

apple_company = driver.find_element_by_xpath("/html/body/div[5]/div[6]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li[1]/div/div/div[2]/a/h3").click()

#elem.send_keys("sudha")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()

//*[@id="ember3539"]/button
//*[@id="ember3402"]/button

#https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%22162479%22%5D"""
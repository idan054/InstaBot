from selenium import webdriver
import time


options = webdriver.ChromeOptions()
# פיתחת כרום דרך משתמש רגיל
# options.add_argument(f"user-data-dir=C:\\Users\\idanb\\AppData\\Local\\Google\\Chrome\\User Data")
browser = webdriver.Chrome(options=options)

# browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')
try: loginButton = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
except: pass


Trending = browser.find_element_by_link_text('Trending')
Trending.text #לקבל את הטקסט של הערך
Trending.get_attribute("href") #לקבל את הקישור של הערך
Trending.click() #ללחוץ על הערך

searchBar = browser.find_element_by_name("search_query")
searchBar.send_keys("LA LA LA")

from selenium.webdriver.common.keys import Keys  #חלק מהערכה להוספת פעולות נפוצות
searchBar.send_keys(Keys.ENTER)

chooseVideo = browser.find_element_by_link_text("Y2K, bbno$ - Lalala (Official Video)")
chooseVideo.send_keys(Keys.ENTER)
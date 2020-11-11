import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://web.whatsapp.com")
print("Scan QR Code and hit Enter")
input()
print("Logged in")
time.sleep(5)
contact = ''  # Enter name of contact in quotes
msg = ""  # Enter msg to send quotes
search_box = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
search_box.send_keys(contact)
search_box.send_keys(Keys.ENTER)
time.sleep(5)
msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
msg_box.send_keys(msg)
msg_box.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()

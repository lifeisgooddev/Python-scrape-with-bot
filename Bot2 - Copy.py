from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
#predefine constants

categories = ["travel", "food", "adventure"]

browser = webdriver.Chrome()
browser.get("http://google.com")


with open ('a.csv', 'w') as f:
	f.write("No, TERBITAN DAN PENGELOLA	, ID, REGISTRASI, BERKAS, VERIFIKASI, PEMBAYARAN, SK ISSN, NO.ISSN ")

	for tr in trs:
		 tds = tr.find_elements_by_xpath(".//td/font")
		 for td in tds:
		 	key = td.get_attribute("innerHTML")
		 	if key == '&nbsp; √ &nbsp;':
		 		key = "checked"
		 	f.write(key)
		 	f.write(",")


f.close()

# select by visible timext

# while True:
# 	try:
# 		nameElm = browser.find_element_by_name("username")
# 		break
# 	except Exception as e:
# 		pass

# nameElm.send_keys("wproman0211@outlook.com")
# passElm = browser.find_element_by_name("password")
# passElm.send_keys("notouch")
# loginBtn = browser.find_element_by_class_name("L3NKy")
# loginBtn.click()
# while True:
# 	try:
# 		browser.find_element_by_class_name("bIiDR")
# 		break
# 	except Exception as e:
# 		pass
# for category in categories:
# 	browser.get(url + category)
# 	while True:
# 		try:
# 			open_storyElem = browser.find_element_by_class_name("D1yaK")
# 			break
# 		except Exception as e:
# 			pass
# 	open_storyElem.click()
# 	for i in range(15):
# 		time.sleep(1)
# 		while True:
# 			try:
# 				next_btn = browser.find_element_by_class_name("ow3u_")
# 				break
# 			except Exception as e:
# 				pass
# 		next_btn.click()
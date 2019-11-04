from selenium import webdriver


from selenium.webdriver.support.ui import Select
import time
import base64
import os
import unicodedata
#predefine constants

categories = ["travel", "food", "adventure"]

browser = webdriver.Chrome()
browser.get("https://intra2.lipi.go.id/masuk.cgi?depan")


select = Select(browser.find_element_by_xpath('/html/body/center/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/font/center/table[1]/tbody/tr[1]/td[1]/font/b/select'))
select.select_by_value('1036008011')
nama = browser.find_element_by_xpath("/html/body/center/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/font/center/table[1]/tbody/tr[1]/td[1]/font/b/input[1]")

nama.send_keys("wagi004")
kata = browser.find_element_by_xpath("/html/body/center/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/font/center/table[1]/tbody/tr[1]/td[1]/font/b/input[2]")
kata.send_keys("wagiyah7")
loginBtn = browser.find_element_by_xpath("/html/body/center/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/font/center/table[1]/tbody/tr[1]/td[1]/font/b/input[3]")
loginBtn.click()


Issn = browser.find_element_by_xpath("/html/body/center/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td[4]/table/tbody/tr/td[3]/font/a[4]")
Issn.click()

with open('a.csv', 'w', encoding='utf-8') as f:
	f.write("No, TERBITAN DAN PENGELOLA	, ID, REGISTRASI, BERKAS, VERIFIKASI, PEMBAYARAN, SK ISSN, NO.ISSN \n")

	for j in range(1, 254):
		trs = browser.find_elements_by_xpath("/html/body/center/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/font/p[3]/table/tbody/tr")
		for i in range(4,29):
			tds = trs[i].find_elements_by_xpath(".//td/font")
			f.write(tds[0].get_attribute("innerHTML"))
			f.write(",")
			text = tds[1].get_attribute("innerHTML")
			a, b = text.split('</a>')

			a_tag =tds[1].find_elements_by_xpath(".//a")
			name = a_tag[0].get_attribute("innerHTML")
			name = name +b
			name = name.replace(",", " ")
			f.write(name)
			f.write(",")
			for k in range(2,9):
			 	key = tds[k].get_attribute("innerHTML")
			 	key = key.replace("√", "Check")
			 	key = key.replace("×", "Uncheck")
			 	key = key.replace("&nbsp", "")
			 	key = key.replace(";", "")
			 	key = key.replace(",", " ")
			 	
			 	f.write(key)
			 	f.write(",")
			f.write("\n")
		path = '/html/body/center/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/font/p[3]/table/tbody/tr[31]/td/font/a['+str(j)+']'
		print(path)
		pagination = browser.find_element_by_xpath(path)
		pagination.click()


f.close()


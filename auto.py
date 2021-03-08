from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys
from os import system, name 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
clear()
print("\n")
print("Auto Less Secure - Selenium")
listnya = "list.txt"
totalemail = len(list(open(listnya)))
list = open(listnya, 'r')
while True:
	email = list.readline().replace('\n','')
	if not email:
		break
	aww = email.strip().split('|')
	print(aww[0]+'|'+aww[1])
	opts = Options()
	opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36")
	# for windows user use => driver = webdriver.Chrome(executable_path='C:/Python27/chromedriver_win32/chromedriver.exe')
	driver = webdriver.Chrome()
	driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="openid-buttons"]/button[1]'))).click()
	emailInput = driver.find_element_by_xpath('//*[@id="identifierId"]')
	emailInput.send_keys(aww[0])
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]/div/button'))).click()
	button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
	button.click()
	button.send_keys(aww[1])
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/div[2]'))).click()
	time.sleep(5)
	content=driver.page_source
	result = content.find('Welcome to your new account')
	verif = content.find('Verifikasi')
	if (verif != -1):
		driver.delete_all_cookies()
		driver.close()
		driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="openid-buttons"]/button[1]'))).click()
		emailInput = driver.find_element_by_xpath('//*[@id="identifierId"]')
		emailInput.send_keys(aww[0])
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]/div/button'))).click()
		button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
		button.click()
		button.send_keys(aww[1])
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/div[2]'))).click()
		time.sleep(5)
		content=driver.page_source
		result = content.find('Welcome to your new account')
		if (result != -1):
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="accept"]'))).click()
			driver.get('https://myaccount.google.com/lesssecureapps?pli=1')
			button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
			button.click()
			button.send_keys(aww[1])
   			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/div[2]'))).click()
			time.sleep(5)
			content=driver.page_source
			result = content.find('Allow less secure apps: OFF')
			if (result != -1):
				print("[ENABLING...]")
				driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/c-wiz/div/div[2]/div/div/div/ul/li/div/div[2]/div/div/div[2]').click()
				print('ENABLED')
				driver.close()
			else:
				print('ENABLED')
				driver.close()
		else:
			driver.get('https://myaccount.google.com/lesssecureapps?pli=1')
			button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
			button.click()
			button.send_keys(aww[1])
   			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/div[2]'))).click()
			time.sleep(5)
			content=driver.page_source
			result = content.find('Allow less secure apps: OFF')
		if (result != -1):
			print("[ENABLING...]")
			driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/c-wiz/div/div[2]/div/div/div/ul/li/div/div[2]/div/div/div[2]').click()
			print('ENABLED')
			driver.close()
		else:
			print('ENABLED')
			driver.close()
	if (result != -1):
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="accept"]'))).click()
		driver.get('https://myaccount.google.com/lesssecureapps?pli=1')
		button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
		button.click()
		button.send_keys(aww[1])
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/div[2]'))).click()
		time.sleep(5)
		content=driver.page_source
		result = content.find('Allow less secure apps: OFF')
		if (result != -1):
			print("[ENABLING...]")
			driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/c-wiz/div/div[2]/div/div/div/ul/li/div/div[2]/div/div/div[2]').click()
			print('ENABLED')
			driver.close()
		else:
			print('ENABLED')
			driver.close()
	else:
		driver.get('https://myaccount.google.com/lesssecureapps?pli=1')
		button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
		button.click()
		button.send_keys(aww[1])
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/div[2]'))).click()
		time.sleep(5)
		content=driver.page_source
		result = content.find('Allow less secure apps: OFF')
		if (result != -1):
			print("[ENABLING...]")
			driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/c-wiz/div/div[2]/div/div/div/ul/li/div/div[2]/div/div/div[2]').click()
			print('ENABLED')
			driver.close()
		else:
			print('ENABLED')
			driver.delete_all_cookies()
			driver.close()

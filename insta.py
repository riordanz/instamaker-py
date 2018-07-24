#########################################
# Created By riordens17                 #
# Github : github.com/riordanz          #
# Instagram : riordanz.17               #
# Facebook : facebook.com/riordens17    #
#########################################
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from sys import argv
from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.instagram.com/")
wait = WebDriverWait(driver, 600)
wait.until(EC.presence_of_element_located((
	By.NAME, 'emailOrPhone')))
email = driver.find_element_by_name('emailOrPhone')
name = driver.find_element_by_name('fullName')
user = driver.find_element_by_name('username')
passwd = driver.find_element_by_name('password')
btn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[6]/span/button')
email.send_keys(argv[1])
name.send_keys(argv[2])
user.send_keys(argv[3])
passwd.send_keys(argv[4])
sleep(1)
btn.click()
wait.until(EC.presence_of_element_located((
	By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
driver.close()
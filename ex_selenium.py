import os, time
from selenium import webdriver

url = 'https://selenium.dev/documentation/en/'
path = os.getcwd()
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

with webdriver.Chrome(executable_path=path+"/chromedriver", chrome_options=options) as driver:
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/section/div[2]/div[2]/div/label[2]').click()
    time.sleep(2)
    code = driver.find_element_by_xpath('/html/body/section/div[2]/div[2]/div/div/section[2]/div/pre/code').text

with open('code.txt','w') as test:
	test.write(code)
	test.close()

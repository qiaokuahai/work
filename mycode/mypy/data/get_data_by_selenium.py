import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 实例化一款浏览器
bor = webdriver.Chrome(executable_path=r'C:/Users/xiaohai/Desktop/driver/chromedriver.exe')

# 对指定的url发起请求
bor.get('https://www.baidu.com/')
sleep(1)
# 进行标签定位
_input = bor.find_element(By.XPATH, '//*[@id="kw"]')
_input.send_keys('selenium')

btn = bor.find_element(By.XPATH, '//*[@id="su"]')
btn.click()
sleep(1)

all_tags = bor.find_elements(By.XPATH, '//*[@id="content_left"]/child::div')
# all_tags = lefts.find_elements(By.XPATH, '/child')
sibling = bor.find_elements(By.XPATH, '//*[@id="content_left"]/child[1]/following-sibling::*')
name_lst = []
for l in all_tags:
    name = l.find_element(By.XPATH, './/a').text
    name_lst.append(name)
print(json.dumps(name_lst))
sleep(5)

bor.quit()

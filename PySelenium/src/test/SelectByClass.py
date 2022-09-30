# Project : AutoPython
# Datetime : 2022/7/15 23:31
# User : zhangyu
# File : SelectByClass.py
# explain : 文件说明


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# https://chromedriver.chromium.org/home
chorme_driver_path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"

chorme_driver_service = Service(chorme_driver_path)

# 创建 WebDriver 对象
wd = webdriver.Chrome(service=chorme_driver_service)
wd.implicitly_wait(10)

# WebDriver 实例对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')

# 根据 class name 选择元素，返回的是 一个列表
# 里面 都是class 属性值为 animal的元素对应的 WebElement对象
element_exp = wd.find_element(By.CLASS_NAME, 'text-color')
elements = wd.find_elements(By.CLASS_NAME, 'text-color')

# 取出列表中的每个 WebElement对象，打印出其text属性的值
# text属性就是该 WebElement对象对应的元素在网页中的文本内容
print(element_exp.text)
for element in elements:
    print(element.text)



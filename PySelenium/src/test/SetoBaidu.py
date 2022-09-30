# Project : AutoPython
# Datetime : 2022/7/15 17:54
# User : zhangyu
# File : SetoBaidu.py
# explain : 文件说明

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service


# https://chromedriver.chromium.org/home
# chrome 浏览器查看版本，然后去上述网站下载对应版本驱动，放到对应的chrome安装路径下
chorme_driver_path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"

chorme_driver_service = Service(chorme_driver_path)

# 创建 WebDriver 对象
wd = webdriver.Chrome(service=chorme_driver_service)


# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')

# 根据id选择元素，返回的就是该元素对应的WebElement对象
element = wd.find_element(By.ID, 'kw')

# 通过该 WebElement对象，就可以对页面元素进行操作了
# 比如输入字符串到 这个 输入框里
element.send_keys('通讯\n')

time.sleep(2)

wd.quit()
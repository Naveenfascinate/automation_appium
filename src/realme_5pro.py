from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from utlis import app_json, captcha_find, entry


def find_element_with_retry():
    while 1:
        captcha_find(driver, 'realme5')


app_json["udid"] = "d150b8b8"
driver = webdriver.Remote("http://localhost:4727/wd/hub", app_json)

driver.implicitly_wait(15)

entry(driver, 990, 287)
find_element_with_retry()




aa = 1
driver.quit()
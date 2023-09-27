from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from anticaptchaofficial.imagecaptcha import *
from appium.webdriver.common.touch_action import TouchAction
import winsound

app_json = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "appPackage": " com.myv3ads",
    "appWaitActivity": "com.myv3ads.MainActivity",
    "app": "D:\\softwares\\v3\\myv3ads_1.11.apk"
}


def dash_button_click(driver, image_text):
    if image_text == "realme5":
        entry(driver, 990, 287)

def entry_profile(driver, x, y):
    try:
        driver.implicitly_wait(1)
        # nav_bar_element = driver.find_element(MobileBy.XPATH,
        #                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.TextView')
        action = TouchAction(driver)
        action.press(x=x, y=y, pressure=2.0).release().perform()
        action.press(x=x, y=y, pressure=2.0).release().perform()
        action.press(x=x, y=y, pressure=2.0).release().perform()
        driver.implicitly_wait(2)
        ads_element = driver.find_element(MobileBy.XPATH,
                                          '//android.view.View[@content-desc="My Profile"]')
        ads_element.click()
        driver.implicitly_wait(5)
        pre_button = driver.find_element(MobileBy.XPATH,
                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.widget.Button')
        pre_button.click()
    except Exception as e:
        pass


def entry(driver, x, y):
    try:
        driver.implicitly_wait(1)
        # nav_bar_element = driver.find_element(MobileBy.XPATH,
        #                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.TextView')
        print("touching dashboard")
        action = TouchAction(driver)
        action.press(x=x, y=y, pressure=2.0).release().perform()
        action.press(x=x, y=y, pressure=2.0).release().perform()
        action.press(x=x, y=y, pressure=2.0).release().perform()
        driver.implicitly_wait(2)
        ads_element = driver.find_element(MobileBy.XPATH,
                                          '//android.view.View[@content-desc="Advertisement"]')
        ads_element.click()
    except Exception as e:
        entry_profile(driver, x, y)


def captcha_find(driver, image_text):
    try:
        element = driver.find_element(MobileBy.XPATH,
                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View')
        element_edit = driver.find_element(MobileBy.XPATH,
                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.EditText')
        element_submit = driver.find_element(MobileBy.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View/android.view.View[2]/android.widget.Button')
        # print(element.screenshot_as_base64)
        # print(element.screenshot_as_png)
        import base64
        from io import BytesIO

        from PIL import Image
        # from captcha_str import base64_string

        # import pytesseract
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Assuming you have the base64 PNG string stored in the variable 'base64_string'

        # Decode the base64 string into bytes
        image_bytes = base64.b64decode(element.screenshot_as_base64)

        # Open the image from the bytes
        image = Image.open(BytesIO(image_bytes))
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        image.save(image_text + ".jpg", "JPEG")
        # Convert the image to grayscale (if needed)
        # image = image.convert("L")
        # # Extract the captcha string using OCR (e.g., using pytesseract)
        # captcha_string = pytesseract.image_to_string(image)

        # Print the captcha string

        # c_str = captcha_string.split("\n")[0]
        # print(c_str)

        # anit captcha

        solver = imagecaptcha()
        solver.set_verbose(1)
        solver.set_key("ffd290f90204cd96544eb62a0f315564")
        # solver.set_soft_id(0)

        captcha_text = solver.solve_and_return_solution(image_text + ".jpg")

        if captcha_text != 0:
            print("captcha text " + captcha_text)
        else:
            print("task finished with error " + solver.error_code)

        print(captcha_text)

        element_edit.send_keys(captcha_text)
        element_submit.click()
        driver.implicitly_wait(5)
        # go_to_ads()
        # return element, c_str
    except Exception as e:
        # print(e)
        try:
            dashbord_goodmrng = driver.find_element(MobileBy.XPATH,
                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.widget.TextView')

            try:
                text_ele = driver.find_element(MobileBy.XPATH,
                                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.widget.TextView[2]')

                if text_ele.text[:2] in 'CM - SG':
                    if image_text == "realme5":
                        entry(driver, 657, 167)
                    else:
                        winsound.Beep(1000, 5000)
            except Exception as e:
                if image_text == "realme5":
                    entry_profile(driver, 657, 167)


        except Exception as e:
            driver.implicitly_wait(1)
            try:
                click_refresh = driver.find_element(MobileBy.XPATH,
                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.widget.Button')
                click_refresh.click()
            except Exception as e:
                driver.implicitly_wait(0.5)


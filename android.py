from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

build_name = os.environ.get("bamboo_LT_BUILD_NAME")
tunnelName = os.environ.get("bamboo_LT_TUNNEL_NAME")
# build_name = "test-app"
# build_name = "Hello"

desired_caps = {
	"lt:options": {
	    "w3c": True,
	    "deviceName": "Galaxy S21 5G",
            "platformName": "Android",
            "platformVersion": "11",
            "app": "lt://APP10160551841662018882237913",  # Enter app_url here
            "isRealMobile": True,
	        "build" : build_name,
# 		    "tunnel": True,
# 		    "tunnelName":tunnelName,
            "name": "Sample Test - Python",
            "network": True,
            "visual": True,
            "video": True,
	}
    }

   


def startingTest():
    if os.environ.get("bamboo_LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = "username"
    else:
        username = os.environ.get("bamboo_LT_USERNAME")
    if os.environ.get("bamboo_LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = "accesskey"
    else:
        accesskey = os.environ.get("bamboo_LT_ACCESS_KEY")

    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://" +
                                  username+":"+accesskey+"@mobile-hub.lambdatest.com/wd/hub")
        colorElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/color")))
        colorElement.click()

        textElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.lambdatest.proverbial:id/Text")))
        textElement.click()

        toastElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/toast")))
        toastElement.click()

        notification = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/notification")))
        notification.click()

        geolocation = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/geoLocation")))
        geolocation.click()
        time.sleep(5)

        driver.back()

        home = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/buttonPage")))
        home.click()

        speedTest = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/speedTest")))
        speedTest.click()
        time.sleep(5)

        driver.back()

        browser = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/webview")))
        browser.click()

        url = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/url")))
        url.send_keys("https://www.lambdatest.com")

        find = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/find")))
        find.click()
        driver.quit()
    except:
        driver.quit()


startingTest()

import random
import string
from appium import webdriver


class Driver:
    @staticmethod
    def get_driver():
        dc = {
            "platformName": "Android",
            "deviceName": "RZ8M83RZAKM",
            "appActivity": "de.check24.check24.activities.Check24Activity",
            "appPackage": "de.check24.check24",
            "automationName": "UiAutomator2",
            "skipDeviceInitialization": "false",
            "skipServerInstallation": "false",
            "noReset": "false"
        }
        n = 3
        temp1 = (random.choices(string.ascii_lowercase + string.digits, k=n))
        temp2 = "ishan27588+"
        temp3 = "".join(temp1)
        final = temp2+temp3
        email = final + "@gmail.com"
        print("The Email Address is " + email)
        firstname = "Automation"
        second_name = "Check24"
        driver = webdriver.Remote("http://localhost:4723", dc)
        return driver, email, firstname, second_name

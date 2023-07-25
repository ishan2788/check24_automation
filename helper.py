from datetime import time
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.common.exceptions import StaleElementReferenceException, \
    InvalidElementStateException, NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions as pause
from selenium.webdriver.support.ui import WebDriverWait


def click_element(driver, index, path):
    try:
        if index == 0:
            WebDriverWait(driver, 15).until(pause.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, path)))
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, path).click()
        elif index == 1:
            WebDriverWait(driver, 15).until(pause.presence_of_element_located((AppiumBy.XPATH, path)))
            driver.find_element(AppiumBy.XPATH, path).click()
        elif index == 2:
            WebDriverWait(driver, 15).until(pause.presence_of_element_located((AppiumBy.CLASS_NAME, path)))
            driver.find_element(AppiumBy.CLASS_NAME, path).click()
    except StaleElementReferenceException:
        time.sleep(10)
        print("StaleElementReferenceException seen in Send keys", path)
        click_element(driver, index, path)
    except InvalidElementStateException:
        time.sleep(10)
        print("StaleElementReferenceException seen in Send keys", path)
        click_element(driver, index, path)


def send_keys(driver, index, path, keys):
    try:
        if index == 0:
            WebDriverWait(driver, 15).until(pause.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, path)))
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, path).send_keys(keys)
        elif index == 1:
            WebDriverWait(driver, 15).until(pause.presence_of_element_located((AppiumBy.XPATH, path)))
            driver.find_element(AppiumBy.XPATH, path).send_keys(keys)
        elif index == 2:
            WebDriverWait(driver, 15).until(pause.presence_of_element_located((AppiumBy.CLASS_NAME, path)))
            driver.find_element(AppiumBy.CLASS_NAME, path).send_keys(keys)
    except StaleElementReferenceException:
        time.sleep(10)
        print("StaleElementReferenceException seen in Send keys", path, keys)
        send_keys(driver, index, path, keys)
    except InvalidElementStateException:
        print("InvalidElementStateException seen in Send keys", path, keys)
        send_keys(driver, index, path, keys)


def swipe_down(driver):
    try:
        dimension = driver.get_window_size()
        v_start_x = dimension['width'] * 0.5
        v_start_y = dimension['height'] * 0.6
        v_end_x = dimension['width'] * 0.5
        v_end_y = dimension['height'] * 0.3
        driver.flick(v_start_x, v_start_y, v_end_x, v_end_y)
    except InvalidElementStateException:
        swipe_down(driver)
    except StaleElementReferenceException:
        swipe_down(driver)


def swipe_right(driver):
    time.sleep(5)
    dimension = driver.get_window_size()
    path = '(//android.widget.TextView[@text = "Reise"])'
    el = driver.find_element(AppiumBy.XPATH, path)
    loc = el.location
    x_scroll = dimension['width'] * 0.4
    time.sleep(2)
    driver.flick(x_scroll, loc['y'], loc['x'], loc['y'])


def click_coordinate(driver):
    dimension = driver.get_window_size()
    xpoint = dimension['width'] * 0.5
    ypoint = dimension['height'] * 0.5
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(x=xpoint, y=ypoint)
    actions.w3c_actions.pointer_action.click()
    actions.w3c_actions.perform()


def tap_back(driver):
    time.sleep(3)
    try:
        el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "Nach oben")
        while len(el) >= 1:
            time.sleep(2)
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Nach oben").click()
            tap_back(driver)
        return
    except (NoSuchElementException, TimeoutException):
        pass


def close_button(driver):
    time.sleep(3)
    el = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")
    el[0].click()

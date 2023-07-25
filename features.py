from driver import Driver
from helper import *


class Login:
    context = Driver.get_driver()  # Get the driver instance from the Driver class
    driver = context[0]
    email = context[1]
    firstname = context[2]
    secondname = context[3]

    def newuser(self):
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "ok"])')
        time.sleep(2)
        click_element(self.driver, index=1, path='(//android.widget.Button[@text = "NONE OF THE ABOVE"])')
        time.sleep(2)
        path = '(//android.widget.EditText[@text = "E-Mail oder Mobiltelefonnummer"])'
        time.sleep(2)
        send_keys(self.driver, index=1, path=path, keys=self.email)
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "weiter"])')
        click_element(self.driver, index=1, path='(//android.widget.Button[@text = "OK"])')
        time.sleep(3)
        close_button(self.driver)

    def trip(self):
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Reise"])')
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Wohin soll es gehen?"])')
        time.sleep(3)
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Mallorca"])')
        time.sleep(5)
        click_element(self.driver, index=1, path='(//android.widget.Button[@text = "Reise finden"])')
        time.sleep(12)
        for i in range(5):
            swipe_down(self.driver)
            time.sleep(2)
        time.sleep(5)
        self.driver.back()

    def hotel(self):
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Hotel"])')
        time.sleep(3)
        click_coordinate(self.driver)
        time.sleep(2)
        click_element(self.driver, index=1, path='(//android.widget.Button[@text = "Hotels finden"])')
        time.sleep(15)
        for i in range(5):
            swipe_down(self.driver)
            time.sleep(2)
        time.sleep(5)
        click_coordinate(self.driver)
        time.sleep(8)
        try:
            click_element(self.driver, index=1, path='(//android.widget.Button[@text = "Zimmer wählen"])')
            time.sleep(8)
            click_element(self.driver, index=1, path='(//android.widget.Button[@text = "auswählen"])')
            time.sleep(8)
            click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "reservieren"])')
            time.sleep(10)
            click_element(self.driver, index=1, path='(//android.widget.Button[@text = "NONE OF THE ABOVE"])')
        except (NoSuchElementException, TimeoutException):
            pass
        try:
            click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "zur Buchung"])')
        except (NoSuchElementException, TimeoutException):
            pass
        try:
            click_element(self.driver, index=1, path='(//android.widget.Button[@text = "verfügbare Angebote anzeigen"])')
        except (NoSuchElementException, TimeoutException):
            pass
        time.sleep(5)
        tap_back(self.driver)

    def rental_car(self):
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Mietwagen"])')
        time.sleep(3)
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Stadt oder Flughafen eingeben"])')
        time.sleep(3)
        path = '(//android.widget.EditText[@text = "Stadt oder Flughafen eingeben"])'
        send_keys(self.driver, index=1, path=path, keys="mu")
        time.sleep(3)
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "München"])')
        time.sleep(3)
        click_element(self.driver, index=1, path='(//android.widget.Button[@text = "Mietwagen finden"])')
        time.sleep(5)
        for i in range(3):
            swipe_down(self.driver)
            time.sleep(2)
        time.sleep(5)
        click_coordinate(self.driver)
        time.sleep(8)
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "weiter zur Stationsauswahl"])')
        time.sleep(5)
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "weiter zu Extras"])')
        time.sleep(5)
        tap_back(self.driver)

    def flights(self):
        time.sleep(5)
        swipe_right(self.driver)
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Flüge"])')
        time.sleep(2)
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Flughafen wählen"])')
        time.sleep(2)
        path = '(//android.widget.EditText[@text = "Flughafen oder Stadt"])'
        send_keys(self.driver, index=1, path=path, keys="ber")
        time.sleep(2)
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Berlin, Deutschland"])')
        time.sleep(2)
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Flughafen wählen"])')
        time.sleep(2)
        path = '(//android.widget.EditText[@text = "Flughafen oder Stadt"])'
        send_keys(self.driver, index=1, path=path, keys="mu")
        time.sleep(2)
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "München, Deutschland"])')
        time.sleep(7)
        click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "Flug finden"])')
        time.sleep(7)
        for i in range(3):
            swipe_down(self.driver)
            time.sleep(2)
        time.sleep(5)
        try:
            click_coordinate(self.driver)
            time.sleep(5)
            click_element(self.driver, index=1, path='(//android.widget.TextView[@text = "zur Buchung"])')
            time.sleep(8)
            click_element(self.driver, index=1, path='(//android.widget.Button[@text = "NONE OF THE ABOVE"])')
        except (NoSuchElementException, TimeoutException):
            pass
        self.driver.back()
        time.sleep(3)
        try:
            click_element(self.driver, index=1, path='(//android.widget.Button[@text = "BUCHUNG VERLASSEN"])')
            time.sleep(3)
        except (NoSuchElementException, TimeoutException):
            pass
        tap_back(self.driver)

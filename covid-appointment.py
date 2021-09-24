import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

# get your api_id, api_hash, token
# from telegram
api_id = 11111
api_hash = '######'
token = '#####'

# your phone number
phone = '+19999999'

browser = webdriver.Chrome("./chromedriver.exe")

available = False
while not available:
    try:
        browser.get("https://snhd.info/get-vaccine/lvccp")
        time.sleep(5)
        clickMenu = browser.find_element_by_id("dose")
        clickMenu.click()
        time.sleep(0.1)
        clickMenu = browser.find_element_by_id("mat-option-3")
        clickMenu.click()
        time.sleep(0.1)
        clickMenu = browser.find_element_by_id("whereDidYouGetYourFirstDose")
        clickMenu.click()
        time.sleep(0.1)
        clickMenu = browser.find_element_by_id("mat-option-58")
        clickMenu.click()
        time.sleep(0.1)
        clickMenu = browser.find_element_by_css_selector("span.mat-button-wrapper")
        clickMenu.click()
        time.sleep(1)
        clickMenu = browser.find_element_by_id("eligibleGroup")
        clickMenu.click()
        time.sleep(0.1)
        clickMenu = browser.find_element_by_id("mat-option-4")
        clickMenu.click()
        time.sleep(0.5)
        actions = ActionChains(browser)
        actions = actions.send_keys(Keys.TAB)
        actions.perform()
        actions = actions.send_keys(Keys.TAB)
        actions.perform()
        actions = actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(0.5)
        clickMenu = browser.find_element_by_id("isInIsolation")
        clickMenu.click()
        time.sleep(0.1)
        clickMenu = browser.find_element_by_id("mat-option-22")
        clickMenu.click()
        time.sleep(0.1)
        clickMenu = browser.find_element_by_id("mat-select-5")
        clickMenu.click()
        time.sleep(0.1)
        clickMenu = browser.find_element_by_id("mat-option-27")
        time.sleep(0.5)
        clickMenu.click()
        time.sleep(4)
    except Exception as e:
        print(e)
        print("Error. Restarting!")
    try:
        clickMenu = browser.find_element_by_id("mat-button-toggle-1-button")
        if clickMenu.is_displayed():
            # creating a telegram session and assigning
            # it to a variable client
            client = TelegramClient('session', api_id, api_hash)

            # connecting and building the session
            client.connect()

            # in case of script ran first time it will
            # ask either to input token or otp sent to
            # number or sent or your telegram id
            if not client.is_user_authorized():
                client.send_code_request(phone)

                # signing in the client
                client.sign_in(phone, input('Enter the code: '))

            try:
                # sending message using telegram client
                client.send_message('+177777777', 'The Vaccine Appointment is available!', parse_mode='html')
            except Exception as e:
                # there may be many error coming in while like peer
                # error, wrong access_hash, flood_error, etc
                print(e)

            # disconnecting the telegram session
            print("Appointment Found. Message Sent")
            client.disconnect()
            available = True

    except NoSuchElementException as e:
        print("No Appointments Available")

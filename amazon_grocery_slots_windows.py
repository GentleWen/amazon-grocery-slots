import bs4

from selenium import webdriver

import sys
import time
import winsound


def getWFSlot(productUrl):
   driver = webdriver.Chrome()
   driver.get(productUrl)
   html = driver.page_source
   soup = bs4.BeautifulSoup(html)
   time.sleep(30)
   no_open_slots = True

   duration = 3000
   milliseconds freq = 440

   while no_open_slots:
      driver.refresh()
      print("Hey kid, I guess you got a million questions, but I'm just refreshing slots for you..")
      html = driver.page_source
      soup = bs4.BeautifulSoup(html)
      time.sleep(4)

      slot_pattern = 'Next available'
      try:
         next_slot_text = soup.find('h4', class_ ='ufss-slotgroup-heading-text a-text-normal').text
         if slot_pattern in next_slot_text:
            print('SLOTS OPEN! Checkout now!!')
            winsound.Beep(freq, duration)
            no_open_slots = False
            time.sleep(1400)
      except AttributeError:
         continue

      try:
         no_slot_pattern = 'No delivery windows available. New windows are released throughout the day.'
         if no_slot_pattern == soup.find('h4', class_ ='a-alert-heading').text:
            print("NO SLOTS!")
      except AttributeError:
            print('SLOTS OPEN! Checkout now!!')
            winsound.Beep(freq, duration)
            no_open_slots = False

getWFSlot('https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1')
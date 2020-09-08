# Web Scraper built with Selenium to check prices from Amazon

import requests
from time import sleep
from selenium import webdriver
import notify2 


notify2.init(".")
URL = 'https://www.amazon.com.br/gp/product/8537808210?pf_rd_r=SF0S41F6CB9CRXZH2NR6&pf_rd_p=96b1767d-f792-4902-8834-039a970f4513'


class Price_bot():
   def __init__(self):
      self.bot = webdriver.Firefox()

   def open_page(self):
      self.bot.get(URL)
      sleep(8)
# Check if the product price dropped and send a notification

   def check_price(self):
      title = self.bot.find_element_by_id('title').text
      price = self.bot.find_element_by_id('a-autoid-7-announce').text
      result = re.sub('[^0-9]','', price)
      converted_price = float(result[0:2])

      if(converted_price < 59):
         desktop_notify = notify2.Notification(f'The price is {converted_price}')
         desktop_notify.show()

      else:
         print(converted_price)

         
bot = Price_bot()
bot.open_page()
bot.check_price()


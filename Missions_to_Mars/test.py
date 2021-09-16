import pandas as pd
import os
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser

def init_browser():
    executable_path = {"executable_path": "/Users/nallu/.wdm/drivers/chromedriver/win32/92.0.4515.107/chromedriver.exe"}
    return Browser('chrome', **executable_path, headless = False)
    
mars_info = {}
def featured():
  #featured photo

    browser = init_browser()
    executable_path = {"executable_path": "/Users/nallu/.wdm/drivers/chromedriver/win32/92.0.4515.107/chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)
    url = "https://spaceimages-mars.com"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    img_url = soup.find("a",class_='showimg fancybox-thumbs')['href']
    featured_image_url = f"https://spaceimages-mars.com/{img_url}"
    browser.quit()

    return featured_image_url

print(featured())
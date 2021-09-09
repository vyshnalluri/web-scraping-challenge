#dependencies
import pandas as pd
import os
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser

# Initialize browser
def init_browser():
    executable_path = {"executable_path": "/Users/nallu/.wdm/drivers/chromedriver/win32/92.0.4515.107/chromedriver.exe"}
    return Browser('chrome', **executable_path, headless = False)
    
mars_info = {}
def scrape():
   
    browser = init_browser()
                       
    #news
    url = "https://redplanetscience.com/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    news_title = soup.find('div', class_="content_title")
    news_title_text = news_title.a.text
    news_p = soup.find("div", class_="article_teaser_body")
    news_p_text = news_p.text
                       
    #featured photo
    executable_path = {"executable_path": "/Users/nallu/.wdm/drivers/chromedriver/win32/92.0.4515.107/chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)
    url = "https://spaceimages-mars.com"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    img_url = soup.find("a",class_='showimg fancybox-thumbs')['href']
    featured_image_url = f"https://spaceimages-mars.com/{img_url}"
                       
    #mars facts
    mars_facts = pd.read_html("https://galaxyfacts-mars.com")[0]
    mars_facts_df = mars_facts[[0,1]]
    mars_facts_df.columns = ["Label", "Value"]
    mars_facts_df = mars_facts_df.set_index("Label")
    mars_facts_html = mars_facts_df.to_html()
    
    #mars hemispheres
    executable_path = {"executable_path": "/Users/nallu/.wdm/drivers/chromedriver/win32/92.0.4515.107/chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)
    url = "https://marshemispheres.com/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    items = soup.find_all('div', class_='item')
    hemi_main_url = 'https://marshemispheres.com/'

    hemi_img_urls = []
    for item in items: 
        title = item.find('h3').text
        image_url = item.find('a', class_='itemLink product-item')['href']
        browser.visit(hemi_main_url + image_url)
        image_html = browser.html
        soup = bs(image_html, 'html.parser')
        image_url = hemi_main_url + soup.find('img', class_='wide-image')['src']
        hemi_img_urls.append({"Title" : title, "Image_URL" : image_url})
                       
    #storing data into a dictionary
    mars_data_dict = {
        "news_title": news_title_text,
        "news_p": news_p_text,
        "featured_image_url": featured_image_url,
        "df_table":mars_facts_df,
        "hemisphere_img": hemi_img_urls
    }
    # Close the browser after scraping
    browser.quit()
                       
    return mars_data_dict
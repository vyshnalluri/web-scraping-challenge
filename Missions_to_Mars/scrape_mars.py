#dependencies
import pandas as pd
import os
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

    
#mars_info = {}
def scrape_all():
   
    executable_path = {"executable_path": "/Users/nallu/.wdm/drivers/chromedriver/win32/92.0.4515.107/chromedriver.exe"}
    browser = Browser('chrome', **executable_path, headless = False)
    
    news_title, news_p = #complete this part

    #storing data into a dictionary
    mars_data_dict = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url(browser),
        "df_table":mars_facts_df(),
        "hemisphere_img": hemi_img_urls(browser)
    }
    browser.quit()
    return mars_data_dict

#news
def news(browser):
    
    url = "https://redplanetscience.com/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    try:
        slide = soup.select_one('div.list_text')
        news_title = slide.find('div', class_="content_title").get_text()
        news_p = slide.find('div', class_="article_teaser_body").get_text()
    except AttributeError:
        return None, None
    
    return news_title, news_p

    #featured photo
def featured_image_url(browser):

    url = "https://spaceimages-mars.com"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    img_url = soup.find("a",class_='showimg fancybox-thumbs')['href']
    featured_image_url = f"https://spaceimages-mars.com/{img_url}"

    return featured_image_url

#mars facts
def mars_facts():

    try:
        mars_facts_df = pd.read_html("https://galaxyfacts-mars.com")[0]
    except BaseException:
        return None

    mars_facts_df.columns = ["Label", "Mars", "Earth"]
    mars_facts_df.set_index("Label")

    return mars_facts_df.to_html(classes="table table-bordered")

#mars hemispheres
def mars_hemi(browser):

    url = "https://marshemispheres.com/"
    browser.visit(url + 'index.html')
    #soup = bs(html, 'html.parser')
    #items = soup.find_all('div', class_='item')
    #hemi_main_url = 'https://marshemispheres.com/'

    hemi_img_urls = []
    for item in items:
        title = item.find('h3').text
        image_url = item.find('a', class_='itemLink product-item')['href']
        browser.visit(hemi_main_url + image_url)
        image_html = browser.html
        soup = bs(image_html, 'html.parser')
        image_url = hemi_main_url + soup.find('img', class_='wide-image')['src']
        hemi_img_urls.append({"Title" : title, "Image_URL" : image_url})
                       
    # Close the browser after scraping
    browser.quit()
     
    return mars_data_dict
if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape())
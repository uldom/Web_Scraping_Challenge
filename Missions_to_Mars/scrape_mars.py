# Import dependencies and set up
from bs4 import BeautifulSoup
import pandas as pd
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint as pp

# Set Executable Path & Initialize Chrome Browser
def scrape():
    url = 'https://redplanetscience.com'
    data_dict = {}
    # Browser
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    # HTML
    html = browser.html
    # BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    # Select latest news
    title = soup.select_one('div.list_text')
    title = title.find('div', class_='content_title').get_text()
    # Select paragraph
    paragraph = soup.select_one('div.list_text')
    paragraph = paragraph.find('div', class_='article_teaser_body').get_text()
    # Print results, title and paragraph
    print(f"News Title: {title}")
    print(f"News Paragraph: {paragraph}")
    article_dict = {'title': title, 'paragraph': paragraph}
    data_dict ['news'] = article_dict
    print(data_dict)
    return data_dict
    url = 'https://spaceimages-mars.com/'
    data_dict = {}
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    # HTML
    html = browser.html
    # BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    # Home splinter click the 'Full Image' button
    f_image = browser.links.find_by_partial_text('FULL IMAGE').click()
    # Image
    featured_image_url = url + soup.find('img', class_='fancybox-image')['src']
    print(f"Featured Image URL: {featured_image_url}")
    
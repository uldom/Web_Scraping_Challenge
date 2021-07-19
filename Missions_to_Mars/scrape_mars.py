# Import dependencies and set up
from bs4 import BeautifulSoup
import pandas as pd
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint as pp

# Set Executable Path & Initialize Chrome Browser
def scrape():
    # url for NASA Mars News
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

    # New url for JPL Mars Space Images - Featured Image
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    # HTML
    html = browser.html
    # BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    # Home splinter click the 'Full Image' button
    f_image = browser.links.find_by_partial_text('FULL IMAGE').click()
    # HTML
    html = browser.html
    # BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    # Image
    featured_image_url = url + soup.find('img', class_='fancybox-image')['src']
    print(f"Featured Image URL: {featured_image_url}")
    data_dict['image'] = featured_image_url
    
    # New url for Mars Facts
    url = 'https://galaxyfacts-mars.com'
    browser.visit(url)
    html = browser.html
    # BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    # Facts about the planet
    mars_facts = soup.find('table', class_ ='table table-striped')
    mars_facts = pd.read_html(str(mars_facts))[0]
    mars_facts.rename(columns={0: 'Description', 1: 'Values'}, errors='raise', inplace=True)
    mars_facts = mars_facts.to_html()
    # mars_facts = mars_facts.set_index('Description')
    mars_facts
    data_dict['table'] = mars_facts

    # # New url for Mars Hemispheres
    # url = 'https://marshemispheres.com/'
    # browser.visit(url)
    # # Home splinter click the Cerberus Hemisphere image
    # links = browser.find_by_css('.description h3')
    # len(links)
    # links[0].click()
    # title = browser.find_by_css('h2.title')[0].text
    # img_url = browser.find_link_by_text('Original').first
    # img_url = img_url['href']
    # data_dict['title'] = title
    # data_dict['img_url'] = img_url
    
    # Loop de la muerte

    mars_hemispheres=[]

    url = 'https://marshemispheres.com/'
    browser.visit(url)

    for i in range (4):
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')
        links = browser.find_by_css('.description h3')
        links[i].click()
        titles = browser.find_by_css('h2.title').text
        img_url = browser.find_link_by_text('Original').first
        img_url = img_url['href']
        mars_hemispheres.append({'titles': titles, 'img_url':img_url})
        # data_dict['mars_hemispheres'] = article_dict.append ({'title': title, 'img_url': img_url})
        print(titles)
        print(img_url)
        browser.back()
        article_dict = {'titles': titles, 'img_url': img_url}

    data_dict['mars_hemispheres'] = mars_hemispheres


    return data_dict
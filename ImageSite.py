import os
import requests
from selenium import webdriver
import bs4
import webbrowser

searchInput = input("Search: ")


os.makedirs(searchInput, exist_ok=True)

browser = webdriver.Firefox()
browser.get('https://imgur.com/')
elem = browser.find_element_by_css_selector(".Searchbar-textInput")

elem.send_keys(searchInput)

searchElem = browser.find_element_by_css_selector(".search")
searchElem.click()

url = 'https://imgur.com/search?q='+searchInput
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

pictureElem = soup.select('#imagelist img')
if pictureElem == []:
    print("Could not find pictures")
else:
    try:
        for i in pictureElem:
            pictureUrl ='https:' + i.get('src')
            print("Downloading image %s..." % pictureUrl)
            res = requests.get(pictureUrl)
            res.raise_for_status()

            imageFile = open(os.path.join(searchInput, os.path.basename(pictureUrl)), 'wb')
 
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

    except requests.exceptions.MissingSchema:
    	print("could not find picture")


print("Done")

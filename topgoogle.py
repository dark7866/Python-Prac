#! /usr/bin/python3
import bs4, sys, requests, webbrowser
print("Googling...")
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
linkElems = soup.select('.kCrYT a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com'+linkElems[i].get('href'))

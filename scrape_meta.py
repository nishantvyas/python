"""
Scrape meta information title, description, keywords for a given url
"""

import re
import requests
import urllib.request
from bs4 import BeautifulSoup

class scrape_meta:
    """
    Class with methods and attributes to scarape meta information for a given url
    """

    def __init__(self, url):
        """
        Initialize scrape parameters
        """
        self.url = url


    def scrape_url_meta(self):
        """

        :param page:
        :return:
        """
        scrape_url = self.url
        html = requests.get(scrape_url)
        soup = BeautifulSoup(html.text, "html.parser")
        payload = {}

        title = soup.find("meta", property="og:title")
        description = soup.find("meta", property="og:description")
        keywords = soup.find("meta", attrs={"name": "keywords"})

        payload["title"] = title["content"] if title else ""
        payload["description"] = description["content"] if description else ""
        payload["keywords"] = keywords["content"] if keywords else ""

        return payload

    def visible(self, element):
        """
        
        :param element:
        :return:
        """
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
        elif re.match('<!--.*-->', str(element.encode('utf-8'))):
            return False
        return True


    def text_from_html(self):
        """

        :param body:
        :return:
        """

        scrape_url = self.url
        html = urllib.request.urlopen(scrape_url).read()
        soup = BeautifulSoup(html,"lxml")
        texts = soup.findAll(text=True)
        visible_texts = filter(self.visible, texts)

        return u" ".join(t.strip() for t in visible_texts)



if __name__ == "__main__":
    """
    """
    url = "https://www.cnn.com/2018/09/27/politics/brett-kavanaugh-supreme-court-rosenstein-donald-trump/index.html"
    scrapeObj = scrape_meta(url)

    payload = scrapeObj.scrape_url_meta()
    if len(payload) > 0:
        print(payload)

    text_body = scrapeObj.text_from_html()
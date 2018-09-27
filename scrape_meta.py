"""
Scrape meta information title, description, keywords for a given url
"""

import requests
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

        payload["title"] = title["content"] if title else "No meta title given"
        payload["description"] = description["content"] if title else "No meta description given"
        payload["keywords"] = keywords["content"] if keywords else "No meta keywords given"

        return payload




if __name__ == "__main__":

    url = "https://www.cnn.com/2018/09/27/politics/brett-kavanaugh-supreme-court-rosenstein-donald-trump/index.html"
    scrapeObj = scrape_meta(url)

    payload = scrapeObj.scrape_url_meta()
    if len(payload) > 0:
        print(payload)




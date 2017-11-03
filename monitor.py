from bs4 import BeautifulSoup
from Scraping import Scraping
import TargetURLConfig as target_URL
import datetime

class AmazonScraping(Scraping):
    dirpass = "/Users/takumi/PycharmProjects/MonitorUsedPS4Price"

    def getLowestPrice(self, target):
        lowest_price = target.find("span", {"class":"a-size-large a-color-price olpOfferPrice a-text-bold"}).get_text().replace('\n','').replace(' ','')
        print(lowest_price)

if __name__ == '__main__':
    amazon_scraping = AmazonScraping()
    amazon_used_ps4_JB_500GB = amazon_scraping.DownloadURLContents(target_URL.amazon_used_ps4_JB_500GB_price)
    amazon_scraping.getLowestPrice(amazon_used_ps4_JB_500GB)





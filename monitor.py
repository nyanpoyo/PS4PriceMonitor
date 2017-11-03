from bs4 import BeautifulSoup
from Scraping import Scraping
import TargetURLConfig as target_URL
import datetime
import Config

class AmazonScraping(Scraping):

    def getLowestPrice(self, target):
        lowest_price = target.find("span", {"class":"a-size-large a-color-price olpOfferPrice a-text-bold"}).get_text().replace('\n','').replace(' ','')
        return lowest_price

if __name__ == '__main__':
    amazon_scraping = AmazonScraping()
    amazon_price_list = []
    amazon_used_ps4_JB_500GB = amazon_scraping.DownloadURLContents(target_URL.amazon_used_ps4_JB_500GB_price)
    amazon_used_ps4_WH_500GB = amazon_scraping.DownloadURLContents(target_URL.amazon_used_ps4_WH_500GB_price)

    amazon_used_ps4_JB_500GB_lowest_price = amazon_scraping.getLowestPrice(amazon_used_ps4_JB_500GB)
    amazon_used_ps4_WH_500GB_lowest_price = amazon_scraping.getLowestPrice(amazon_used_ps4_WH_500GB)
    amazon_price_list.append(amazon_used_ps4_JB_500GB_lowest_price)
    amazon_price_list.append(amazon_used_ps4_WH_500GB_lowest_price)
    amazon_scraping.SaveData(Config.dir_pass, amazon_price_list, "AmazonLowestPriceLog.txt")
    amazon_scraping.SaveData(Config.dir_pass, "hoge", "AmazonLowestPriceLog.txt")




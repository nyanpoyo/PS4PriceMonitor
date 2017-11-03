from bs4 import BeautifulSoup
from Scraping import Scraping
import TargetURLConfig as target_URL
import datetime
import Config
import re

class AmazonScraping(Scraping):
    def getLowestPrice(self, target):
        lowest_price_info = target.find("span", {
            "class": "a-size-large a-color-price olpOfferPrice a-text-bold"}).get_text().replace('\n', '').replace(' ', '')
        regex = r'\D' #数字以外が対象
        lowest_price = re.sub(regex,'',lowest_price_info)
        return lowest_price

    def getNumOfStar(self, target):
        _star = target.findAll("span", {"class": "a-icon-alt"})
        i = 0
        while (1):
            star_info = _star[i].get_text().replace('\n', '').replace(' ', '')
            if star_info is not None:
                break
            else:
                i = i + 1
        regex = r'[0-5]'
        star = re.findall(regex,star_info)[1]
        star_percent = int(star) / 5 * 100
        return str(star_percent)


if __name__ == '__main__':
    amazon_scraping = AmazonScraping()
    amazon_price_list = []

    amazon_used_ps4_JB_500GB = amazon_scraping.DownloadURLContents(target_URL.amazon_used_ps4_JB_500GB_price)
    amazon_used_ps4_WH_500GB = amazon_scraping.DownloadURLContents(target_URL.amazon_used_ps4_WH_500GB_price)

    amazon_used_ps4_JB_500GB_lowest_price = amazon_scraping.getLowestPrice(amazon_used_ps4_JB_500GB)
    amazon_used_ps4_WH_500GB_lowest_price = amazon_scraping.getLowestPrice(amazon_used_ps4_WH_500GB)

    amazon_used_ps4_JB_500GB_stars = amazon_scraping.getNumOfStar(amazon_used_ps4_JB_500GB)
    amazon_used_ps4_WH_500GB_stars = amazon_scraping.getNumOfStar(amazon_used_ps4_WH_500GB)

    amazon_price_list.append(amazon_used_ps4_JB_500GB_lowest_price)
    amazon_price_list.append(amazon_used_ps4_JB_500GB_stars)
    amazon_price_list.append(amazon_used_ps4_WH_500GB_lowest_price)
    amazon_price_list.append(amazon_used_ps4_WH_500GB_stars)

    amazon_scraping.SaveData(Config.dir_pass, amazon_price_list, "AmazonLowestPriceLog.txt")

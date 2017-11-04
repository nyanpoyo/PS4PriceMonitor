from bs4 import BeautifulSoup
from Scraping import Scraping
from Scraping import AmazonScraping
import TargetURLConfig as target_URL
import Config


if __name__ == '__main__':
    amazon_scraping = AmazonScraping()
    amazon_price_list = []

#Downloat pages
    amazon_used_ps4_JB_500GB = amazon_scraping.DownloadURLContents(target_URL.amazon_used_ps4_JB_500GB_price)
    amazon_used_ps4_WH_500GB = amazon_scraping.DownloadURLContents(target_URL.amazon_used_ps4_WH_500GB_price)
    amazon_new_ps4_JB_500GB = amazon_scraping.DownloadURLContents(target_URL.amazon_new_ps4_JB_500GB_price)
    amazon_new_ps4_WH_500GB = amazon_scraping.DownloadURLContents(target_URL.amazon_new_ps4_WH_500GB_price)

#Get lowest price
    amazon_used_ps4_JB_500GB_lowest_price = amazon_scraping.getUsedLowestPrice(amazon_used_ps4_JB_500GB)
    amazon_used_ps4_WH_500GB_lowest_price = amazon_scraping.getUsedLowestPrice(amazon_used_ps4_WH_500GB)
    amazon_new_ps4_JB_500GB_lowest_price = amazon_scraping.getNewLowestPrice(amazon_new_ps4_JB_500GB)
    amazon_new_ps4_WH_500GB_lowest_price = amazon_scraping.getNewLowestPrice(amazon_new_ps4_WH_500GB)

#Get store evaluation
    amazon_used_ps4_JB_500GB_stars = amazon_scraping.getStoreEvaluation(amazon_used_ps4_JB_500GB)
    amazon_used_ps4_WH_500GB_stars = amazon_scraping.getStoreEvaluation(amazon_used_ps4_WH_500GB)

    amazon_price_list.append(amazon_used_ps4_JB_500GB_lowest_price)
    amazon_price_list.append(amazon_used_ps4_JB_500GB_stars)
    amazon_price_list.append(amazon_used_ps4_WH_500GB_lowest_price)
    amazon_price_list.append(amazon_used_ps4_WH_500GB_stars)
    amazon_price_list.append(amazon_new_ps4_JB_500GB_lowest_price)
    amazon_price_list.append(amazon_new_ps4_WH_500GB_lowest_price)

    amazon_scraping.SaveDataCSV(Config.dir_pass, amazon_price_list, "AmazonLowestPriceLog.txt")

from Scraping import AmazonScraping
import PS4Config as ps4_config
from PS4Config import PS4
import Config
import time
from Scraping import Control
from Tweet import Twitter

if __name__ == '__main__':
    amazon_scraping = AmazonScraping()
    control = Control()
    twitter = Twitter()

    amazon_ps4 = [PS4("CUH-2000AB01", "500GB", "JB", "used", "amazon"),
                  PS4("CUH-2100AB02", "500GB", "WH", "used", "amazon"),
                  PS4("CUH-2100AB01", "500GB", "JB", "new", "amazon"),
                  PS4("CUH-2100AB02", "500GB", "WH", "new", "amazon")]

    csv_output_list = []

    # Set URL
    amazon_ps4[0].URL = ps4_config.amazon_used_ps4_JB_500GB_URL
    amazon_ps4[1].URL = ps4_config.amazon_used_ps4_WH_500GB_URL
    amazon_ps4[2].URL = ps4_config.amazon_new_ps4_JB_500GB_URL
    amazon_ps4[3].URL = ps4_config.amazon_new_ps4_WH_500GB_URL

    # Downloat pages
    amazon_ps4[0].SetObject(amazon_scraping.DownloadURLContents(amazon_ps4[0].URL))
    time.sleep(0.5)  # To avoid 503 Error
    amazon_ps4[1].SetObject(amazon_scraping.DownloadURLContents(amazon_ps4[1].URL))
    time.sleep(0.5)
    amazon_ps4[2].SetObject(amazon_scraping.DownloadURLContents(amazon_ps4[2].URL))
    time.sleep(0.5)
    amazon_ps4[3].SetObject(amazon_scraping.DownloadURLContents(amazon_ps4[3].URL))

    # Get lowest price
    amazon_ps4[0].price = amazon_scraping.getUsedLowestPrice(amazon_ps4[0])
    amazon_ps4[1].price = amazon_scraping.getUsedLowestPrice(amazon_ps4[1])
    amazon_ps4[2].price = amazon_scraping.getNewLowestPrice(amazon_ps4[2])
    amazon_ps4[3].price = amazon_scraping.getNewLowestPrice(amazon_ps4[3])

    # Get store evaluation
    amazon_ps4[0].shop_evaluation = amazon_scraping.getStoreEvaluation(amazon_ps4[0])
    amazon_ps4[1].shop_evaluation = amazon_scraping.getStoreEvaluation(amazon_ps4[1])

    # Output to CSV file
    control.makeOutputList(Config.dir_pass, "AmazonLowestPriceLog.csv", csv_output_list, amazon_ps4)

    amazon_scraping.SaveDataCSV(Config.dir_pass, csv_output_list, "AmazonLowestPriceLog.csv")
    print(csv_output_list)

    for no in range(len(amazon_ps4)):
        amazon_scraping.WriteTweetDraft(Config.dir_pass, "TweetDraft", no, amazon_ps4[no])

    for i in range(len(amazon_ps4)):
        twitter.TweetbyDraft(Config.dir_pass, "TweetDraft"+str(i)+".txt")
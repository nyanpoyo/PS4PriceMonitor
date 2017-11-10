from Scraping import AmazonScraping
import PS4Config as ps4_config
from PS4Config import PS4
import Config
import time
from Scraping import LogControl
from Tweet import Twitter

if __name__ == '__main__':

    amazon_ps4 = [PS4("CUH-2000AB01", "500GB", "JB", "used", "amazon"),
                  PS4("CUH-2100AB02", "500GB", "WH", "used", "amazon"),
                  PS4("CUH-2100AB01", "500GB", "JB", "new", "amazon"),
                  PS4("CUH-2100AB02", "500GB", "WH", "new", "amazon")]

    amazon_compare_num = len(amazon_ps4)
    amazon_scraping = AmazonScraping(amazon_compare_num)
    amazon_scraping.SetDirPass(Config.dir_pass)
    amazon_control = LogControl()
    twitter = Twitter()
    tweet_timing = [False for i in range(amazon_compare_num)]
    csv_output_list = []
    price_archive_list = []

    # Set URL
    for i_url in range(amazon_compare_num):
        amazon_ps4[i_url].URL = ps4_config.amazon_URL_list[i_url]

    # Downloat pagess
    for i_dl in range(amazon_compare_num):
        amazon_ps4[i_dl].SetObject(amazon_scraping.DownloadURLContents(amazon_ps4[i_dl].URL))
        time.sleep(0.5)

    # Get lowest price
    amazon_ps4[0].price = amazon_scraping.getUsedLowestPrice(amazon_ps4[0])
    amazon_ps4[1].price = amazon_scraping.getUsedLowestPrice(amazon_ps4[1])
    amazon_ps4[2].price = amazon_scraping.getNewLowestPrice(amazon_ps4[2])
    amazon_ps4[3].price = amazon_scraping.getNewLowestPrice(amazon_ps4[3])

    # Make archive list
    for i in range(amazon_compare_num):
        price_archive_list.append(amazon_ps4[i].price)

    # Get store evaluation
    amazon_ps4[0].shop_evaluation = amazon_scraping.getStoreEvaluation(amazon_ps4[0])
    amazon_ps4[1].shop_evaluation = amazon_scraping.getStoreEvaluation(amazon_ps4[1])

    # Output to CSV file
    amazon_control.makeOutputList(Config.dir_pass, "AmazonLowestPriceLog.csv", csv_output_list, amazon_ps4, tweet_timing)
    amazon_scraping.SaveDataCSV(csv_output_list, "AmazonLowestPriceLog.csv")
    amazon_scraping.SaveDataCSV(price_archive_list, "AmazonPriceLog.csv")
    print(csv_output_list)
    print(price_archive_list)

    for no in range(amazon_compare_num):
        amazon_scraping.WriteTweetDraft(Config.dir_pass, "TweetDraft", no, amazon_ps4[no])

    for i in range(amazon_compare_num):
        if(tweet_timing[i]):
         twitter.TweetbyDraft(Config.dir_pass, "TweetDraft"+str(i)+".txt")

    print(tweet_timing)

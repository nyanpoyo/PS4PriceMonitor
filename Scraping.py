from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import csv
import sys
import numpy as np
import datetime


class Scraping:
    def DownloadURLContents(self, URL):
        try:
            self.URL = urlopen(URL)

        except HTTPError as he:
            print("Sorry, The server couldn't fulfill your request")
            print("Error code:", he.code)
            sys.exit()

        except URLError as ue:
            print("Failed to search a server")
            print("Reason:", ue.reason)
            sys.exit()

        else:
            print("Connection Success!")
            URL_contents = BeautifulSoup(self.URL.read(), "lxml")
            return URL_contents

    def SaveDataList(self, dirpass, data, file_name):
        try:
            fw = open(dirpass + file_name, 'w')

        except IOError:
            print("Sorry, couldn't open the file")
            sys.exit()

        else:
            if type(data) is list:
                fw.writelines(str(data))
            else:
                fw.write(str(data) + "\n")
        finally:
            fw.close()

    def SaveDataCSV(self, dirpass, data, file_name):
        try:
            fw = open(dirpass + file_name, 'a')

        except IOError:
            print("Sorry, couldn't open the file")
            sys.exit()

        else:
            writer = csv.writer(fw, lineterminator='\n')
            writer.writerow(data)
        finally:
            fw.close()

    def ReadFile(self, dirpass, file_name):
        try:
            fr = open(dirpass + file_name, 'r')

        except IOError:
            print("Sorry, couldn't open the file")
            sys.exit()

        else:
            return fr.read()

        finally:
            fr.close()


class AmazonScraping(Scraping):
    price_difference = []

    def __init__(self, comp_num):
        self.comp_num = comp_num

    def getUsedLowestPrice(self, ps4):
        temp = ps4.bs_obj.findAll("div", {"class": "a-row a-spacing-mini olpOffer"})
        used_lowest_price_info = temp[0].find("span", { "class": "a-size-large a-color-price olpOfferPrice a-text-bold"}).get_text().replace('\n', '').replace(' ',
                                                                                                                   '')
        regex = r'\D'  # 数字以外が対象
        used_lowest_price = re.sub(regex, '', used_lowest_price_info)
        ps4.can_buy = True
        return used_lowest_price

    def getNewLowestPrice(self, ps4):
        try:
         is_sold_out = ps4.bs_obj.find("span", {"class": "a-size-medium a-color-success"}).get_text().replace('\n','').replace(' ', '')

        except AttributeError:
            print("Attribute Error")
            sys.exit()

        else:
         if is_sold_out == "出品者からお求めいただけます。":
            print("Sorry, sold out. You can buy it from other exhibitor")
            ps4.can_buy = False
            return 999999
         elif is_sold_out == "在庫あり。":
            temp = ps4.bs_obj.findAll("tr", {"id": "priceblock_ourprice_row"})
            new_lowest_price_info = temp[0].find("span", {"class": "a-size-medium a-color-price"}).get_text().replace('\n', '').replace(' ', '')
            regex = r'\D'
            new_lowest_price = re.sub(regex, '', new_lowest_price_info)
            ps4.can_buy = True
            return new_lowest_price


    def getStoreEvaluation(self, ps4):
        _star = ps4.bs_obj.findAll("div", {"class": "a-column a-span2 olpSellerColumn"})
        i = 0
        while (True):
            star_info = _star[i]
            if star_info is not None:
                break
            else:
                i = i + 1
        temp = star_info.find("b").string
        regex = r'\D'
        evaluation = re.sub(regex, '', temp)
        return evaluation

    def WriteTweetDraft(self, dir_pass, file_name, text_num, ps4):
        try:
            fw = open(dir_pass + file_name + str(text_num) + ".txt", 'w')

        except IOError:
            print("Sorry, couldn't open the file")
            sys.exit()

        else:
            date = datetime.datetime.today()
            draft = "【" + str(date.month) + "月" + str(date.day) + "日" + str(date.hour) + "時" + str(date.minute) + "分" + "】" + "\nShop:" + ps4.shop + "\nModel:" + ps4.model + "\nStatus:" + ps4.status
            if(ps4.can_buy):
             if(ps4.status=="used"):
                draft = draft + "\nShop Evaluation:" + ps4.shop_evaluation
             draft = draft + "\nPrice:" + str(ps4.price) + "\nPrice difference:" + str(ps4.price_difference) + "\nURL:" + ps4.URL
            else:
                draft = draft + "\nSorry, this product is sold out now. You can buy it other exhibitor."
            fw.write(draft)

        finally:
            fw.close()


class Control:

    def GetLowerPrice(self, dir_pass, price_csv, compared_price, target_row, lowest_price, ps4, tweet_timing):
        log_price_list = np.loadtxt(dir_pass + price_csv, delimiter=',', usecols=(target_row,))

        try:
            lowest_price_in_log = int(np.min(log_price_list))
            print("llog:"+str(lowest_price_in_log))
        except IndexError:
            print("It has failed to indicate the compared price list")
            if log_price_list is None:
                lowest_price[target_row] = compared_price

        else:
            if (compared_price < lowest_price_in_log):
                lowest_price[target_row] = compared_price
                ps4.price_difference = lowest_price_in_log - lowest_price[target_row]
                print("log:"+str(lowest_price_in_log))
                print("Get:"+str(compared_price))
                if(ps4.price_difference > 100000):
                    ps4.price_difference = lowest_price[target_row]
                tweet_timing[target_row] = True
                print(tweet_timing)

            else:
                lowest_price[target_row] = lowest_price_in_log
                tweet_timing[target_row] = False
                print(tweet_timing[target_row])



    def makeOutputList(self, dirpass, price_csv, output_list, ps4, tweet_timing):  # format now price list to output price list
        lowest_price = [999999 for i in range(len(ps4))]
        for i in range(len(ps4)):
         self.GetLowerPrice(dirpass, price_csv, int(ps4[i].price), i, lowest_price, ps4[i], tweet_timing)
         output_list.append(lowest_price[i])
         print(output_list)

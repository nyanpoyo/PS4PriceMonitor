from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import datetime


class Scraping:
    def DownloadURLContents(self, URL):
        try:
            self.URL = urlopen(URL)

        except HTTPError as he:
            print("Sorry, The server couldn't fulfill your request")
            print("Error code:", he.code)

        except URLError as ue:
            print("Failed to search a server")
            print("Reason:", ue.reason)

        else:
            print("Connection Success!")
            URL_contents = BeautifulSoup(self.URL.read(), "lxml")
            return URL_contents

    def SaveData(self, dirpass, data, file_name):
        try:
            fw = open(dirpass + file_name, 'w')

        except IOError:
            print("Sorry, couldn't open the file")

        else:
            if type(data) is list:
                fw.writelines(str(data))
            else:
                fw.write(str(data) + "\n")
        finally:
            fw.close()

    def ReadFile(self, dirpass, file_name):
        try:
            fr = open(dirpass + file_name, 'r')

        except IOError:
            print("Sorry, couldn't open the file")

        else:
            return fr.read()

        finally:
            fr.close()

class AmazonScraping(Scraping):
    def getLowestPrice(self, target):
        lowest_price_info = target.find("span", {
            "class": "a-size-large a-color-price olpOfferPrice a-text-bold"}).get_text().replace('\n', '').replace(' ', '')
        regex = r'\D' #数字以外が対象
        lowest_price = re.sub(regex,'',lowest_price_info)
        return lowest_price

    def getStoreEvaluation(self, target):
        _star = target.findAll("div", {"class": "a-column a-span2 olpSellerColumn"})
        i = 0
        while (1):
            star_info = _star[i]
            if star_info is not None:
                break
            else:
                i = i + 1
        temp = star_info.find("b").string
        regex = r'\D'
        evaluation = re.sub(regex,'',temp)
        return evaluation
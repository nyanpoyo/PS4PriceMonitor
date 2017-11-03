from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


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
            fw = open(dirpass + file_name, 'a')

        except IOError:
            print("Sorry, couldn't open the file")

        else:
            if type(data) is list:
                fw.writelines(data)
            else:
                fw.write(data + "\n")
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

import tweepy


class Twitter:
    # Setting
    CONSUMER_KEY = 'JhlKQ1588Slr3TyvhQV3xORcZ'
    CONSUMER_SECRET = 'hoBOVmcJ4FannA3KFj0mf6sbp0lGkZJlte9hccDKmQSMgOqVTJ'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    ACCESS_TOKEN = '732567257583226880-QRIIXEbcCCi3j5Axxap5li8GGAZFjbT'
    ACCESS_SECRET = 'LBlxDWSfo8aFu3t6R4eA4EWeENuz8CPg6WPBFDRyKhNqz'
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    def TweetbyDraft(self, dir_pass, file_name):
        try:
            fr = open(dir_pass + file_name, 'r')

        except IOError:
            print("Sorry, couldn't open the file")

        else:
            content = fr.read()
            # self.api.update_status(status=content)
            print(content)

        finally:
            fr.close()

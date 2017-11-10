
class PS4():
    def __init__(self,model, HDD_size, color, status, shop):
        self.model = model
        self.HDD_size = HDD_size
        self.color = color
        self.price = 0
        self.status = status
        self.shop = shop
        self.shop_evaluation = 0
        self.price_difference = 0
        self.URL = ""
        self.can_buy = False

    def SetObject(self, bs_obj):
        self.bs_obj = bs_obj


#CUH-2000AB01
amazon_used_ps4_JB_500GB_URL = "https://www.amazon.co.jp/gp/offer-listing/B01LPTFJLO/ref=dp_olp_used?ie=UTF8&condition=used"
#CUH-2100AB02
amazon_used_ps4_WH_500GB_URL = "https://www.amazon.co.jp/gp/offer-listing/B073QT5JK1/ref=dp_olp_used?ie=UTF8&condition=used"
#CUH-2100AB01
amazon_new_ps4_JB_500GB_URL  = "https://www.amazon.co.jp/PlayStation-4-%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%83%BB%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF-500GB-CUH-2100AB01/dp/B0742J781D/ref=sr_1_1?s=videogames&ie=UTF8&qid=1509703090&sr=1-1&keywords=ps4"
#CUH-2100AB02
amazon_new_ps4_WH_500GB_URL  = "https://www.amazon.co.jp/PlayStation-4-%E3%82%B0%E3%83%AC%E3%82%A4%E3%82%B7%E3%83%A3%E3%83%BC%E3%83%BB%E3%83%9B%E3%83%AF%E3%82%A4%E3%83%88-500GB-CUH-2100AB02/dp/B073QT5JK1/ref=sr_1_2?s=videogames&ie=UTF8&qid=1509703090&sr=1-2&keywords=ps4"

amazon_URL_list = [amazon_new_ps4_JB_500GB_URL, amazon_used_ps4_WH_500GB_URL, amazon_new_ps4_JB_500GB_URL, amazon_new_ps4_WH_500GB_URL]
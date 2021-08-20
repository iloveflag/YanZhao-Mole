import requests
from datetime import datetime


class School:
    len = 0

    def __init__(self, title, url):
        self.title = title
        self.url = url

    def check(self):
        r = requests.get(self.url, verify=False)
        l = len(r.text)
        if l!=self.len:
            print(str(self.title)+"有更新"+str(datetime.now()))
            self.len = l
            return True
        else:
            return False




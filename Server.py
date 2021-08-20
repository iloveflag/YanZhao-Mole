import requests


class Server:
    title = "发布了新消息，请查看"
    desp = "请点击进入:"
    ServerUrl = "https://sctapi.ftqq.com/{SendKey}.send"

    def __init__(self, school):
        self.desp += str(school.url)
        self.title = str(school.title)+self.title

    def send(self):
        datas = {'title': self.title, 'desp': self.desp}
        r = requests.post(self.ServerUrl, data=datas)
        print("已通过server酱发送到手机")




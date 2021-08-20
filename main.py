from Server import Server
from School import School
from datetime import datetime, timedelta

if __name__ == '__main__':
    schoollist=[]
    schoollist.append(School("浙江大学", "http://grs.zju.edu.cn/yjszs/redir.php?catalog_id=130678"))
    checktime = datetime.now()-timedelta(days=1)
    while(1):
        while((datetime.now()-checktime).days==1):
            for school in schoollist:
                if(school.check()):
                    s = Server(school)
                    s.send()
            checktime=datetime.now()
            print("每天检查更新完毕:"+str(checktime))


# 来，挑战一下
# 请求的url="https://www.liepin.com/zhaopin/?compkind=&dqs=&pubTime=&pageSize=40&salary=&compTag=180&sortFlag=15&degradeFlag=0&compIds=&subIndustry=&jobKind=&industries=&compscale=&key=%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86&siTag=i9Jq-FcUGTpC9QESjC5G3Q%7EfA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_fp&d_ckId=61ea6ea3f6d5f5edca49995a72e6c97b&d_curPage=0&d_pageSize=40&d_headId=61ea6ea3f6d5f5edca49995a72e6c97b&curPage=0"
import time
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
for i in range(0, 5):
    url = f"https://www.liepin.com/zhaopin/?compkind=&dqs=&pubTime=&pageSize=40&salary=&compTag=180&sortFlag=15&degradeFlag=0&compIds=&subIndustry=&jobKind=&industries=&compscale=&key=%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86&siTag=i9Jq-FcUGTpC9QESjC5G3Q%7EfA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_fp&d_ckId=61ea6ea3f6d5f5edca49995a72e6c97b&d_curPage=0&d_pageSize=40&d_headId=61ea6ea3f6d5f5edca49995a72e6c97b&curPage={i}"

    res = requests.get(url, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, "lxml")
    titles = soup.find_all(class_="sojob-item-main clearfix")
    # gongsi=soup.find(class_="company-name").string
    # print(titles)
    for item in titles:
        it = item.find(class_="field-financing").find("span").string
        if it == "已上市":
            gongsi = item.find(class_="company-name").find("a").string
            zhiwei = item.find("h3").text.strip()
            lianjie = item.find("h3").find("a").attrs["href"]
            save = f"{gongsi},{zhiwei},{lianjie}"
            with open("/Users/工作数据.txt", "a") as f:
                f.write(save + "\n")
    time.sleep(2)
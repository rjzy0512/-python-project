# 使用import导入requests模块
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 将网址赋值给变量url
url = "http://search.jumei.com/?filter=0-41-1&search=&cat=19#search_list_wrap&bid=2_s"

# 将User-Agent以字典键对形式赋值给headers
headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# 将 url 和 headers参数，添加进requests.get()中，将字典headers传递headers参数，给赋值给response
response = requests.get(url, headers=headers)

# 将服务器响应内容转换为字符串形式，赋值给html
html = response.text

# 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html, 'lxml')

# TODO 获取商品名称
# 获取商品价格
# 判断价格区间
content_all=soup.find_all(class_="item_wrap_right")
for content in content_all:
    name=content.find(class_="s_l_name").text.strip()
    jiage=content.find(class_="search_list_price").find("span").text
    if float(jiage) >=50 and float(jiage)<=150:
        with open ("洗面奶.txt","a")as f:
            f.write(f"{name} {jiage}"+"\n")
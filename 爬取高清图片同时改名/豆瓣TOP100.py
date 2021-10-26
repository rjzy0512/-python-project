import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 将User-Agent以字典键对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# TODO 使用for循环遍历range()函数生成的0-3的数字
for i in range(0, 4):

    # TODO 取遍历中的每个数和25相乘计算每页的数值，并赋值给page=i 8
    page = i * 25

    # TODO 用"https://movie.douban.com/top250?start="和page转换成的字符串格式相连，接着在连上"&filter="，并赋值给url
    url = "https://movie.douban.com/top250?start=" + str(page) + "&filter="

    # TODO 将字典headers传递给headers参数
    # 将 url 和 headers参数，添加进requests.get()中，赋值给response=
    response = requests.get(url, headers=headers)

    # TODO 将服务器响应内容转换为字符串形式，赋值给html=
    html = response.text

    # TODO 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html, "lxml")

    # TODO 使用find_all()查询soup中class=title的节点，赋值给content_all

    content_all = soup.find_all(class_="title")
    # TODO for循环遍历content_all
    for content in content_all:
        # TODO 获取每个节点中标签内的内容，赋值给contentString
        contentString = content.string

        # TODO 使用print输出contentString
        print(contentString)
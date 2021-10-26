# 使用import导入requests模块
import requests

# 使用from...import从bs4模块中导入BeautifulSoup
from bs4 import BeautifulSoup

# 复制网页链接赋值给变量url
url = "http://www.xiaowangzi.org/index.html"

# 将User-Agent以字典键值对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# 使用get()函数请求链接，并且带上headers
response = requests.get(url, headers=headers)

# 调用.encoding属性获取requests模块的编码方式
# 调用.apparent_encoding属性获取网页编码方式
# 将网页编码方式赋值给response.encoding
response.encoding = response.apparent_encoding

# 使用.text属性将服务器相应内容转换为字符串形式，赋值给html
html = response.text

# 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html, "lxml")

# TODO 使用find_all()查询soup中的p标签，赋值给content_all

content_all = soup.find_all("p")
# TODO 使用for循环遍历content_all
for content in content_all:

    # TODO 使用find()函数获取img标签，赋值给img
    img = content.find(name="img")

    # TODO 如果img为空
    if img == None:
        # TODO 使用.text获取content节点中的内容，使用split()函数去掉空格和换行符，赋值给sentence
        sentence = content.text.split()

        # TODO 使用join()函数将列表转换成字符串类型，赋值给sentence
        sentence = "".join(sentence)

        # TODO 使用with语句配合open()函数，写入方式设置为"a"，文件名称为"/Users/小王子.txt"
        with open("/Users/小王子.txt", "a") as f:
            # TODO 使用write()将sentence写入，末尾加上换行符"\n"
            f.write(sentence + "\n")
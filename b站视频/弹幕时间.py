# TODO 使用import导入requests模块
import requests

# TODO 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# TODO 将视频弹幕接口链接赋值给变量url

url = "https://comment.bilibili.com/218710655.xml"
# TODO 将变量url作为参数，添加进requests.get()中，给赋值给response
response = requests.get(url)

# TODO 使用.apparent_encoding属性获取网页编码方式
# 将网页编码方式赋值给response.encoding
response.encoding = response.apparent_encoding

# TODO 将服务器响应内容转换为字符串形式，赋值给xml=
xml = response.text

# TODO 使用BeautifulSoup()读取xml，添加lxml解析器，赋值给soup
soup = BeautifulSoup(xml, "lxml")

# TODO 使用find_all()查询soup中d的节点，赋值给content_all
content_all = soup.find_all(name="d")

# TODO 新建一个列表timeList
timeList = []

# TODO for循环遍历content_all
for content in content_all:
    # TODO 使用.attrs获取p对应的属性值，并赋值给data
    data = content.attrs["p"]

    # TODO 使用split()函数按逗号分割data，把第一个元素时间赋值给time

    time = data.split(",")[0]
    # TODO 将time转换成浮点数，添加进列表timeList中

    timeList.append(float(time))
# TODO 使用print输出timeList
print(timeList)
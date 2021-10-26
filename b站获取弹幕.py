import requests

# TODO 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# TODO 将获取到的含有cid的xml地址，赋值给变量url
url="https://comment.bilibili.com/186803402.xml"
#186803402=cid
# TODO 将变量url作为参数，添加进requests.get()中，给赋值给response
response=requests.get(url)

# TODO 使用.text属性获取response内容，赋值给xml
xml=response.text

# TODO 使用BeautifulSoup()读取xml，添加lxml解析器，赋值给soup=B
soup=BeautifulSoup(xml,"lxml")

# TODO 使用find_all()查询soup中d的节点，赋值给content_all=

content_all=soup.find_all("d")
# TODO 输出content_all
print(content_all)
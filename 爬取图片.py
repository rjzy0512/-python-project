# 使用import导入requests模块
import requests

# 使用from..import从bs4模块导入BeautifulSoup
from bs4 import BeautifulSoup

# 将电影URL地址，赋值给变量url
url = "https://movie.douban.com/top250"

# 将User-Agent以字典键对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# 将字典headers传递给headers参数，添加进requests.get()中，赋值给response
response = requests.get(url, headers=headers)

# TODO 将服务器响应内容转换为字符串形式，赋值给html=re

html = response.text
# TODO 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup

soup = BeautifulSoup(html, "lxml")
# TODO 使用find_all()查询soup中class="pic"的节点，赋值给content_all

content_all = soup.find_all(class_="pic")
# TODO for循环遍历content_all

for content in content_all:
    # TODO 使用find()查询content中的img标签，并赋值给imgContent=
    imgContent = content.find(name="img")

    # TODO 使用.attrs获取alt对应的属性值，并赋值给imgName=attts
    imgName = imgContent.attrs["alt"]

    # TODO 使用.attrs获取src对应的属性值，并赋值给imgUrl
    imgUrl = imgContent.attrs["src"]

    # TODO 将链接添加进requests.get()中，赋值给imgResponse
    imgResponse = requests.get(imgUrl)

    # TODO 使用.content属性将响应消息转换成图片数据，赋值给img
    img = imgResponse.content

    # TODO 使用with语句配合open()函数以图片写入的方式打开文件
    # 用格式化将图片名字和.jpg格式组合
    # 打开的文件赋值为f
    with open(f"/Users/qian/{imgName}.jpg", "wb") as f:
        f.write(img)
        # TODO 使用write()将图片写入

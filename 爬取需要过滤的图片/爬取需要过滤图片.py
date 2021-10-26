# TODO 使用import导入requests模块
import requests

# TODO 使用from...import从bs4模块中导入BeautifulSoup
from bs4 import BeautifulSoup

# 将User-Agent以字典键对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# TODO 将URL""""赋值给变量url
url = "https://www.futta.net/photo-season/autumn/"

# TODO 使用get()函数请求链接，并且带上headers
response = requests.get(url, headers=headers)

# TODO 使用.text属性将服务器相应内容转换为字符串形式，赋值给html=
html = response.text

# TODO 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html, "lxml")

# TODO 使用find()查询class="contentsset"属性，并赋值给content_all=
content_all = soup.find(class_="contentsset")

# TODO 使用find_all()查询li标签，并赋值给lis
lis = content_all.find_all(name="li")
# 设置一个计数器count初始值为1
count = 1

# TODO for循环遍历lis
for li in lis:

    # TODO 使用find()查询img标签，并赋值给imgContent
    imgContent = li.find(name="img")

    # TODO 使用if判断，当获取到的img标签内容为None时，就跳过
    if imgContent == None:
        continue

    # TODO 使用.attrs属性获取src对应的属性值，并赋值给imgUrl
    imgUrl = imgContent.attrs["src"]
    print(imgUrl)

    # TODO 使用get()函数请求链接，并赋值给imgResponse
    imgResponse = requests.get(imgUrl)

    # TODO 使用.content属性将响应消息转换成图片数据，赋值给img
    img = imgResponse.content

    # TODO 使用with open()以图片写入的方式打开文件
    # 用格式化将count和.jpg格式组合
    # 打开的文件赋值为f
    print(img)
    with open(f"{count}.jpg", "wb") as f:
        # TODO 使用write()函数写入图片
        f.write(img)

    # TODO 完成一张图片写入时，count计数加1
    count += 1
# 使用import导入requests模块
import requests

# 使用from..import从bs4模块导入BeautifulSoup
from bs4 import BeautifulSoup

# 将User-Agent以字典键对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# 使用for循环遍历range()函数生成的1-2的数字
for page in range(1, 3):

    # 使用格式化方法赋值给变量url
    url = f"https://www.mafengwo.cn/cy/10099/0-0-35291-0-0-{page}.html"

    # 将字典headers传递给headers参数，添加进requests.get()中，赋值给response
    response = requests.get(url, headers=headers)

    # 将服务器响应内容转换为字符串形式，赋值给html
    html = response.text

    # 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html, "lxml")

    # 使用find_all()查询soup中class="item clearfix"的节点，赋值给content_all
    content_all = soup.find_all(class_="item clearfix")

    # for循环遍历content_all
    for content in content_all:
        # TODO 使用find()查询content中class="title"的节点
        # 使用节点选择器找到h3节点下的a节点的内容，用.string获取内容
        # strip()方法去掉首尾空格，并赋值给name

        name = content.find(class_="title").h3.a.string.strip()
        # TODO 使用find()查询content中class="grade"的评分
        # 使用节点选择器找到em节点，用.string获取内容，并赋值给rate
        rate = content.find(class_="grade").em.string
        # print(name)

        # TODO 格式化在name和rate之间加一个"-"，并赋值给imgName
        imgName = f"{name}-{rate}"

        # TODO 使用find()查询content中的img标签，并赋值给imgContent
        imgContent = content.find(name="img")

        # TODO 使用.attrs获取src对应的属性值，并赋值给imgUrl
        imgUrl = imgContent.attrs["src"]

        # TODO 将链接添加进requests.get()中，赋值给imgResponse
        imgResponse = requests.get(imgUrl)

        # TODO 使用.content属性将响应消息转换成图片数据，赋值给img
        img = imgResponse.content

        # TODO 使用with语句配合open()函数以图片写入("wb")的方式打开文件
        # 用格式化将名字和.jpg格式组合，图片保存到路径Users/michelin
        # 打开的文件赋值为f
        with open(f"/Users/michelin/{imgName}.jpg", "wb") as f:
            # TODO 使用write()将图片写入
            f.write(img)
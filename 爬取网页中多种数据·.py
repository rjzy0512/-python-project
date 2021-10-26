# 使用import导入requests模块
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 将URL地址，赋值给变量url
url = "https://book.douban.com/top250?start=0"

# 将User-Agent以字典键对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# 将 url 和 headers参数，添加进requests.get()中，将字典headers传递headers参数，给赋值给response
response = requests.get(url, headers=headers)

# 将服务器响应内容转换为字符串形式，赋值给html
html = response.text

# 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html, "lxml")

# 使用find_all()查询soup中class="item"的节点，赋值给content_all
content_all = soup.find_all(class_="item")

# TODO for循环遍历content_all
for content in content_all:

    # TODO 使用find查询content中class="pl2"的节点(p后面是字母l)，赋值给pl2=c
    pl2=content.find(class_="pl2")

    # TODO 使用.text获取pl2中a标签下的的text文本信息，赋值给title=
    title=pl2.find("a").text

    # TODO 使用replace()去掉title中的换行符"\n"
    title=title.replace("\n","")

    # TODO 使用replace()去掉title=title中的空格
    title=title.replace(" ","")

    # TODO 使用find查询content中class="rating_nums"的节点，赋值给rating_nums=
    rating_nums=content.find(class_="rating_nums")

    # TODO 获取rating_nums节点中的内容，赋值给rate
    rate=rating_nums.string

    # TODO 使用find查询content中class="inq"的节点，赋值给inq=
    inq=content.find(class_="inq")

    # TODO 获取inq节点中的内容，赋值给introduction
    introduction=inq.string

    # TODO 使用格式化输出结果，title,rate,introduction两两之间加空格
    print(f"{title} {rate} {introduction}")


    ##如下图所示，我们可以看到包含“红楼梦”书名的节点没有统一的名称，所以我们不能直接使用find_all()函数。因此，我们需要先使用find()函数获取class="pl2"的节点，然后通过.a方法获取其中的a标签，再通过.text方法，获取a标签下的文本内容，就可以获得“红楼梦”的书名啦。

# 使用find()获取pl2节点
#pl2 = content.find(class_="pl2")
# 使用.text获取pl2中a标签下的的text文本信息
#title = pl2.find("a").text
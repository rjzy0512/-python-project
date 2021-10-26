# 使用import导入requests模块
import requests
# 使用from...import从bs4模块中导入BeautifulSoup模块
from bs4 import BeautifulSoup
# TODO 使用import导入time模块
import time

# 将User-Agent以字典键对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}

# TODO 使用for循环和range()函数，遍历1-10，遍历的变量设为page
for i in range(1, 11):

    # TODO 使用time.sleep()控制，每次循环停顿1秒

    time.sleep(1)
    # 使用格式化拼接链接，赋值给url
    url = f"http://www.mafengwo.cn/cy/10065/0-0-0-0-0-{i}.html"

    # 使用requests.get()请求内容，获取响应消息，赋值给response
    response = requests.get(url, headers=headers)
    # 使用.text属性将服务器相应内容转换为字符串形式，赋值给html
    html = response.text
    # 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html, "lxml")
    # 使用find_all()查询soup中class="item clearfix"的节点，赋值给content_all
    content_all = soup.find_all(class_="item clearfix")

    # for循环遍历content_all
    for content in content_all:
        # TODO 使用find()查询content中的class="grade"的节点，并赋值给content_grade
        content_grade = content.find(class_="grade")

        # TODO 使用节点选择器获取下个节点em标签，并使用.string获取文本内容，赋值给score
        score = content_grade.em.string

        # TODO 使用节点选择器获取p节点下的em节点，使用.string获取文本内容，赋值给review
        review = content_grade.p.em.string

        # TODO 使用find()查询content中的class="title"的节点
        # 获取a节点的.string属性，赋值给title

        title = content.find(class_="title").h3.a.string
        # 使用print()输出title, score, review
        print(title, score, review)
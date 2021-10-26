# 导入需要用到的模块
import requests
from bs4 import BeautifulSoup

# headers
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}

# 创建储存评分与链接的字典scoreDict
scoreDict = {}

# TODO 使用for循环和range()生成1-3的变量并遍历
for i in range(1,4):

    # TODO 使用格式化组合链接，赋值给urli
    url=f"https://www.xiachufang.com/search/?keyword=%E9%B1%BC%E9%A6%99%E8%82%89%E4%B8%9D&cat=1001&page={i}"

    # TODO 使用requests()函数，将url作为参数传入，并将返回值赋值给变量response
    response=requests.get(url,headers=headers)

    # TODO 将服务器响应内容转换为字符串形式，赋值给html
    html=response.text

    # TODO 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup=BeautifulSoup(html,"lxml")

    # TODO 使用find_all()查询soup中class="info pure-u"的节点，赋值给content_all
    content_all=soup.find_all(class_="info pure-u")

    # TODO 使用for循环遍历content_all
    for content in content_all:

        # TODO 使用find()查询content中class="score bold green-font"的节点
        # 并赋值给rate
        rate=content.find(class_="score bold green-font")

        # TODO 如果rate不为空
        if rate !=None:

            # TODO 使用.text属性获取rate的内容，并赋值给score
            score=rate.text

            # TODO 使用节点选择器获取做菜详情链接，选择到content.find("a").attrs["href"]，并赋值给url_rate
            url_rate=content.find("a").attrs["href"]

            # TODO  以做菜详情链接为键和对应的评分为值，添加加入字典
            scoreDict[url_rate]=score

# TODO 使用for循环同时遍历字典scoreDict.items()的key和value
for key,value in scoreDict.items():

    # TODO 使用max()找出字典所有值中最大的值
    # if判断如果value的值为最大值
    if value==max(scoreDict.values()):

        # TODO 将键与"https://www.xiachufang.com"拼接后赋值给link
        link="https://www.xiachufang.com"+key

# TODO 使用requests()函数，将link作为参数传入，并将返回值赋值给变量detail_response
detail_response=requests.get(link,headers=headers)

# 将服务器响应内容转换为字符串形式，赋值给detail_html
detail_html = detail_response.text

# 用BeautifulSoup()传入变量detail_html和解析器lxml，赋值给detail_soup
detail_soup = BeautifulSoup(detail_html, "lxml")

# TODO 使用find_all()查询detail_soup中class="text"的节点，赋值给step_all

step_all=detail_soup.find_all(class_="text")
# 创建计数变量i，并赋值为1
i = 1

# TODO 使用for循环遍历step_all，遍历的变量为step
for step in step_all:

    # TODO 使用.text获取step的文本内容，并赋值给text
    text=step.text

    # TODO 使用格式化输出计数i和步骤内容text，用"."链接
    print(f"{i}.{text}")

    # 将计数变量i的值增加1
    i = i + 1
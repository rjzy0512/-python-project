# 使用import导入requests模块
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# TODO 使用import导入jieba模块

import jieba
# TODO 从pyecharts.charts中导入WordCloud模块

from pyecharts.charts import WordCloud

# 将https://comment.bilibili.com/218710655.xml赋值给变量url
url = "https://comment.bilibili.com/218710655.xml"

# 将变量url作为参数，添加进requests.get()中，给赋值给response
response = requests.get(url)

# 调用.encoding属性获取requests模块的编码方式
# 调用.apparent_encoding属性获取网页编码方式
# 将网页编码方式赋值给response.encoding
response.encoding = response.apparent_encoding

# 将服务器响应内容转换为字符串形式，赋值给xml
xml = response.text

# 使用BeautifulSoup()读取xml，添加lxml解析器，赋值给soup
soup = BeautifulSoup(xml, "lxml")

# 使用find_all()查询soup中d的节点，赋值给content_all
content_all = soup.find_all(name="d")

# TODO 创建一个空白列表wordList
wordList = []

# for循环遍历content_all
for comment in content_all:
    # 使用.string获取弹幕内容，并赋值给data
    data = comment.string

    # TODO 使用jieba.lcut()将data进行分词，赋值给words
    words = jieba.lcut(data)

    # TODO 将列表wordList和列表words进行累加
    wordList += words

# TODO 创建一个空白字典wordDict

wordDict = {}
# TODO for循环遍历列表wordList
for word in wordList:

    # TODO 如果列表中的元素长度大于1
    if len(word) > 1:

        # TODO 如果该元素不存在字典的键中
        if word not in wordDict.keys():

            # TODO 将字典中键所对应的值设置为1
            wordDict[word] = 1

        # TODO 否则
        else:

            # TODO 将字典中键所对应的值累加
            wordDict[word] += 1

# TODO 创建WordCloud对象，赋值给wordCloud
wordCloud = WordCloud()

# TODO 使用add()函数，series_name的值设置为空
# data_pair的值为字典wordDict转换成由元组组成的列表
# 将word_size_range的值设置为[20,80]
wordCloud.add(series_name="", data_pair=wordDict.items(), word_size_range=[20, 80])

# TODO 使用wordCloud.render()存储文件，设置文件名为wordcloud.html
wordCloud.render("wordcloud.html")

# TODO 使用print输出 success
print("success")
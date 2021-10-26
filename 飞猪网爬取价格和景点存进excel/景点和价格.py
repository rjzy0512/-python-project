# 导入requests模块
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 导入time模块
import time

# 使用import导入pandas模块，并使用as简写为pd
import pandas as pd

# 将User-Agent以字典键对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}

# TODO新建一个列表nameList
# 新建一个列表priceList
nameList = []
priceList = []

# TODO for循环遍历range()函数生成的1-5的数字

for page in range(1, 6):
    # TODO 利用格式化字符生成串网站链接 赋值给变量url
    url = f"https://travelsearch.fliggy.com/index.htm?spm=181.61408.a1z7d.6.647523e4uB0Fd3&searchType=product&keyword=%E4%B8%8A%E6%B5%B7&category=SCENIC&ttid=seo.000000576&pagenum={page}"

    # TODO 将url和headers参数，添加进requests.get()中，将字典headers传递给headers参数，给赋值给res
    res = requests.get(url, headers=headers)

    # TODO 使用.text属性获取网页内容，赋值给html
    html = res.text

    # TODO 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html, "lxml")

    # TODO 使用find_all()函数获取class="product-wrap clear-fix"的节点，并赋值给tourist_wraps
    tourist_wraps = soup.find_all(class_="product-wrap clear-fix")

    # TODO for循环遍历tourist_wraps
    for tourist in tourist_wraps:

        # TODO 使用find()函数从节点中获取class="main-title"的节点
        # 使用.string属性提取出标签内容，赋值给title
        title = tourist.find(class_="main-title").string

        # TODO 使用str()将变量title的类型转换成字符串
        title_str = str(title)
        # TODO 如果title_str的第一个字符不是"["
        if title_str[1] != "[":
            # TODO 就把title_str添加进列表nameList中
            nameList.append(title_str)

            # TODO 使用find()函数从节点中获取class="price"的节点,赋值给price_item
            price_item = tourist.find(class_="price")

            # TODO 使用.contents属性提取price_item的子节点,索引第2个元素，赋值给child
            child = price_item.contents[1]

            # TODO 使用append()函数将child添加进列表priceList
            priceList.append(child)

    # TODO 使用time.sleep()停顿2秒
    time.sleep(2)

# TODO 先将获取的列表信息转换成字典类型，赋值给total
total = {"景点名称": nameList, "景点价格/元": priceList}

# TODO 将total传入DataFrame()函数，赋值给info
info = pd.DataFrame(total)

# TODO 使用ExcelWriter()函数打开"/Users/yeye/城市景点.xlsx"文档
# 添加mode参数，设置值为a
# 添加engine，设置值为openpyxl，赋值给writer
writer = pd.ExcelWriter("/Users/yeye/城市景点.xlsx", mode="a", engine="openpyxl")

# TODO 使用to_excel将信息写入writer文档中，并设置工作表名称为上海景点
info.to_excel(writer, sheet_name="上海景点")

# TODO 使用save()函数保存文档
# 使用close()函数关闭文档
writer.save()
writer.save()
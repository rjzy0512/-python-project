# 使用import导入requests模块
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 使用import导入pandas模块，并使用as简写为pd
import pandas as pd

# 将网址赋值给变量url
url = "https://www.tripadvisor.cn/Attractions-g298184-Activities-c47-Tokyo_Tokyo_Prefecture_Kanto.html"

# 将User-Agent以字典键对形式赋值给headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# 新建4个列表，用于存储景点名字nameList、区域districtList、街道addressList和邮编postcodeList
nameList = []
districtList = []
addressList = []
postcodeList = []

# 使用ExcelWriter()函数打开 /Users/东京.xlsx 文档，赋值给writer
writer = pd.ExcelWriter("/Users/东京.xlsx")


# 定义一个新函数getInfo，传入参数info_url
def getInfo(info_url):
    # 将info_url和headers参数，添加进requests.get()中，给赋值给res
    res = requests.get(info_url, headers=headers)

    # 使用.text属性获取网页内容，赋值给html
    html = res.text

    # 用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html, "lxml")

    # TODO 使用find()方法找到景点名字(class="ui_header h1"节点)，使用.text获取文本内容并赋值给name
    name = soup.find(class_="ui_header h1").text

    # TODO 将name添加进nameList中
    nameList.append(name)

    # TODO 使用find()方法找到景点所在区域(class="locality"节点)，使用.text获取文本内容并赋值给district
    district = soup.find(class_="locality").text

    # TODO 将district添加进districtList.中
    districtList.append(district)

    # TODO 使用find()方法找到景点所在区域(class="street-address"节点)，并赋值给address

    address = soup.find(class_="street-address")
    # TODO 判断address不为空
    if address != None:
        # TODO 不为空，使用.text获取文本内容，并赋值给address
        address = address.text
    # TODO 为空
    else:
        # TODO 将address设置为"无"
        address = "无"
    # TODO 将address添加进addressList中
    addressList.append(address)

    # TODO 使用同样的方法处理邮编信息postcode，添加进postcodeList中
    # 获取class="postal-code"节点
    # 判断节点中的内容不为空获取信息，为空设置为无，再添加到列表中
    postcode = soup.find(class_="postal-code")
    if postcode != None:
        postcode = postcode.text
    else:
        postcode = "无"
    postcodeList.append(postcode)


# 将 url 和 headers参数，添加进requests.get()中，将字典headers传递headers参数，给赋值给response
response = requests.get(url, headers=headers)

# 将服务器响应内容转换为字符串形式，赋值给html
html = response.text

# 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
soup = BeautifulSoup(html, "lxml")

# 使用find_all()查询soup中class="attraction_clarity_cell"的节点，赋值给content_all
content_all = soup.find_all(class_="attraction_clarity_cell")

# for循环遍历content_all
for content in content_all:
    # 找到class="listing_title"节点，获取a标签下的href对应的属性值，并赋值给detail_url
    detail_url = content.find(class_="listing_title").a.attrs["href"]

    # 给detail_url加上前缀，并赋值给info_url
    info_url = "https://www.tripadvisor.cn" + detail_url

    # 调用getInfo()函数，传入参数info_url
    getInfo(info_url)

# 先将获取的列表信息转换成字典类型，赋值给total
total = {"景点名称": nameList, "区域": districtList, "街道": addressList, "邮编": postcodeList}

# 将total传入DataFrame()函数，赋值给info
info = pd.DataFrame(total)

# 使用to_excel将信息写入writer文档中，并设置工作表名称为sheet_name="东京景点"
info.to_excel(excel_writer=writer, sheet_name="东京景点")

# 使用save()函数保存文档
writer.save()

# 使用close()函数关闭文档
writer.close()
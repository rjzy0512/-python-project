# 使用import导入requests模块
import requests

# 使用import导入json模块
import json

# 将User-Agent以字典键对形式赋值给headers
headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
# 复制链接并赋值给url
url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=1178886&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=9d8a323c646add49&fold=1"

# 将字典headers传递给headers参数
# 使用get()函数请求链接，赋值给res
res = requests.get(url,  headers=headers)

# 使用.text属性将响应消息转换成字符串，赋值给html
html = res.text

# TODO 使用lstrip()移除左侧的"fetchJSON_comment98("，赋值给html
html=html.lstrip("fetchJSON_comment98(")

# TODO 使用rstrip()移除右侧的");"，赋值给html
html=html.rstrip(");")

# TODO 使用json.loads()将str转换成dict型，赋值给json_data
json_data=json.loads(html)

# TODO 使用"comments"键获取对应的值，赋值给data
data=json_data["comments"]

# TODO 使用for循环遍历列表data中的每一项
for item in data:
    # TODO 提取键creationTime对应的值，赋值给creationTime
    creationTime=item["creationTime"]

    # TODO 提取content对应的值，赋值给content
    content=item["content"]

    # TODO 使用格式化输出creationTime和content，中间空一格
    print(f"{creationTime} {content}")
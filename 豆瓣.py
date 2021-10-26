# 动动你的小脑袋
import requests
import json
from bs4 import BeautifulSoup
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.222 Safari/537.36"}
# 复制链接并赋值给url


for i in range(0,5):
    i = i * 20
    url = f"https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={i}"

# 将字典headers传递给headers参数
# 使用get()函数请求链接，赋值给res
    res = requests.get(url,headers=headers)

# 使用.text属性将响应消息转换成字符串，赋值给html
    html = res.text

    json_data=json.loads(html)
    data=json_data["subjects"]
    for item in data:
        title = item["title"]
        rate = item["rate"]
        json_url1=item["url"]
    #json_url=json_url1.replace("/","")
        print(f"{title} {rate} {json_url1}")

    print(url)
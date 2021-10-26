import requests
from bs4 import  BeautifulSoup

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.222 Safari/537.36"}
#for i in range(1, 4):
url="https://www.dpm.org.cn/lights/royal.html"
response=requests.get(url,headers=headers)
response.encoding = response.apparent_encoding
    ##response.encoding = response.apparent_encoding 把乱码变成中文
html=response.text
soup=BeautifulSoup(html, "lxml")
content_all = soup.find_all(class_="pic")


for content in content_all:
    imgContent = content.find(name="img")


        # TODO 使用.attrs获取imgContent的src的属性值，并赋值给imgUrl
    imgUrl = imgContent.attrs["src"]
    print(imgUrl)
    name = imgContent.attrs["alt"]

    imgResponse = requests.get(imgUrl)
    img = imgResponse.content
    name=name.replace(" ","_")
        # TODO 使用.content属性将响应消息转换成图片数据，赋值给img

    print(name)
        #print(img)
    with open(f"{name}.jpg", "wb") as f:
        f.write(img)
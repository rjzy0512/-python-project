# TODO 使用import导入requests模块
import requests

# TODO 复制左侧的图片地址，赋值给变量url
url="https://npbcz.files.wordpress.com/2020/09/4-1.jpg"


# TODO 将 url 添加进requests.get()中，赋值给response
response=requests.get(url)

# TODO 使用.content属性获取图片内容，并赋值给img
img=response.content

# TODO 使用with...as语句配合open()以wb方式，打开名字为"math.png"的文件，并赋值给f 
with open("math.png","wb")as f:

    # TODO 使用write()函数写入img
    f.write(img)


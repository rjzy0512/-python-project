import requests

pinjie = ".jpg?w=400"
for xunhuan in ["16-1", "17-1", "18-1", "19-1"]:
    url = "https://npbcz.files.wordpress.com/2020/09/" + xunhuan + pinjie
    response = requests.get(url)
    ##使用.content属性获取图片内容，并赋值给img
    img = response.content
    with open(f"{xunhuan}.jpg", "wb") as f:
        f.write(img)

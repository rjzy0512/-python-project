from MyQR import myqr

# TODO 从myqr中调用run()函数
# 添加参数words，参数值为"https://np.baicizhan.com/courses"
# 添加参数save_name，参数值为"yequ.gif"
# 添加参数picture,参数值为"/Users/yequ/running.gif"
# 将二维码设置为彩色
# 边长设置为10
myqr.run(words="love mu little ,love me long",
         save_name="hhh.jpg",
         picture=r"C:\Users\Administrator\Desktop\微信图片_20211017193016.jpg",
         colorized=True,
         version=6)
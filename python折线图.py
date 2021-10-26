# TODO 从pyecharts.charts中导入Line模块
from pyecharts.charts import Line

# A电影的售票数据
y_data_A = [20, 10, 23, 134, 234, 14, 76]

# B电影的售票数据
y_data_B = [125, 82, 25, 62, 45, 74, 156]

# 一周的天数数据
x_data = ["第一天", "第二天", "第三天", "第四天", "第五天", "第六天", "第七天"]

# TODO 使用Line()创建Line对象，赋值给line
line = Line()

# TODO 将列表x_data传入add_xaxis()函数
line.add_xaxis(x_data)

# TODO 使用add_yaxis()函数，将数据统称设置为"A电影"
# 将列表y_data_A传入add_yaxis()函数
line.add_yaxis("A电影", y_data_A)

# TODO 使用add_yaxis()函数，将数据统称设置为"B电影"
# 将列表y_data_B传入add_yaxis()函数
line.add_yaxis("B电影", y_data_B)

# TODO 使用render()函数存储文件，设置文件名为data.html
line.render("data.html")

# TODO 使用print输出success
print("success")
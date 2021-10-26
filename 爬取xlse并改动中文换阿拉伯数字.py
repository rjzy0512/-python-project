# TODO 使用import导入rmbTrans模块

import rmbTrans
# TODO 使用import导入openpyxl模块
import openpyxl

# TODO 读取工作目录下"开口哭牌供货列表.xlsx"，并赋值给变量wb
wb=openpyxl.load_workbook("开口哭牌供货列表.xlsx")

# TODO 获取工作表"6月供货"，赋值给变量ws
ws=wb['6月供货']

# TODO 定义一个变量total_amount，初始值为0

total_amount=0
# TODO 使用for循环，遍历工作表ws的每一行
for hang in ws.rows:
    # TODO 将每一行的第7个元素的单元格值，赋值给变量value
    value=hang[6].value
    # TODO 使用rmbTrans模块中的trans()函数，将每一行的中文金额转换为阿拉伯数字的金额。
    zhunhuan=rmbTrans.trans(value)
    # TODO total_amount + amount，赋值给total_amount
    total_amount=total_amount + zhunhuan

# TODO 使用格式化输出"开口哭牌供应商6月采购总金额为{total_amount}元。"
print(f"开口哭牌供应商6月采购总金额为{total_amount}元。")
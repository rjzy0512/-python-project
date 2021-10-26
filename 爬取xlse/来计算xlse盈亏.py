# 使用import导入openpyxl模块
import openpyxl


# 将计算单月销售额的步骤移到函数gmv()中,参数path：销售数据Excel文件路径,返回值：计算出的销售结果
def gmv(path):
    # ##TODO## 添加data_only = True，读取路径path的工作簿，赋值给变量wb
    wb = openpyxl.load_workbook(path, data_only=True)

    # ##TODO## 读取名为"销售订单数据"的工作表并赋值给变量ws
    ws = wb["销售订单数据"]

    # 定义一个变量total_amount来表示本月总销售额
    total_amount = 0

    # 遍历工作表的所有行数据
    for row in ws.rows:

        # 总价在9列，索引也就是8，获取索引为8的单元格值
        amount = row[8].value

        # ##TODO## 使用type()函数，判断如果单元格值的数据类型是整型
        if type(amount) == int:
            # ##TODO## 逐个添加总价到本月销售额total_amount里
            total_amount += amount

    # ##TODO## 将计算后的销售额返回
    return total_amount


# ##TODO## 循环遍历1～12的数字
for yue in range(1, 13):

    # ##TODO## 利用格式化字符串，拼接Excel文件名"2019年{month}月销售订单.xlsx"，组成路径赋值给变量path
    path = f"2019年{yue}月销售订单.xlsx"

    # ##TODO## 使用定义的gmv函数，传入path，将结果赋值给monthly_gmv
    monthly_gmv = gmv(path)

    # ##TODO## 判断如果monthly_gmv大于8500
    if monthly_gmv > 8500:
        # ##TODO## 格式化输出"{month}月是盈利的。盈利{monthly_gmv-8500}元。"
        print(f"{yue}月是盈利的。盈利{monthly_gmv - 8500}元。")
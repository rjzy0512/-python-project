# TODO 使用import导入openpyxl模块
import openpyxl

# TODO 添加data_only = True，读取工作目录里名为"平台销售订单.xlsx"的工作簿并赋值给变量wb_mall=o
wb_mall = openpyxl.load_workbook("平台销售订单.xlsx", data_only=True)

# TODO 读取名为"销售订单数据"的工作表并赋值给变量ws_mall
ws_mall = wb_mall["销售订单数据"]

# TODO 定义一个空列表，赋值给变量mall_order_id_list

mall_order_id_list = []
# TODO 遍历工作表ws_mall的所有行数据
for rows in ws_mall.rows:
    # TODO 读取每一行的第一个单元格值，赋值给变量mall_order_id
    mall_order_id = rows[0].value

    # TODO 使用append()，将mall_order_id插入列表mall_order_id_list
    mall_order_id_list.append(mall_order_id)

# TODO 使用pop()，删去列表mall_order_id_list的第一个元素

mall_order_id_list.pop(0)

# TODO 添加data_only = True，读取工作目录里名为"系统数据.xlsx"的工作簿并赋值给变量wb_system=o

wb_system = openpyxl.load_workbook("系统数据.xlsx", data_only=True)
# TODO 读取名为"订单数据"的工作表并赋值给变量ws_system
ws_system = wb_system["订单数据"]

# TODO 定义一个空列表，赋值给变量system_order_id_list
system_order_id_list = []

# TODO 遍历工作表ws_system的所有行数据
for rows_system in ws_system.rows:
    # TODO 读取每一行的第二个单元格值，赋值给变量system_order_id
    system_order_id = rows_system[1].value
    # print(system_order_id)
    # TODO 使用append()，将system_order_id插入列表system_order_id_list
    system_order_id_list.append(system_order_id)

# TODO 使用pop()，删去列表system_order_id_list的第一个元素
system_order_id_list.pop(0)

# TODO 遍历列表mall_order_id_list中的所有元素item
for item in mall_order_id_list:

    # TODO 判断item如果不在列表system_order_id_list中
    if item not in system_order_id_list:
        # TODO 使用格式化输出"订单号 xxxxxx 不在系统数据中"
        print(f"订单号 {item} 不在系统数据中")

# TODO 遍历列表system_order_id_list中的所有元素item
for item in system_order_id_list:

    # TODO 判断item如果不在列表mall_order_id_list中
    if item not in mall_order_id_list:
        print(f"订单号 {item} 不在商城数据中")
        # TODO 使用格式化输出"订单号 xxxxxx 不在商城数据中"

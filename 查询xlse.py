# TODO 导入openpyxl模块

import openpyxl


# TODO 定义函数queryPhone，通过姓名查询电话号码
# 参数 queryName: 要查询的姓名
# 返回值: 返回一个所有匹配查询用户名的电话号码组成的列表，如果没有查询到就返回空列表
def queryPhone(queryName):
    # TODO 使用openpyxl.load_workbook打开工作簿：电话本.xlsx，赋值给wb=变量
    wb = openpyxl.load_workbook("电话本.xlsx", data_only=True)

    # TODO 通过变量wb和中括号获取名为：电话簿 的工作表对象赋值给sheet变量
    sheet = wb["电话簿"]

    # 定义一个列表queryResult来装返回结果
    queryResult = []

    # 遍历行数据，逐个判断姓名是否跟查询的姓名匹配
    for rowData in sheet.rows:
        # TODO 每一行第一个单元格是姓名, 第二个单元格是电话号码
        # 将姓名赋值给变量name 电话号码赋值给变量phone
        name = rowData[0].value
        phone = rowData[1].value

        # TODO 判断如果姓名name跟查询的姓名queryName一样
        if name == queryName:
            # TODO 就把电话号码使用append函数添加到queryResult中
            queryResult.append(phone)

    # TODO 查询完成，返回结果queryResult
    return queryResult


queryPhone("郭坪")

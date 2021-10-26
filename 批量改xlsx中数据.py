# TODO 使用import导入openpyxl模块
import openpyxl
import os

# TODO 使用import导入os模块


# TODO 将2019年订单文件路径'/Users/zhener/doc'赋值给path
path = '/Users/zhener/doc'
#地址
# TODO 使用os.listdir()获取路径下所以文件名，赋值给fileNames

fileNames = os.listdir(path)
# TODO 使用for循环逐个列表中的获取文件名
for file in fileNames:

    # TODO 使用os.path.join()拼接文件路径，赋值给filePath
    filePath = os.path.join(path, file)

    # TODO 使用openpyxl.load_workbook()打开文件，赋值给wb
    wb = openpyxl.load_workbook(filePath)

    # TODO 使用for循环遍历工作簿对象的 .worksheets 属性
    for sheel in wb.worksheets:

        # TODO for循环逐行遍历工作表的 .rows 属性
        for row in sheel.rows:

            # TODO 使用if判断第3列单元格值为"有点酸可乐"时

            if row[2].value == "有点酸可乐":
                # TODO 修改单元格的值为"有点酸甜可乐"
                row[2].value = "有点酸甜可乐"

    # TODO 格式化方法将文件以原名称保存到路径 "/Users/zhener/revise"
    wb.save(f'/Users/zhener/revise/{file}')
    #地址
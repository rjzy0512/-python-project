# TODO 使用import导入os模块
import os

# TODO 使用import导入openpyxl模块

import openpyxl
# TODO 使用import导入shutil模块
import shutil

# TODO 使用openpyxl.load_workbook()打开v/Users/giraffe/长颈鹿图书馆.xlsx' ，并赋值给wb

wb = openpyxl.load_workbook(r'C:\Users\Administrator\Downloads\giraffe\giraffe/长颈鹿图书馆.xlsx')
# TODO 使用wb将 长颈鹿图书馆书籍清单 工作表，并赋值给allBooks

allBooks = wb['长颈鹿图书馆书籍清单']
# TODO 定义一个空列表 bookName 用于存储图书名称
bookName = []

# TODO 使用for循环逐行遍历allBooks的所有行
for hang in allBooks.rows:

    # TODO 使用if语句判断第五列的值为"计算机科学"时
    if hang[4].value == "计算机科学":
        # TODO 将满足条件的第2列的书籍名字添加到列表bookName中
        bookName.append(hang[1].value)

# TODO 将电子图书存储路径 '/Users/giraffe/books' 赋值给path=""
path = r"C:\Users\Administrator\Downloads\giraffe\giraffe\books"

# TODO 使用os.listdir()获取路径下的文件名称，赋值给fileNames=
fileNames = os.listdir(path)

# TODO 使用for循环遍历books文件夹中所有文件名称
for item in fileNames:

    # TODO 使用os.path.splitext()分割文件后缀名，并获取文件名称赋值给title
    title = os.path.splitext(item)[0]

    # TODO 使用if语句判断文件名称title在书籍列表中时
    if title in bookName:
        # TODO 满足条件时使用os.path.join()拼接文件存储位置，并赋值给filePath=
        filePath = os.path.join(path, item)

        # TODO 使用shutil.move()函数移动文件到目标路径 '/Users/giraffe/计算机科学'

        shutil.move(filePath, r'C:\Users\Administrator\Downloads\giraffe\giraffe\计算机科学')
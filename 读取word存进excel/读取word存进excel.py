# TODO 使用import导入docx

import docx
# TODO 使用import导入openpyxl模块

import openpyxl

# TODO 读取数学英语词汇的Word文档，并赋值给变量wordDoc
wordDoc = docx.Document(r"C:\Users\Administrator\PycharmProjects\pythonProject\读取word存进excel\tingting\数学英语词汇.docx")

# TODO 定义一个空列表wordList来装入重点单词

wordList = []
# TODO 使用for循环遍历文档中所有段落
for para in wordDoc.paragraphs:

    # TODO  使用for循环遍历段落中的每个样式块
    for run in para.runs:

        # TODO 使用if语句判断当前样式块是否加粗或有下划线
        if run.bold or run.underline:
            # TODO 如果是，则使用append()函数将该单词添加到wordList列表中
            wordList.append(run.text)

# TODO 创建一个新工作簿，并赋值给变量newWb

newWb = openpyxl.Workbook()
# TODO 将名为Sheet的默认工作表赋值给变量sheet
sheet = newWb["Sheet"]

# TODO 将sheet工作表名称修改为"数学"
sheet.title = "数学"

# TODO 使用for循环和enumerate()函数
# 遍历存放了重点单词的列表wordList的同时
# 生成一个从1开始的索引index
for index, word in enumerate(wordList, 1):
    # TODO 将重点单词逐行赋值到表格中的A列中
    sheet[f"A{index}"].value = word

# TODO 将工作簿保存到指定路径 /Users/tingting/重点单词.xlsx
newWb.save(r"C:\Users\Administrator\PycharmProjects\pythonProject\读取word存进excel\重点单词.xlsx")
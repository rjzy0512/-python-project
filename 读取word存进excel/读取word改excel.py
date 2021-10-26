# 使用import导入docx
import docx
# 使用import导入openpyxl模块
import openpyxl

# 读取数学英语词汇的Word文档，并赋值给变量wordDoc
wordDoc = docx.Document(r"C:\Users\Administrator\PycharmProjects\pythonProject\读取word存进excel\tingting\数学英语词汇.docx")

# TODO 定义一个空列表correctList来装入重点单词的中文意思

correctList = []
# 遍历文档中所有段落
for para in wordDoc.paragraphs:
    # 遍历段落中的每个样式块
    for run in para.runs:
        # TODO 使用if语句判断当前样式块是否加粗或有下划线
        if run.bold or run.underline:
            # TODO 如果是，获取该重点单词的中文释义，也就是本段落中的第一个样式块的文本内容
            # 并赋值给变量correctAnswer

            correctAnswer = para.runs[0].text
            # TODO 使用append()函数将变量correctAnswer添加到correctList列表中
            correctList.append(correctAnswer)

        # TODO 使用openpyxl.load_workbook()函数打开默写完成后的单词表，并赋值给变量wb=
wb = openpyxl.load_workbook(r"C:\Users\Administrator\PycharmProjects\pythonProject\读取word存进excel\tingting\重点单词.xlsx")

# TODO 将 数学 工作表赋值给变量sheet
sheet = wb["数学"]

# TODO 使用for循环和enumerate()函数
# 遍历存放了单词中文意思的列表correctList的同时
# 生成一个从1开始的索引index

for index, word in enumerate(correctList, 1):
    # TODO 使用if语句判断B列数据与正确答案不一致时
    if sheet[f"B{index}"].value != word:
        # TODO 若不一致，则将正确的中文意思添加到第C列中
        sheet[f"C{index}"].value = word

# TODO 使用save()函数将单词表保存到指定路径 /Users/tingting/重点单词.xlsx
wb.save(r"C:\Users\Administrator\PycharmProjects\pythonProject\读取word存进excel\tingting\重点单词.xlsx")
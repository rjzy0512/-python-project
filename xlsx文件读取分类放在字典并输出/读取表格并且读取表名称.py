# TODO 使用import导入openpyxl
import openpyxl

# TODO 将汇总工作簿路径 "/Users/yequ/data/汇总.xlsx" 赋值给path
path = "/Users/yequ/data/汇总.xlsx"

# TODO 使用 openpyxl.load_workbook() 打开工作簿赋值给wb

wb = openpyxl.load_workbook(path)
# TODO 将 "口香糖" 工作表赋值给gum

gum = wb["口香糖"]
# TODO 使用for循环遍历工作簿对象的 .worksheets属性

for sheet in wb.worksheets:
    # TODO 使用if语句判断工作表的 .title属性获得的工作表名称 等于"口香糖"时就跳过
    if sheet.title == "口香糖":
        continue

    # TODO 使用for循环遍历工作表的 .rows属性
    for row in sheet.rows:

        # TODO 取第1列商品名称的值，赋值给productName
        productName = row[0].value

        # TODO 使用if语句判断“口香糖”字符在商品名称中时
        if "口香糖" in productName:

            # TODO 定义一个用于存储整行商品信息的空列表orderContent
            orderContent = []

            # TODO 使用for循环遍历该行rowData中的单元格

            for cell in row:
                # TODO 将每一个元素的值追加到列表orderContent中
                orderContent.append(cell.value)

            # TODO 循环结束后，使用 .title属性 获取工作表的名称追加到列表orderContent中
            orderContent.append(sheet.title)

            # TODO 利用append()函数将整行商品信息追加到gum工作表中
            gum.append(orderContent)

# TODO 使用save()函数保存工作簿到原路径path
wb.save(path)
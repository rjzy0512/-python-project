# 打开提示.xlsx工作簿
wb = openpyxl.load_workbook("提示.xlsx")

# 将案例工作表赋值给sheet
sheet = wb["案例"]

# 使用for循环遍历工作表的 .rows属性
for rowData in sheet.rows:

# 定义存储该行数据的空列表rowValues
rowValues = []

# 使用for循环遍历rowData的单元格
for cell in rowData:

    # 将单元格的值追加到列表中
rowValues.append(cell.value)
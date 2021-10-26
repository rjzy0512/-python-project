# 挑战自己吧
# 挑战自己吧
import openpyxl
import os
import shutil


# 获取地址
url = r"C:\Users\Administrator\PycharmProjects\pythonProject\学生资料"
allItems = os.listdir(url)
# 获取xlse中地区信息
wb = openpyxl.load_workbook("学生地区.xlsx", data_only=True)
ws = wb["地区表"]
diqu = []
for rows in ws.rows:
    shengfen = rows[1].value
    diqu.append(shengfen)
diqu.pop(0)
mingzi = []
for rows in ws.rows:
    xingming = rows[0].value
    mingzi.append(xingming)
mingzi.pop(0)

for shu in range(0,312):
    xindiqu = os.path.join(url, diqu[shu])
    new_diqu = os.path.join(xindiqu,mingzi[shu]+'.docx')
    if not os.path.exists(xindiqu):
        os.mkdir(xindiqu)

    print(new_diqu)
#拼接地址  new_diqu
    yidongqiandizhi=os.path.join(url,mingzi[shu]+'.docx')
    shutil.move(yidongqiandizhi,new_diqu)


#优秀
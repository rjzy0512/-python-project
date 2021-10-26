# 使用import导入ezexif模块
import ezexif

# 使用import导入os模块
import os

# 使用import导入openpyxl模块
import openpyxl

# 读取照片所在的文件夹路径"/Users/Desktop/photo"，赋值给变量photoPathList
photoPathList = "/Users/Desktop/photo"

# TODO 获取文件夹下的所有照片列表，赋值给变量photoList
photoList=os.listdir(photoPathList)

# TODO 读取路径为"/Users/Desktop/照片参数.xlsx"的Excel文档，赋值给变量wb

wb=openpyxl.load_workbook("/Users/Desktop/照片参数.xlsx")
# TODO 读取工作表"示例"
ws=wb["示例"]

# 将需要填写的标题，组成一个列表titleList
titleList = ["file_name","Image ExifOffset","EXIF ExposureProgram","EXIF DateTimeOriginal","EXIF MeteringMode","EXIF Flash","EXIF ExposureMode"]

# TODO 遍历photoList下的照片文件
for photo in photoList:

    # TODO 使用os.path.join()函数，将变量photoPathList，photo组合得到photoPath=o
    photoPath=os.path.join(photoPathList,photo )

    # TODO 获取exif信息并赋值给变量exifInfo
    exifInfo=ezexif.process_file(photoPath)

    # TODO 在字典exifInfo中，添加一个键file_name，它的值是变量photo
    exifInfo["file_name"]=photo

    # 定义一个空列表rowData
    rowData = []

    # TODO 使用for循环，遍历列表titleList的所有元素，给变量key
    for key in titleList:

        # TODO 找到字典exifInfo中key对应的值，使用append()函数加入列表rowData.
        rowData.append(exifInfo[key])

    # TODO 将列表rowData，使用append()函数，添加到工作表ws中
    ws.append(rowData)

# TODO 将工作簿保存路径为"/Users/Desktop/照片参数-新.xlsx"的Excel文档
wb.save("/Users/Desktop/照片参数-新.xlsx")
# 如果运行成功，输出"success"
print("success")
# TODO 使用import导入os模块

import os
# TODO使用import导入shutil模块
import shutil

# TODO 将文件夹路径 /Users/yequ/不合格 赋值给变量unqualifiedPath
unqualifiedPath = "/Users/yequ/不合格"

# TODO 将报名表的路径 /Users/yequ/Downloads/registration 赋值给变量allFormPath
allFormPath = "/Users/yequ/Downloads/registration"

# TODO 使用os.listdir()函数获取该路径下所有报名表，并赋值给变量allItems
allItems = os.listdir(allFormPath)

# TODO 使用print输出现在报名表的数量，也就是变量allItems的长度
print(len(allItems))

# TODO 使用for循环逐个遍历所有报名表
for item in allItems:

    # TODO 使用os.path.splitext()函数获取文件名的前半段，并赋值给变量fileName
    fileName = os.path.splitext(item)[0]

    # TODO 使用split()函数以"-"分隔文件名，并赋值给变量result=
    result = fileName.split("-")

    # TODO 使用os.path.join()函数合并报名表路径，并赋值给变量path
    path = os.path.join(allFormPath, item)

    # TODO 使用if语句判断列表result的长度是否不等于3
    if len(result) != 3:

        # TODO 若长度不符合，使用shutil.move()函数移动该报名表到指定文件夹中
        shutil.move(path, unqualifiedPath)

    # 判断列表中第二个元素【意愿科目】是否不属于可竞选科目
    elif result[1] not in ["语文", "数学", "英语", "体育", "音乐", "安全教育", "美术"]:
        # 若不属于，使用shutil.move()函数移动该报名表到指定文件夹中
        shutil.move(path, unqualifiedPath)

    # TODO 判断列表中第三个元素【意愿年级】是否不属于可竞选年级
    elif result[2] not in ["一年级", "二年级", "三年级", "四年级", "五年级", "六年级"]:

        # TODO 若不属于，使用shutil.move()函数移动该报名表到指定文件夹中
        shutil.move(path, unqualifiedPath)

# TODO 使用os.listdir()函数重新获取allFormPath路径下所有报名表，并赋值给变量allItemsAfter
allItemsAfter = os.listdir(allFormPath)

# TODO 使用print输出现在报名表的数量，也就是变量allItemsAfter的长度
print(len(allItemsAfter))
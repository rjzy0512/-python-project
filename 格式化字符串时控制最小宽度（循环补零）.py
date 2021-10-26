#格式化字符串时控制最小宽度
# 姓名列表
nameList = ["Joe", "Tony", "Kevin"]
# 编号列表
idList = [8, 231, 92]

# 遍历0~2的数字，逐个访问列表中的元素
for index in range(3):
    # TODO 格式化输出姓名和编号，姓名控制最小宽度为5，编号最小宽度为3并补0
    print(f"{nameList[index]:5} - {idList[index]:03}")
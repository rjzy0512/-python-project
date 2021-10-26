score = {"数学":121, "语文": 141, "英语": 132, "物理": 90}

# 使用get()函数访问存在的键
print(score.get("英语"))

# 使用get()函数访问不存在的键
print(score.get("地理"))

# 使用get()函数访问不存在的键，指定第二个参数为0
print(score.get("历史", 0))

# 使用get()函数访问存在的键，第二个参数会被忽略
print(score.get("数学", 0))
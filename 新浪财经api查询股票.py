# 使用import导入requests
import requests

# TODO 定义get_detail()函数用于获取股票信息，传入参数code
def get_detail(code):
    # 使用"http://hq.sinajs.cn/list="与股票代码进行拼接，赋值给url
    url = "http://hq.sinajs.cn/list=" + code
    # 使用requests模块获取数据，赋值给res
    res = requests.get(url)
    # 将服务器响应内容转换为字符串形式，赋值给html
    html = res.text

    # TODO 用split()以=进行分割，分割后取第二个元素赋值给content
    content=html.split("=")[1]
    # TODO 使用strip()去掉空格，赋值给content
    content=content.strip()
    # TODO 使用lstrip()去掉左侧的"，赋值给content
    content=content.lstrip('"')
    # TODO 使用rstrip()去掉右侧的";，赋值给content
    content=content.rstrip('";')
    # TODO 用split()以,进行分割，分割后赋值给details
    details=content.split(",")

    # TODO 使用return返回details
    return details

# 定义一个列表，列表中是要查询的股票代码
stock =[ "s_sh600390", "s_sh600621", "s_sh000001", "s_sh000300", "s_sz399005", "s_sz399006", "s_sh600004", "s_sh603160", "s_sh601238", "s_sh600028", "s_sh600745", "s_sh601668"]

# TODO 使用for循环遍历stock列表 ，遍历的变量设为code
for code in stock:
    # TODO 调用get_detail()，传入code参数，赋值给result
    result=get_detail(code)
    # TODO 使用格式化输出 名称{result[0]}: 收盘价{result[1]}, 涨跌额{result[2]}, 涨跌幅{result[3]}, 成交量{result[4]}, 成交额{result[5]}
    print(f"名称{result[0]}: 收盘价{result[1]}, 涨跌额{result[2]}, 涨跌幅{result[3]}, 成交量{result[4]}")
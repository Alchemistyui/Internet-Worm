import re


# 正则表达式由字符和操作符构成
# . 单个字符， []字符集，单个字符取值范围，[^]非字符集， * 前一个字符0次或无限次扩展
# + 前一个字符0次或无限次扩展， ？ 前一个字符0次或1次扩展， |左右表达式任选一个
# {m} 扩展前面的字符m次，{m，n} 扩展m至n次， ^ 匹配开头， $匹配结尾， () 分组，里面只能用 |
# \d 数字0-9， \w 字符，包含大小写数字

# 函数式用法
match = re.search(r'[1-9]\d{5}', 'BIT 100081')
if match:
    print(match.group(0))

# search方法是匹配整个字符串，match是从开始位置匹配

# 面向对象用法，优点在于只用一次编译
# 将字符串编译为正则表达式对象
pat = re.compile(r'[1-9]\d{5}')
rst = pat.search('BIT 100081')

# search，match等返回的结果为match对象，属性string原文本，re正则表达式，
# pos搜索文本开始位置，endpos结束位置，方法group(0)匹配后字符串,start()匹配字符串在源字符串开始位置,
# end(),span()返回（star(),end())的元组



# re库默认采用贪婪匹配，即匹配符合的最长字符串
match = re.search(r'PY.*N','PYANBNCNDN')
print(match.group(0))

# 最小匹配，对*，+， ？，{m，n}操作符后面加上？
match = re.search(r'PY.*？N','PYANBNCNDN')






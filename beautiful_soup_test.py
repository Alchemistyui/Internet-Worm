import requests
from bs4 import BeautifulSoup
# 引入正则表达式
import re



r = requests.get("https://python123.io/ws/demo.html")

demo = r.text

# 解析demo的HTML解释器
soup = BeautifulSoup(demo, "html.parser")

# 使HTML变得更加友好（增加换行符），标签也可使用
print(soup.prettify())

print(soup.title)

# 若文档中存在多个同类标签，soup.tag只返回第一个标签
print(soup.a)

soup.a.name

# 父标签名字
soup.a.parent.name

# 标签的属性
soup.a.attrs
# 属性字典中的属性的值
soup.a.attrs['class']

type(soup.a)

# 标签中的值，可跨越标签层次，如p中的b
print(soup.a.string)
# 判断文本是否是注释通过type进行判断

# 下行遍历
soup.head.contents
soup.body.contents[1]

for child in soup.body.children:
    print(child)


# 上行遍历parent，parents
soup.title.parent

for parent in soup.a.parents:
    # 一定要判断，因为soup对象没有父节点
    if parent is None:
        print(parent)
    else:
        print(parent.name)

# 平行遍历建立在同一个父亲结点下,平行结点获得的可能是string类型而不是标签
soup.a.next_sibling
soup.a.previous_sibling
# 加s也可获取所有结点从而进行遍历


# 信息查找与提取
# find_all: 参数：1.检索参数的名字，可为['a', 'b']， 2.属性值检索(字符信息)
# 3.是否默认搜索子孙结点，为false则只搜索儿子， 4.对标签中间的字符串区域进行检索
for link in soup.find_all('a'):
    print(link.get('herf'))


# 查找以b开头的（正则表达式：给出部分进行搜索）
for tag in soup.find_all(re.compile('b')):
    print(tag.name)


soup.find_all('p', 'course')
soup.find_all(id = 'link1')
soup.find_all(string = 'Basic Python')
# a() = a.find_all()



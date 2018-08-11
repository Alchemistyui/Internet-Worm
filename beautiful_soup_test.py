import requests
from bs4 import BeautifulSoup


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











#用户：xiangjianqun   

#日期：2018-12-25   

#时间：10:23   

#文件名称：PyCharm

import sys

sys.path.append("/Users/xiangjianqun/PycharmProjects/untitled/learning/test/test1")

import time
x=time.localtime()
print(time.strftime("%Y-%m:%d %H:%M:%S",x)) #格式化的字符串

import hashlib
m=hashlib.md5()
m.update(b'hello python')
m.update(b"hello")
print(m.hexdigest())


import re
s1="sdftpg23p"
p1=re.search('^[a-z]+', s1)
p2=re.match('^[a-z]+', s1).group()
#group() 返回被 RE 匹配的字符串
#start() 返回匹配开始的位置,end() 返回匹配结束的位置,span() 返回一个元组包含匹配 (开始,结束) 的位置
#match和search一旦匹配成功，就是一个match object对象
print(p1)
print(p2)
w = re.findall('\btina','tian tinaaaa')
#返回[]
print(w)
s = re.findall(r'\btina','tian tinaaaa')
#返回['tina']
print(s)

a = "123abc456"
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0))   #123abc456,返回整体
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1))   #123
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2))   #abc
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3))   #456
#group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。

tt = "Tina is a good girl, she is cool, clever, and so on..."
rr = re.compile(r'\w*oo\w*')
print(rr.findall(tt))
print(re.findall(r'(\w)*oo(\w)',tt))#()表示子表达式

#匹配电话号码
p = re.compile(r'\d{3}-\d{6}')
print(p.findall('010-628888'))
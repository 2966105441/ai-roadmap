#写法一：整个搬进来，用的时候加前缀
import tools
print(tools.greet("小红"))
print(tools.add(3,4))

#写法2：只拿一个函数出来，不用加前缀
from tools import greet
print(greet("小红"))

#写法3：整个搬进来，但换个短代号
import tools as t
print(t.greet("小红"))

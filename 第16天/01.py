import os
os.environ["NO_PROXY"] = "127.0.0.1,localhost"

import requests

r = requests.get("http://127.0.0.1:8000/hello",timeout=5)

print("状态码：",r.status_code)
print("类型：",type(r))
print("内容：",r.text)
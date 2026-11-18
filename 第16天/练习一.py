import os
os.environ["NO_PROXY"] = "127.0.0.1,localhost"

import requests

r = requests.get("http://127.0.0.1:8000/hello", timeout=5)
print("r.encoding =", r.encoding)
print("r.apparent_encoding =", r.apparent_encoding)
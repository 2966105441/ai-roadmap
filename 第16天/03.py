import os
os.environ["NO_PROXY"] = "127.0.0.1,localhost"

import requests

for path in ["/hello", "/nope"]:
    r = requests.get("http://127.0.0.1:8000" + path, timeout=5)
    print(f"{path:<10} -> {r.status_code} {r.reason}")

try:
    requests.get("http://127.0.0.1:8000/nope", timeout=5).raise_for_status()
except requests.exceptions.HTTPError as e:
    print("抓到：", e)
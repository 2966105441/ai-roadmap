import os
os.environ["NO_PROXY"] = "127.0.0.1,localhost"

import requests

r = requests.get("http://127.0.0.1:8000/stats.json", timeout=5)
top = r.json()["top"]

print(" / ".join(f'{d["word"]}×{d["count"]}' for d in top))

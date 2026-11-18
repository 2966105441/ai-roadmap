"""05.py —— 用 config 里的地址去请求，代码里没有一个写死的值"""
import requests

import config
print("模型 =", config.MODEL)
print("地址 =", config.BASE_URL)
r = requests.get(config.BASE_URL + "/hello", timeout=config.TIMEOUT)
print("状态码 =", r.status_code)
print("内容 =", r.json())


"""01.py —— 手动校验：四个字段，写了十行，还只报第一个问题"""
data = {"model": "fake-mimo", "temperature": "0.3", "timeout": "5s", "debug": "0"}

model = data.get("model")
if not model:
    raise SystemExit("缺少 model")

temperature = float(data["temperature"])      # 值不是数字就崩在这
try:
    timeout = int(data["timeout"])
except ValueError:
    raise SystemExit("timeout 不是整数：" + repr(data["timeout"]))

debug = data["debug"] in ("1", "true", "yes", "on")
print(model, temperature, timeout, debug)

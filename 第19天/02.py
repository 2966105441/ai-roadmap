"""02.py —— 同样的数据交给 pydantic，三个类型全自动转好"""
from pydantic import BaseModel


class Settings(BaseModel):
    model: str
    temperature: float
    timeout: int
    debug: bool


s = Settings(model="fake-mimo", temperature="0.3", timeout="5", debug="0")
print(s)
print("类型 =", type(s.temperature).__name__, type(s.timeout).__name__, type(s.debug).__name__)
print("temperature + 1 =", s.temperature + 1)
print("debug =", s.debug, "  |  但 bool('0') =", bool("0"))

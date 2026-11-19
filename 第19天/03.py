"""03.py —— 数据真有问题时，它一次把问题全说完"""
from pydantic import BaseModel, ValidationError


class Settings(BaseModel):
    model: str
    temperature: float
    timeout: int


坏数据 = {"temperature": "5s", "timeout": "abc"}

try:
    Settings(**坏数据)
except ValidationError as e:
    print(e)
    print("一共", e.error_count(), "条")

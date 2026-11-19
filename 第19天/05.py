"""05.py —— 用 pydantic 重写第 17 天的 config.py"""
import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class Settings(BaseModel):
    base_url: str
    api_key: str
    model: str = "fake-mimo"
    temperature: float = Field(default=0.7, ge=0, le=2)
    timeout: float = 10.0


s = Settings(base_url=os.getenv("LLM_BASE_URL"), api_key=os.getenv("LLM_API_KEY"),
             model=os.getenv("LLM_MODEL"), temperature=os.getenv("LLM_TEMPERATURE"),
             timeout=os.getenv("LLM_TIMEOUT"))

print("base_url =", s.base_url, "| model =", s.model)
print("temperature =", s.temperature, type(s.temperature).__name__)
print("timeout =", s.timeout, type(s.timeout).__name__)
print("key =", s.api_key[:5] + "******")




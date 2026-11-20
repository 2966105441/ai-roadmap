"""config.py —— 所有配置只在这里读一次，进门先校验"""
import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class Settings(BaseModel):
    model: str = "fake-mimo"
    api_key: str
    temperature: float = Field(default=0.7, ge=0, le=2)
    top: int = Field(default=3, ge=1)


def get_settings() -> Settings:
    """从环境变量读一遍，返回一个已经校验过的配置对象"""
    return Settings(
        model=os.getenv("LLM_MODEL", "fake-mimo"),
        api_key=os.getenv("LLM_API_KEY"),
        temperature=os.getenv("LLM_TEMPERATURE", "0.7"),
        top=os.getenv("APP_TOP", "3"),
    )

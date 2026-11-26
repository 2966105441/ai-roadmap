# ai-roadmap

从零开始学 Python 的每日记录。目标：**2027 年暑期拿到 AI 大模型开发实习**。

这个仓库不是教程，是我的练习本。每天一个目录，踩过的坑都留在里面。

---

## 先看这个：`llm-chat/`

一个**不用联网、不用 API Key** 就能跑的 AI 对话客户端。前面 30 天学的东西全焊在这里。

```bash
git clone git@github.com:2966105441/ai-roadmap.git
cd ai-roadmap/llm-chat
pip install -r requirements.txt
```

然后开两个终端：

```bash
# 终端 1：启动本地假接口（这个窗口别关）
python fake_server.py

# 终端 2：开始聊天
python main.py
```

它做到的事：

| 能力 | 怎么做到的 |
| --- | --- |
| 多轮对话 | 模型没有记忆，每轮把**全量历史**重发一遍 |
| 流式输出 | `stream=True` + `iter_lines`，字到了就打，首字延迟从 1.4 秒降到 0.05 秒 |
| 会话存档 | 每轮写完就落盘，换 `--session` 就是另一段对话 |
| 自动截断 | 超过 7 条删最早的一问一答，`system` 永远保住 |
| 温度可调 | 0 = 每次答案一样，2 = 每次都不一样 |

聊天时可以敲 `/quit` `/clear` `/len` `/temp 1.5`。

细节和每个文件的分工见 [`llm-chat/README.md`](llm-chat/README.md)。

---

## 目录

| 目录 | 内容 |
| --- | --- |
| **`llm-chat/`** | **能跑的东西都在这**：聊天客户端 + 本地假接口 + 说明 |
| `第三天/` ~ `第七天/` | Python 基础：字符串、列表、字典、循环、函数、文件读写 |
| `第八天/` `第九天/` | 类与对象、`__init__` / `self`、异常处理、`with` |
| `第十天/` `第十一天/` | 模块与包、`pip`、jieba 分词、JSON 读写、配置分离 |
| `第14天/` | CSV 读写、把数据读成对象 |
| `第15天/` | 类型注解 `typing`、把大文件拆成多个模块 |
| `第16天/` | `requests` 与 HTTP、`status_code`、异常分类 |
| `第17天/` | `.env` 读配置、`python-dotenv` |
| `第18天/` | `logging` 日志、写文件、按级别过滤 |
| `第19天/` | `pydantic` 数据校验 |
| `第20天/` | `argparse` 命令行参数 |
| `第21天/` | 入口脚本：`config.py` + `main.py`，`if __name__ == "__main__"` |
| `第22天/` ~ `第30天/` | 大模型接口：裸调 → 多轮 → 落盘 → 类 → CLI → 斜杠命令 → 流式 → 截断 → 温度 |
| `data/` | 练习用小语料（中英文各一份 + 停用词表） |
| `notes/` | 每周复盘 |

## 怎么跑单个练习

每个目录里的脚本都是独立的，大部分直接在目录内跑：

```bash
cd 第30天
python 01.py
```

`第22天` 之后的脚本要先启动假接口（`llm-chat/fake_server.py` 或 `第16天/fake_api.py`），
否则会报 `ConnectionError [WinError 10061]` —— 那不是代码错，是服务没开。

## 进度

- [x] 第 1–2 周：语法、数据结构、函数、文件、面向对象、异常、Git
- [x] 第 3 周：CSV、类型注解、requests、配置、日志、校验、命令行
- [x] 第 4–5 周：大模型客户端（多轮 / 流式 / 截断 / 温度）
- [ ] 第 6 周：Prompt 工程

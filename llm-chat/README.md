# llm-chat

一个**不用联网、不用 API Key** 就能跑的 AI 对话客户端。

它在本地起一个假接口，模仿大模型的返回格式（`choices[0].message.content`），
所以你不用注册任何平台就能把「多轮对话 / 流式 / 截断 / 温度」全部跑一遍。

## 怎么跑

需要 Python 3.10 以上。

```bash
pip install -r requirements.txt
```

然后开**两个**终端：

```bash
# 终端 1：启动假接口（这个窗口别关，关了聊天就报错）
python fake_server.py

# 终端 2：开始聊天
python main.py
```

看到 `你：` 就可以打字了。

## 会看到什么

```
（会话 chat｜角色 tutor｜温度 0.7｜流式）

你：你好
它：你这次发了 2 条消息，最后一句是「你好」。这个我懂。
你：再说一句
它：你这次发了 4 条消息，最后一句是「再说一句」。嗯……让我想想。
```

「发了 N 条消息」是假接口故意报给你的，用它能看到历史在涨：
**2 → 4 → 6 → 6 → 6**，到 7 条就不再涨了（自动截断生效）。

> 结尾那半句是按温度抽出来的，你跑出来不会和上面一样 —— 这正是 Day 30 讲的东西。

## 命令

聊天时可以直接敲：

| 命令 | 作用 |
| --- | --- |
| `/quit` | 退出 |
| `/clear` | 清空这次会话（`system` 那句保留） |
| `/len` | 看本地存了几条 |
| `/temp 1.5` | 当场改温度 |

启动参数：

| 参数 | 作用 |
| --- | --- |
| `--role tutor` | 用 `prompts/` 里哪个文件当 system prompt。可选 `tutor` / `reviewer` / `vague` |
| `--temp 0.7` | 温度。0 = 每次答案一样，2 = 每次都不一样 |
| `--session work` | 会话名，存档成 `work.json`。不写就是 `chat.json` |
| `--plain` | 不用流式，等整句回来再打 |

## 几个文件

| 文件 | 干什么 |
| --- | --- |
| `main.py` | 命令行入口：解析参数、读 system prompt、`while` 循环读输入、把 `/` 开头的命令拦下来 |
| `client.py` | `ChatSession` 类：管历史、管存档、自动截断、带温度发请求；末尾的 `parse_json()` / `extract()` 负责把模型吐的 JSON 洗干净 |
| `fake_server.py` | 本地假接口。聊天只用 `/chat` 和 `/chat_stream`，`/extract` 用来演示「让模型输出结构化数据」 |
| `prompts/` | 一个文件一个角色。`tutor.txt` 只答 Python 问题，`reviewer.txt` 只挑代码毛病，`vague.txt` 是空白对照 |
| `01.py` | 实验脚本：同一个问题、两个 system prompt，各问一次看差别 |
| `02.py` | 实验脚本：连抽三次，看模型怎么用 `` ```json `` 和开场白把 `json.loads` 弄炸 |
| `03.py` | 一句话变一条数据，攒成 `notes.json` |

## 限制

- 假接口的回复是模板，**不是真模型**。它只会告诉你「你发了几条消息」+ 按温度抽一句话
- `/extract` 的「抽取」是查关键词表（`明天`/`下周` → 日期），不是真理解。但它会**故意**轮流用三种格式回你：干净、套 ```` ```json ````、带开场白——真模型也这样，`parse_json()` 就是为这个写的
- 要接真模型：把 `client.py` 顶上那两行 `URL` 换成真地址，请求头加 `Authorization: Bearer <你的 Key>`，再删掉 `os.environ["NO_PROXY"]` 那一行
- 历史存成 JSON 文件，扛不住并发。真产品用数据库

## 学到的东西都在这

这 11 个文件不是一次写成的，是 Day 22 到 Day 33 一天加一块拼出来的：

| 天 | 加了什么 |
| --- | --- |
| Day 22 | `requests.post` 裸调接口，取 `choices[0].message.content` |
| Day 23 | 多轮对话：模型无状态，每轮重发全量 `messages` |
| Day 24 | 会话落盘：`json.dump(ensure_ascii=False)`，每轮都写 |
| Day 25 | 用类管状态：`self.history` 一个对象一份 |
| Day 26 | 焊成 CLI：`while` + `input()` + `--session` |
| Day 27 | 斜杠命令：`/` 开头的在 `send()` 之前拦下，不进历史 |
| Day 28 | 流式：`stream=True` + `iter_lines`，首字延迟 1.4s → 0.05s |
| Day 29 | 自动截断：超 7 条删最早的一问一答，`system` 永不动 |
| Day 30 | 温度：`exp(分/温度)` 再按权重抽签 |
| Day 31 | 收进一个仓库：改名、写 README、写 `requirements.txt` |
| Day 32 | system prompt 搬进文件，`--role` 切角色 |
| Day 33 | 让模型吐 JSON：`parse_json()` 切出 `{` 到 `}` 之间那段，`extract()` 一句话变一条待办 |

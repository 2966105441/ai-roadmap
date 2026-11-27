"""fake_server.py —— 本地假接口，模仿大模型 API 的返回格式

不需要联网，不需要 API Key。先跑这个，再另开终端跑 main.py。
聊天只用到 /chat 和 /chat_stream 两个端点；
/hello /stats.json /slow /flaky 是早期练 requests 时加的，留着不影响。
system 里写了「只回答包含以下关键词的问题：」就会按关键词拒答（Day 032 加的）。
"""
import json
import math
import random
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = 8000
flaky_n = {"n": 0}          # /flaky 被请求了几次

# 回复的结尾可以从这五个里挑，分数是「模型」给它们打的分（Day 030 加的）
PHRASES = ["这个我懂。", "嗯……让我想想。", "不太确定，但我觉得能行。", "别问了，先动手。"]
PHRASE_LOGITS = [3.0, 2.0, 1.2, 0.6]


def pick_phrase(temperature):
    """按温度从候选结尾里抽一个：温度低就总挑分最高的，温度高就谁都可能"""
    t = float(temperature)
    if t <= 0.05:                                   # 温度趋近 0：直接拿最高分
        return PHRASES[PHRASE_LOGITS.index(max(PHRASE_LOGITS))]
    exps = [math.exp(x / t) for x in PHRASE_LOGITS]  # 温度越小，分差被放大得越狠
    return random.choices(PHRASES, weights=exps)[0]

SCOPE_KEY = "只回答包含以下关键词的问题："     # system 里写了这行，就按关键词判断

WRAP_N = {"n": 0}          # /extract 被请求了几次，用来轮流模拟模型的三种坏习惯


def guess_due(text):
    """假接口版的「抽取」：认出几个词就给日期，认不出就说待定（Day 033 加的）"""
    for key, due in [("明天", "2026-11-28"), ("下周", "2026-12-04")]:
        if key in text:
            return due
    return "待定"



def read_system(msgs):
    """取第一条 system 的内容，没有就返回空串"""
    for m in msgs:
        if m.get("role") == "system":
            return m.get("content", "")
    return ""


def out_of_scope(msgs, text):
    """system 写了关键词约束、而这句话一个都没命中 → 该拒答（Day 032 加的）"""
    system = read_system(msgs)
    if SCOPE_KEY not in system:
        return False                                # 没写这条约束就不管
    line = system.split(SCOPE_KEY, 1)[1].split("\n", 1)[0]
    words = [w.strip() for w in line.replace("、", ",").split(",") if w.strip()]
    return not any(w.lower() in text.lower() for w in words)

# 这份数据就是你 Day 011 / Day 015 真跑出来的结果，不是编的
STATS = {
    "source": "sample_zh.txt",
    "total": 82,
    "distinct": 55,
    "top": [
        {"word": "检索", "count": 6},
        {"word": "质量", "count": 6},
        {"word": "回答", "count": 4},
        {"word": "文档", "count": 4},
    ],
}


class Handler(BaseHTTPRequestHandler):

    def _send(self, code, payload):
        """统一的出口：把字典变成 JSON 字节，附带状态码发回去"""
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        print(f"  <- GET  {self.path}", flush=True)

        if self.path == "/stats.json":
            self._send(200, STATS)

        elif self.path == "/hello":
            self._send(200, {"msg": "你好，requests"})

        elif self.path == "/slow":
            time.sleep(3)                       # 故意拖 3 秒，用来练 timeout
            self._send(200, {"msg": "我睡了 3 秒才回你"})

        elif self.path == "/flaky":
            flaky_n["n"] += 1
            n = flaky_n["n"]
            if n % 3 == 0:                      # 每第 3 次才成功
                self._send(200, {"msg": "这次成功了", "第几次": n})
            else:
                self._send(500, {"error": "服务器临时抽风", "第几次": n})

        else:
            self._send(404, {"error": "没有这个地址", "path": self.path})

    def _stream(self, text):
        """流式出口：不算总长度，写完一句立刻发一句（Day 028 加的）"""
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.end_headers()
        for ch in text:                         # 一个字发一次
            chunk = {"id": "chat-001",
                     "choices": [{"index": 0, "delta": {"content": ch}}]}
            self.wfile.write(("data: " + json.dumps(chunk, ensure_ascii=False) + "\n\n").encode("utf-8"))
            self.wfile.flush()                  # 不 flush 就攒着不出去
            time.sleep(0.05)
        self.wfile.write(b"data: [DONE]\n\n")
        self.wfile.flush()

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length).decode("utf-8")
        print(f"  <- POST {self.path}   收到：{raw}", flush=True)

        if self.path == "/chat_stream":
            data = json.loads(raw or "{}")
            msgs = data.get("messages") or [{"role": "user", "content": data.get("prompt", "")}]
            last = ""
            for m in msgs:
                if m.get("role") == "user":
                    last = m.get("content", "")
            phrase = pick_phrase(data.get("temperature", 0.7))
            tail = "这个问题不在我能回答的范围内。" if out_of_scope(msgs, last) else phrase
            self._stream(f"你这次发了 {len(msgs)} 条消息，最后一句是「{last}」。{tail}")

        elif self.path == "/extract":
            data = json.loads(raw or "{}")
            text = data.get("text", "")
            item = {"title": text, "due": guess_due(text), "done": False}
            body = json.dumps(item, ensure_ascii=False)
            WRAP_N["n"] += 1
            pre = ["好的，我提取到：\n", "", "```json\n"][WRAP_N["n"] % 3]   # 开场白 / 干净 / 代码块
            content = pre + body + ("```" if "```" in pre else "")
            self._send(200, {
                "id": "chat-002",
                "model": "fake-mimo",
                "choices": [{"index": 0,
                             "message": {"role": "assistant", "content": content},
                             "finish_reason": "stop"}],
            })

        elif self.path == "/chat":
            data = json.loads(raw or "{}")
            phrase = pick_phrase(data.get("temperature", 0.7))
            msgs = data.get("messages")         # 新版请求：一串带角色的消息
            if msgs:
                last = ""
                for m in msgs:                  # 取最后一条 user 说的话
                    if m.get("role") == "user":
                        last = m.get("content", "")
                chars = sum(len(m.get("content", "")) for m in msgs)
                tail = "这个问题不在我能回答的范围内。" if out_of_scope(msgs, last) else phrase
                reply = f"你这次发了 {len(msgs)} 条消息，最后一句是「{last}」。{tail}"
            else:                               # 老版请求：只有一个 prompt
                last = data.get("prompt", "")
                chars = len(last)
                reply = f"你问的是「{last}」。{phrase}"
            self._send(200, {
                "id": "chat-001",
                "model": "fake-mimo",
                "choices": [{
                    "index": 0,
                    "message": {"role": "assistant", "content": reply},
                    "finish_reason": "stop",
                }],
                "usage": {"prompt_tokens": chars,
                          "completion_tokens": 12,
                          "total_tokens": chars + 12},
            })
        else:
            self._send(404, {"error": "没有这个地址"})

    def log_message(self, *args):
        pass                                    # 关掉默认日志，上面自己打印


print(f"假接口已启动： http://127.0.0.1:{PORT}")
print("这个窗口不会结束，是正常的 —— 它在等你来请求。要停就点红色方块。")
ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()

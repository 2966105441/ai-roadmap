"""fake_api.py —— 本地假接口服务器，只为练 requests 用

它不联网、不需要安装任何东西。
先运行这个文件，它会在你电脑上开一个「网站」，然后你再运行别的脚本去请求它。
"""
import json
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = 8000
flaky_n = {"n": 0}          # /flaky 被请求了几次

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

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length).decode("utf-8")
        print(f"  <- POST {self.path}   收到：{raw}", flush=True)

        if self.path == "/chat":
            data = json.loads(raw or "{}")
            msgs = data.get("messages")         # 新版请求：一串带角色的消息
            if msgs:
                last = ""
                for m in msgs:                  # 取最后一条 user 说的话
                    if m.get("role") == "user":
                        last = m.get("content", "")
                chars = sum(len(m.get("content", "")) for m in msgs)
                reply = f"你这次发了 {len(msgs)} 条消息，最后一句是「{last}」。"
            else:                               # 老版请求：只有一个 prompt
                last = data.get("prompt", "")
                chars = len(last)
                reply = f"你问的是「{last}」。"
            self._send(200, {
                "id": "chat-001",
                "model": "fake-mimo",
                "choices": [{
                    "index": 0,
                    "message": {"role": "assistant",
                                "content": reply + "这是一条假回复。"},
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

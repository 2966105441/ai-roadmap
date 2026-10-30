messages = [
    {"role":"system","content":"你是一个助手"},
    {"role":"user","content":"你好"},
    {"role":"assistant","content":"你好，请问有什么可以帮您"}
]

print("共",len(messages),"条消息")
print("最后一条说话的是：",messages[-1]["role"])
print("内容是：",messages[-1]["content"])


print("--- 全部展开 ---")

for m in messages:
    print(f"[{m["role"]}]{m["content"]}")
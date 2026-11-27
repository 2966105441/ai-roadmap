path = "D:/code/ai-roadmap/llm-chat/client.py"
parts = path.split("/")
print(parts[-1])
print(parts[-1].rsplit(".",1)[1])
print("/".join(parts[:-1])) 
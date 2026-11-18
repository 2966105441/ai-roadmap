"""01.py —— 环境变量是啥？你电脑上早就有一堆了"""
import os

print("现在系统里一共有", len(os.environ), "个环境变量")
print("（这个数字每次可能不一样，不用管）")

print("\n随便看两个：")
print("  用户名 =", os.environ.get("USERNAME"))
print("  电脑名 =", os.environ.get("COMPUTERNAME"))

print("\n取一个不存在的名字，不会报错，只给你 None：")
print("  os.environ.get('瞎写的') =", os.environ.get("瞎写的"))

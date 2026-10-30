"""开发环境自检脚本

用法：在 PyCharm 里右键 Run，或在终端执行 python check_env.py
如果全部显示正常，说明你的环境配置对了。
"""

import sys
import platform

print("=" * 42)
print("        开发环境自检")
print("=" * 42)

print(f"Python 版本     ：{sys.version.split()[0]}")
print(f"解释器路径      ：{sys.executable}")
print(f"操作系统        ：{platform.system()} {platform.release()}")

in_venv = sys.prefix != sys.base_prefix
print(f"是否在虚拟环境  ：{'是' if in_venv else '否'}")

print("-" * 42)

if in_venv:
    print("✅ 一切正常，可以开始今天的学习了")
else:
    print("⚠️  没有使用虚拟环境，请检查 PyCharm 右下角的解释器设置")

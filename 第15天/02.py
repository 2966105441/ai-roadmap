def count_words(words:list[str]) -> dict[str,int]:
    result = {}
    for w in words:
        result[w] = result.get(w,0) + 1
    return result

print(count_words(["a","b","c","a"]))



from typing import Optional

def find_old(name:str) -> Optional[str]:
    return None

def find_new(name:str) -> str|None:
    return None

print(find_old.__annotations__)
print(find_new.__annotations__)
print("两者相等吗：",find_old.__annotations__["return"] == find_new.__annotations__["return"])



def say_hi(name:str) -> None:
    print(f"你好，{name}")

print(say_hi.__annotations__)
def is_palindrome(s):
    """正着读反着读一样就是回文"""
    return s == s[::-1]


def truncate(s,n):
    """超过n个字符就截断，后面加..."""
    if len(s)<=n:
        return s
    return s[:n] + "..."

if __name__ == "__main__":
    print(is_palindrome("上海自来水来自海上"))
    print(is_palindrome("人工智能"))
    print(truncate("这是一段很长很长很长的文字",5))
    print(truncate("短",5))
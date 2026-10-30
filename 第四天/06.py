#5.2 排序：sort 和 sorted 的区别
nums = [3,1,4,1,5,9,2]
print(nums)

nums.sort()   #  从小到大，直接改自己
print(nums)

nums.sort (reverse=True)   # 从大到小
print(nums)

words = ["banana","apple","Cherry"]
print(sorted(words))     # 生成一个新的，不改原列表
print(words)              # 原列表没变
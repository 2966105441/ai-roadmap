def area(width,height):
    return width*height
print(area(10,10))


def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

print(is_even(4))


def greet(name,greeting="你好"):
    print(f"{name},{greeting}")
greet("胡涛")
greet("话筒","早上规划")
greet(greeting="早上好",name="胡涛")


def find_max(nums):
    if len(nums) == 0:
        return "该列表没值"
    else:
        nums_max = nums[0]
        for i in nums:
            if i > nums_max:
                nums_max = i
    return nums_max
print(find_max([88,75,12]))


def count_words(text):
    return len(text.split())
print(count_words("Ai 小明 jasjcaj llll qqqq"))
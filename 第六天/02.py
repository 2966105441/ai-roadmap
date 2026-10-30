def test():
    print("我被执行了")

print("定义完了，但你看到上面那行了吗？")
test()
# def 那段只是登记了一下，直到 test() 那一行才真正跑。

# 函数名怎么起
# 规则	        对的	                        错的
# 小写 + 下划线	find_contact	            FindContact（那是类名写法）
# 动词开头	    show_all add_contact	    contacts2（不知道它干什么）
# 不缩写	        calculate_score	            calc_scr

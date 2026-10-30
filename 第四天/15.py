matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix[0])
print(matrix[1][2])

for row in matrix:
    for x in row:
        print(x,end=" ")
    print()
# end=" " 和空 print() 各自的作用
# print 默认每次打印完自动换行。end=" " 把"换行"换成"空格"，所以数字能排在一行。
# 内层循环跑完后，需要一个空的 print() 把行结束掉——空的 print 就是"只换行"。
# 注意最后一行也带着一个多余的空格，这不算错，肉眼看不出来。

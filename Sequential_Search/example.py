import random

num = 0
data = [0] * 50
for i in range(50):
    data[i] = random.randint(1,100)
# 此处代码主要是打印生成的数字， 生成10行5列的格式
for i in range(10):
    for j in range(5):
        # 此处打印数字, i * 5 + 1 表示当前的位置, 1 * 5 + j 表示区列表中的数字对应, end='' 则为了五个数保持同一行
        print('%2d[%3d] ' % (i * 5 + j + 1, data[i * 5 + j]), end='')
    # 换行
    print('')

while num != -1:
    find = 0
    num = int(input('Enter a number: '))
    # 一下就是最简单的循环列表去逐一比较
    for i in range(50):
        find += 1
        if data[i] == num:
            print(f"在{i + 1} 处找目标数字: {num}, 共查找: {find} 次")

    if find == 0 and num != -1:
        print("can not find any number")

'''
折半查找法

'''

def search(data, num):
    low = 0
    high = len(data) - 1
    while low <= high and num != -1:
        mid = int((low + high) / 2)
        if num < data[mid]:
            print("%d 介于 %d[%d] 和 %d[%d] 之间， 查找左半边" % (num, low + 1, data[low], mid +1 , data[mid]))
            high = mid - 1
        elif num > data[mid]:
            print("%d 介于 %d[%d] 和 %d[%d] 之间， 查找右半边" % (num, mid + 1, data[mid], high + 1, data[high]))
            low = mid+1
        else:
            return mid
    return -1

num = 0
data = [12, 45, 56, 66, 77, 80, 97, 101, 120]
for i in range(1):
    for j in range(len(data)):
        print("%d[%d]" % (i * 9 + j + 1, data[i * 9 + j]), end=' ')
    print('')

while True:
    number = 0
    num = int(input("Enter"))
    if num == -1:
        break
    number = search(data, num)
    if number == -1:
        print("Not found")
    else:
        print(f"Found number {number + 1}, {data[number]}")

"""
程序运行逻辑：
    low 和 high 分别对应0， 和列表的最大索引值
    low <= high: low 和 high 会移动，此处进行判断
    mid = int((low + high) / 2)： 用于查找已经排序好的列表中位的索引
    data[num] 取列表中位的值与查找的值进行比较
    如果num 小于 data[num], 就意味着查找的值在列表的左半边
    所以 最高位 high 就等于 mid - 1， 在此例子中，high就成了3
    所以新的取值区间就变成了0-3




"""
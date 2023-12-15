"""
插补查找算法
"""
def insert_search(data, num):
    low = 0
    high = len(data) - 1
    while low <= high and num != 1:
        """
        for example search num is 57， list is [34, 53, 57, 68, 72, 81, 89, 93, 99]
        0 + int((57 - data[0]) * (8-0)/(data[8]-data[0]))
        0 + (57 - 34) * 8/(99-34)
        核心计算公式： middle = left + (target-data[left])/(data[right]-data[left])*(right-left)
        取middle对应的值与目标比较，如果data[mid] > num, 则将最高位索引长度重新赋值为mid  - 1
        else：将最低位赋值为mid + 1
        """
        mid = low + int((num - data[low]) * (high - low) / (data[high] - data[low]))
        if num == data[mid]:
            return mid
        elif num < data[mid]:
            print(f"要查找的值{num}介于{low + 1}, {data[low]}和{mid + 1}, {data[mid]}之间，向左查找")
            high = mid - 1

        elif num > data[mid]:
            print(f"要查找的值{num}介于{mid + 1},{data[mid]}和{high + 1}, {data[high]}之间，向右查找")
            low = mid + 1
    return -1
num = 0
data = [0] * 9
for i in range(9):
    num = int(input("please input a number: "))
    data[i] = num
print(f"the list is: {data}")
while True:
    number = 0
    num = int(input("please input a number you want to search: "))
    if num == -1:
        break
    number = insert_search(data, num)
    if number == -1:
        print("can not find the number")
    else:
        print(number +1, data[number])
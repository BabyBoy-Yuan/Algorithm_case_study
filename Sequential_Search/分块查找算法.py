def search(data, key):
    length = len(data)  # 获取列表长度
    first = 0  # 列表第一个元素下标
    last = length - 1  # 列表最后一个元素下标
    print("长度：%s 分块的数据是： %s" % (length, data))
    while first <= last:
        mid = (first + last) // 2
        if data[mid] == key:
            return mid
        elif data[mid] > key:
            last = mid - 1
        else:
            first = mid + 1
    return False

def block(data, count, key):
    """

    :param data: 列表
    :param count: 块长度
    :param key: 查找的数据
    :return:
    """
    length = len(data)  # 获取列表长度
    blocklenght = length//count  # 计算分块
    if count * blocklenght != length:  # 如果分块数乘以块长度不等于列表长度，块数加一
        blocklenght += 1
    print(f"共 {blocklenght} 块")
    print("块的数据是：")
    for block_i in range(blocklenght):  # 遍历块
        block_data = []  # 创建一个列表，用于存储块数据
        for i in range(count): # 向块中添加数据
            if block_i * count + i >= length:
                break
            block_data.append(data[block_i * count + i])
        result = search(block_data, key)
        if result != False:
            return block_i* count + result
    return False


data = [23,43,56,78,97,100,120,135,147,150,155]
result = block(data, 4, 135)
print(result)
"""
此算法计算逻辑如下：
1、计算列表长度
    lenght = 11， blocklenght= 11//4 = 2 块长度为4，所以11//4=2，剩余3个数据，所以块数加一
    for block_i in range(blocklenght) 这个for循环就是分块
    for i in range(count) 此for循环就是向块中添加数据 
        data[block_i * count + i]， 关键在这段代码
            第一次循环，block_i=0，count=4，i=0，所以data[0*4+0]=data[0]=23
            第二次循环，block_i=0，count=4，i=1，所以data[0*4+1]=data[1]=43
            第三次循环，block_i=0，count=4，i=2，所以data[0*4+2]=data[2]=56
            第四次循环，block_i=0，count=4，i=3，所以data[0*4+3]=data[3]=78
            # ============================================================
            第五次循环，block_i=1，count=4，i=0，所以data[1*4+0]=data[4]=97
            第六次循环，block_i=1，count=4，i=1，所以data[1*4+1]=data[5]=100
            第七次循环，block_i=1，count=4，i=2，所以data[1*4+2]=data[6]=120
            第八次循环，block_i=1，count=4，i=3，所以data[1*4+3]=data[7]=135
            # ============================================================
            第九次循环，block_i=2，count=4，i=0，所以data[2*4+0]=data[8]=147
            第十次循环，block_i=2，count=4，i=1，所以data[2*4+1]=data[9]=150
            第十一次循环，block_i=2，count=4，i=2，所以data[2*4+2]=data[10]=155
"""
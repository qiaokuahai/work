"""
堆排序

第一是建立初始堆

#建立初始大根堆
for i in range(0,length // 2 +1)[::-1]:
    HeapAdjust(sorted_list,i,length)
第二部分是排序的T(n),因为HeapAdjust()是logn,一共执行n次，故T(n)=O(nlogn)
因此总的时间复杂度为O(nlogn)

例如[3, 5, 9, 8, 7]
"""


def heap_sort(input_list):
    # 调整parent结点为大根堆
    def heap_adjust(input_list, parent, length):

        temp = input_list[parent]
        child = 2 * parent + 1

        while child < length:
            if child + 1 < length and input_list[child] < input_list[child + 1]:
                child += 1

            if temp > input_list[child]:
                break
            input_list[parent] = input_list[child]
            parent = child
            child = 2 * child + 1
        input_list[parent] = temp
    if input_list == []:
        return []
    sorted_list = input_list
    length = len(sorted_list)
    # 最后一个结点的下标为length//2-1
    # 建立初始大根堆
    # 构建堆的时候一定要倒着循环，这是因为底层的数据构建完成之后，上层的数据就可以根据底层的结果来构建。
    for i in range(0, length // 2)[::-1]:
        heap_adjust(sorted_list, i, length)

    for j in range(1, length)[::-1]:
        # 把堆顶元素即第一大的元素与最后一个元素互换位置
        temp = sorted_list[j]
        sorted_list[j] = sorted_list[0]
        sorted_list[0] = temp
        # 换完位置之后将剩余的元素重新调整成大根堆
        heap_adjust(sorted_list, 0, j)
        print('%dth' % (length - j))
        print(sorted_list)
    return sorted_list


if __name__ == '__main__':
    input_list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100, 1, 6, 249]
    print("input_list:")
    print(input_list)
    sorted_list = heap_sort(input_list)
    print("sorted_list:")
    print(input_list)

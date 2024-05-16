"""
堆排序

正序排序需要构造大顶堆，倒序构造小顶堆
"""


def heapify(lst, n, i):
    largest = i
    lson = i*2 + 1
    rson = i*2 + 2
    if lson < n and lst[lson] > lst[largest]:
        largest = lson
    if rson < n and lst[rson] > lst[largest]:
        largest = rson
    if i != largest:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)


def heap_sort(lst, n):
    # 构建大顶堆
    first = int((n-1)/2)
    for i in range(first, -1, -1):
        heapify(lst, n, i)

    # 调换第一和最后一个元素
    for j in range(n-1, -1, -1):
        lst[0], lst[j] = lst[j], lst[0]
        heapify(lst, j, 0)


if __name__ == '__main__':
    input_list = [50, 123, 543, 187, 8, 9, 7, 49, 30, 0, 2, 11, 100, 1, 6, 249, 111]
    print("input_list:")
    print(input_list)
    heap_sort(input_list, len(input_list))
    print("sorted_list:")
    print(input_list)

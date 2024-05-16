"""
快速排序
时间复杂度 n*logn
"""


def partition(lst, start, end):
    tmp = lst[start]
    while start < end:
        while lst[end] >= tmp and start < end:
            end -= 1
        lst[start] = lst[end]
        while lst[start] <= tmp and start < end:
            start += 1
        lst[end] = lst[start]
    lst[start] = tmp
    return start


def quick_sort(lst, start, end):
    if start < end:
        mid = partition(lst, start, end)
        quick_sort(lst, start, mid-1)
        quick_sort(lst, mid+1, end)


if __name__ == "__main__":
    test_list = [2, 10, 11, 6, 19, 21]
    test_list = [3, 7, 1, 9, 2, 6, 8, 3]
    quick_sort(test_list, 0, len(test_list)-1)
    print(test_list)

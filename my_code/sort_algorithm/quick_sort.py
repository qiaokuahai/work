"""
快速排序
时间复杂度 n*logn
"""


def quick_sort(arr, start, end):
    if start >= end:
        return
    left_index = start
    right_index = end
    flag_value = arr[left_index]
    while left_index < right_index:  # 这里面一定不能是left_index <= right_index,因为最终要保证left_index与right_index重合
        while left_index < right_index and arr[right_index] >= flag_value:  # 这里必须是 >=， 如果是大于， 则由数据相等的时候会导致死循环
            right_index -= 1
        arr[left_index] = arr[right_index]
        while left_index < right_index and arr[left_index] <= flag_value:
            left_index += 1
        arr[right_index] = arr[left_index]

    # 此时left_index和right_index相等
    arr[left_index] = flag_value
    quick_sort(arr, start, left_index-1)
    quick_sort(arr, right_index + 1, end)


if __name__ == "__main__":
    test_list = [2, 10, 11, 6, 19, 21]
    test_list = [3, 7, 1, 9, 2, 6, 8, 3]
    quick_sort(test_list, 0, len(test_list)-1)
    print(test_list)

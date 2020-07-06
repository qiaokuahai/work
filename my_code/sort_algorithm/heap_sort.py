"""
堆排序

第一是建立初始堆

#建立初始大根堆
for i in range(0,length // 2 +1)[::-1]:
    HeapAdjust(sorted_list,i,length)
第二部分是排序的T(n),因为HeapAdjust()是logn,一共执行n次，故T(n)=O(nlogn)
因此总的时间复杂度为O(nlogn)

正序排序需要构造大顶堆，倒序构造小顶堆
"""


# 本示例构造的是大顶堆
def heap_sort(input_list):
    # 调整parent结点为大根堆
    def heap_adjust(input_list, parent, length):
        # 获取当前节点的左子树和右子树
        parent_index = parent
        left_child_index = parent_index * 2 + 1
        right_child_index = parent_index * 2 + 2
        curr_index = left_child_index  # 当前指针指向的位置，默认指向当前节点的左子树
        while curr_index < length:
            parent_value = input_list[parent_index]  # 首先获取父节点的值
            if right_child_index < length:
                if input_list[left_child_index] < input_list[right_child_index]:
                    # 如果要构造小顶堆，1.需要改input_list[left_child_index] > input_list[right_child_index]
                    # 如果要构造小顶堆，2.需要改parent_value < input_list[curr_index]
                    curr_index += 1
            # curr_value为当前节点的值，此时的curr_index已经是子节点中值最大的那个结点的index
            if parent_value > input_list[curr_index]:
                break
            # 对调父节点和子节点的数据
            input_list[parent_index], input_list[curr_index] = input_list[curr_index], input_list[parent_index]
            parent_index = curr_index
            left_child_index = parent_index * 2 + 1
            right_child_index = parent_index * 2 + 2
            curr_index = left_child_index

    length = len(input_list)
    # 最后一个结点的下标为length//2-1
    # 建立初始大根堆
    # 构建堆的时候一定要倒着循环，这是因为底层的数据构建完成之后，上层的数据就可以根据底层的结果来构建。
    for i in range(length // 2 - 1, -1, -1):
        heap_adjust(input_list, i, length)

    for j in range(1, length)[::-1]:
        # 把堆顶元素即第一大的元素与最后一个元素互换位置
        input_list[0], input_list[j] = input_list[j], input_list[0]
        # 换完位置之后将剩余的元素重新调整成大根堆
        # 调整的时候就不用全部遍历了，单次深度往下走，将顶层元素放到合适的位置，因为除了顶层的元素， 其他的元素都满足根节点大于子节点
        heap_adjust(input_list, 0, j)
        print('%dth' % (length - j))
        print(input_list)
    return input_list


if __name__ == '__main__':
    input_list = [50, 123, 543, 187, 8, 9, 7, 49, 30, 0, 2, 11, 100, 1, 6, 249, 111]
    print("input_list:")
    print(input_list)
    sorted_list = heap_sort(input_list)
    print("sorted_list:")
    print(input_list)

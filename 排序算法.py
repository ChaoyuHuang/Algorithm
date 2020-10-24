# encoding: utf-8

##排序算法的集中解决方案
## LOW B组合
###1、冒泡排序

import time


def maopao(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr


print(maopao([8, 5, 2, 1, 10]))


## 选择排序
def select_sort(arr):
    for i in range(len(arr) - 1):
        min_pos = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_pos]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return (arr)


print(select_sort([8, 5, 2, 1, 10]))


## 插入排序
def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


print(insert_sort([8, 5, 2, 1, 10]))


## 快速排序 先找到一个base值，将list分割为两个，继而进行递归
def _quick_sort1(arr):
    if len(arr) < 2:
        return arr
    tmp = arr[0]
    left = [v for v in arr[1:] if v <= tmp]
    right = [v for v in arr[1:] if v > tmp]
    left = _quick_sort1(left)
    right = _quick_sort1(right)
    return left + [tmp] + right


def quick_sort1(arr):
    return _quick_sort1(arr)


# 快排第二种写法
def quick_sort2(arr, start, end):
    if start < end:
        i, j = start, end
        base = arr[i]

        while i < j:
            while i < j and (arr[j] >= base):
                j -= 1
            arr[i] = arr[j]
            while i < j and (arr[i] <= base):
                i += 1
            arr[j] = arr[i]
        arr[i] = base

        quick_sort2(arr, start, i - 1)
        quick_sort2(arr, j + 1, end)
    return arr


myList = [9, 2, 1, 6, 4, 10, 0.5, 0]
print("Quick Sort: ")
start = time.time()
quick_sort2(myList, 0, len(myList) - 1)
end = time.time()
print(myList)
print("use time:", end - start)


## 堆排序

### 构建堆的过程
def sift(arr, low, high):
    # arr表示树， low表示树根，high表示树最后一个节点的位置
    tmp = arr[low]
    i = low
    j = 2 * i + 1
    # i指向空位， j指向两个子节点
    while j <= high:  # 循环退出的第二种情况:j>high了，没有子节点了
        if j + 1 <= high and arr[j] < arr[j + 1]:  # 如果右子节点存在且大于左子节点,指向右节点
            j += 1
        if arr[j] > tmp:
            arr[i] = arr[j]
            i = j
            j = 2 * i + 1
        else:  # 退出的第一种情况：j位置的值比tmp要小，说明两个子节点都比tmp小
            break
    arr[i] = tmp


### 构建堆以后，挨个出数
def heap_sort(arr):
    n = len(arr)
    # 1. 构建堆
    for low in range(n // 2 - 1, -1, -1):
        sift(arr, low, n - 1)
    # 2.挨个出数
    for high in range(n - 1, -1, -1):
        arr[0], arr[high] = arr[high], arr[0]
        sift(arr, 0, high - 1)


myList = [9, 2, 1, 6, 4, 10, 0.5, 0]
print("heap_sort: ")
start = time.time()
heap_sort(myList)
end = time.time()
print(myList)
print("use time:", end - start)


## 归并排序:适合现有列表为两段有序，将其合并为一个列表
def merge_sort(arr, low, mid, high):
    # 列表两段有序[0, mid],  [mid:high]
    i = low
    j = mid + 1
    arr_tmp = []
    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            arr_tmp.append(arr[i])
            i += 1
        else:
            arr_tmp.append(arr[j])
            j += 1
    while i <= mid:
        arr_tmp.append(arr[i])
        i += 1
    while j <= high:
        arr_tmp.append(arr[j])
        j += 1
    # arr_tmp[0:x]写到 arr[low:high]
    for i in range(low, high + 1):
        arr[i] = arr_tmp[i - low]
    return arr


print(merge_sort([1, 3, 5, 8, 9, 2, 4, 7], 0, 4, 7))


## 合并两个有序列表为一个列表
def merge_list(arr1, arr2):
    i = 0
    j = 0
    arr_tmp = []
    while i <= (len(arr1) - 1) and j <= (len(arr2) - 1):
        if arr1[i] < arr2[j]:
            arr_tmp.append(arr1[i])
            i += 1
        else:
            arr_tmp.append(arr2[j])
            j += 1
    while i <= (len(arr1) - 1):
        arr_tmp.append(arr1[i])
        i += 1
    while j <= (len(arr2) - 1):
        arr_tmp.append(arr2[j])
        j += 1
    return arr_tmp


print(merge_list([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))


##递归写法
def merge1(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge1(arr, low, mid)
        merge1(arr, mid + 1, high)
        arr = merge_sort(arr, low, mid, high)
	return arr


print(merge1([1, 3, 5, 7, 9, 2, 4, 6], 0, 7))

# 一般情况下耗时 快速排序 < 归并排序 < 堆排序
# 三种排序方式的缺点:
## 1、快速排序：极端情况下排序效率很低 比如[9,8,7,6,5,4,3,2,1]这样倒叙的数组
## 2、归并排序: 需要额外的内存开销
## 3、堆排序: 在快的排序算法中相对较慢

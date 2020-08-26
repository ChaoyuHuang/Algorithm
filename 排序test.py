# encoding: utf-8
def maopao(arr):
	for i in range(len(arr)-1):
		for j in range(len(arr)-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

arr = [10, 1, 0, 8, 9, 12, 16, -0.1]
print(maopao(arr))


def select_sort(arr):
	for i in range(len(arr)-1):
		min_pos = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[min_pos]:
				min_pos = j
		arr[i], arr[min_pos] = arr[min_pos], arr[i]
	return arr
print(select_sort(arr))

def insert_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and (arr[j] > key):
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
	return arr

print(insert_sort(arr))


def quick_sort(arr, start, end):
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
		quick_sort(arr, start, i-1)
		quick_sort(arr, j+1, end)
	return arr

print(quick_sort(arr, 0, len(arr) - 1))


def _quick_sort(arr):
	if len(arr) < 2:
		return arr
	tmp = arr[0]
	left = [v for v in arr[1:] if v <= tmp]
	right = [v for v in arr[1:] if v > tmp]
	left = _quick_sort(left)
	right = _quick_sort(right)
	return left + [tmp] + right

def quick_sort1(arr):
	return _quick_sort(arr)

print(quick_sort1(arr))


## 堆排序
### 建立堆
def sift(arr, low, high):
	tmp = arr[low]
	i = low
	j = 2 * i + 1
	while j <= high:
		while j + 1 <= high and (arr[j+1] > arr[j]):
			j += 1
		if arr[j] > tmp:
			arr[i] = arr[j]
			i = j
			j = 2 * i + 1
		else:
			break
	arr[i] = tmp

def heap_sort(arr):
	n = len(arr)
	for low in range(n//2, -1, -1):
		sift(arr, low, n-1)
	##挨个出数
	for high in range(n-1, -1, -1):
		arr[0], arr[high] = arr[high], arr[0]
		sift(arr, 0, high - 1)

heap_sort(arr)
print(arr)

## 归并排序
def merge_sort(arr, low, mid, high):
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
	for i in range(low, high+1):
		arr[i] = arr_tmp[i-low]
	return arr

print(merge_sort([1,3,5,7,9,2,4,6,8,10], 0, 4, 9))
# encoding: utf-8

## 二分查找, 循环思路
def binarySearch(arr, val):
	low = 0
	high = len(arr) - 1
	while low <= high:
		mid = (high + low) // 2
		if arr[mid] == val:
			return mid
		elif arr[mid] > val:
			high = mid - 1
		else:
			low = mid + 1
	return -1

print(binarySearch([1,2,3,4,5,6,8],5))

## 递归二分查找
def binarySearch1(arr, low, high, val):
	if high >= low:
		mid = (low + high) // 2
		if arr[mid] == val:
			return mid
		elif arr[mid] > val:
			return binarySearch1(arr, low, high-1, val)
		else:
			return binarySearch1(arr, low+1, high, val)
	else:
		return -1


## 线性查找
def linear_search(arr, val):
	for i in range(len(arr)):
		if arr[i] == val:
			return i
	return -1

print(binarySearch1([2,5,3,1,2,4], 0, 5, 3))


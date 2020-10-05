# encoding: utf-8
## 循环的写法，这个写法效率最高
def feibo(n):
    a = 1
    b = 1
    c = 1
    if n <= 2:
        return c
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c


print(feibo(20))


## 循环写法，加一个list进行存储
def feibo2(n):
    result = [1, 1]
    if n <= 2:
        return result[-1]
    for i in range(2, n + 1):
        result.append(result[i - 1] + result[i - 2])
    return result[-1]


print(feibo2(20))


## 递归写法，效率最低
def feibo3(n):
    if (n == 0) | (n == 1):
        return 1
    else:
        return feibo3(n - 1) + feibo3(n - 2)


print(feibo3(20))

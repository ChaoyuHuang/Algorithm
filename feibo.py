def feibo3(n):
    tmp = [1, 2, 4, 8]
    if n <= 0:
    	return -1
    if n <= 4:
    	return tmp[n-1]
    else:
    	for i in range(4, 102):
    		tmp.append(tmp[i-1] + tmp[i-2] + tmp[i-3] + tmp[i-4])
    return tmp[-1]

print(feibo3(102)) 



def feibo4(n):
	if n <= 0:
		return -1
	if n == 1:
		return 1
	elif n == 2:
		return 2
	elif n == 3:
		return 4
	elif n == 4:
		return 8
	else:
		for i in range(5, 6):
			return feibo4(i-1) + feibo4(i-2) + feibo4(i-3) + feibo4(i-4)

print(feibo4(5))
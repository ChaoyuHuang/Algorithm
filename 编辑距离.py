# encoding:utf-8
s1 = "abcssss"
s2 = "acefgssd"

n = len(s1) + 1
m = len(s2) + 1
dq = [[0] * m for i in range(n)]
for i in range(n):
	dq[i][0] = i
for j in range(m):
	dq[0][j] = j
for i in range(1, n):
	for j in range(1, m):
		if s1[i-1] == s2[j-1]:
			dq[i][j] = dq[i-1][j-1]
		else:
			dq[i][j] = min(dq[i-1][j-1], dq[i][j-1], dq[i-1][j]) + 1
print(dq[-1][-1])


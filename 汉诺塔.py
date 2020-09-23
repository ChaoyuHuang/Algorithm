# encoding: utf-8

##递归思想，这题用递归是最优解   2^n - 1
def hano(n, A, B, C):
    if n > 0:
        hano(n - 1, A, C, B)  # 由A经C再到B
        print("%s->%s" % (A, C))  # 必有一步A-C
        hano(n - 1, B, A, C)  # 再由B经A到C

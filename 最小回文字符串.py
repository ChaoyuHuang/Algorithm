# encoding: utf-8

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        length = len(s)
        ## 如果字符串长度为1，或者字符串跟倒序一样，那么直接返回
        if length == 1 or s == s[::-1]:
            return s
        max_len, start = 1, 0
        for i in range(1, length):
            even = s[i - max_len:i + 1]
            odd = s[i - max_len - 1:i + 1]
            if i - max_len - 1 >= 0 and odd == odd[::-1]:  ## 如果找到了第一个三位字母是回文字符串，则start变为i-max_len-1开始搜索
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
                continue
        return s[start:start + max_len]


a = 'abcdbdca'

solution = Solution()
print(solution.longestPalindrome(a))
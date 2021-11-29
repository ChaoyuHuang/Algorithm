## url:https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
## code:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}
        for i, v in enumerate(s):
            if v in c_dict and c_dict[v] > k:
                k = c_dict[v]
                c_dict[v] = i
            else:
                c_dict[v] = i
                res = max(res, i-k)
        return res

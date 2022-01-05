class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 首先，如果一共就没有三个数字，直接返回空
        if len(nums) < 3:
            return []
        
        #先排序 这样可以如果第一个数字就大于0 后面的都不用判断了 输出结果 节省时间
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return res #如果第一个数字就大于0 后面的都不用判断了 输出结果
 
            if i > 0 and nums[i] == nums[i-1]:
                continue #如果这个数和前一个数一样 就跳过这个数字 不然就重复判断了
                         #i>0是因为python可以有nums[-1]，就算所有数字相同，aka第一个数字和最后一个数字 
                         #相同，第一个数字也肯定要判断，不能跳过
            else:
                #双指针，L从i的后一个开始，R从最后一个开始
                L = i+1
                R = len(nums)-1
                while L<R:
                    if nums[i] + nums[L] +nums[R] == 0:
                        res.append([nums[i], nums[L], nums[R]])
                        #找到一个答案后，L和R都要先指到下一个不同的的数字 才能避免重复
                        while L<R and nums[L] == nums[L+1]:
                            L += 1
                        while L<R and nums[R] == nums[R-1]:
                            R -= 1
                        #while loop停下的时候表示L和R已经到了最后一个相同数字 再移一次就是新数字了
                        L += 1
                        R -= 1
                    elif nums[i] + nums[L] +nums[R] < 0: #i固定 sum小了 说明左指针需要变大
                        L += 1
                    elif nums[i] + nums[L] +nums[R] > 0: #i固定 sum大了 说明右指针需要变小
                        R -= 1
                        
        return res

class Solution:
    def threeSum(self, nums: List(int) -> List[List[int]]):
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                L = i + 1
                R = len(nums) - 1
                while L < R:
                    if nums[i] + nums[L] + nums[R] == 0:
                        res.append(nums[i], nums[L], nums[R])
                        while L < R and nums[L] == nums[L+1]:
                            L += 1
                        while L < R and nums[R] == nums[R-1]:
                            R -=1
                        L += 1
                        R -= 1
                    elif nums[i] + nums[L] + nums[R] < 0:
                        L += 1
                    elif nums[i] + nums[L] + nums[R] >0:
                        R -= 1
        return res
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count1 = sum(nums)
        n = len(nums)
        maxCount = float('-inf')
        i, j = 0, 0
        cur1 = 0
        while j < 2* n:
            if nums[j % n] == 1:
                cur1 += 1
            while j - i + 1 > count1:
                if nums[i % n] == 1:
                    cur1 -= 1
                i += 1
            maxCount = max(maxCount, cur1)
            j += 1
        return count1 - maxCount

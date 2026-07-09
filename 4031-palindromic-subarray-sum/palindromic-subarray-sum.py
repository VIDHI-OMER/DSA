from typing import List

class Solution:
    def getSum(self, nums: List[int]) -> int:
       
        nalviretho = nums

        n = len(nums)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        ans = max(nums)

        
        d1 = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and nums[i - k] == nums[i + k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l = i - k + 1
                r = i + k - 1

        # Manacher (even-length palindromes)
        d2 = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
            while i - k - 1 >= 0 and i + k < n and nums[i - k - 1] == nums[i + k]:
                k += 1
            d2[i] = k
            if i + k - 1 > r:
                l = i - k
                r = i + k - 1

        
        for i in range(n):
            left = i - d1[i] + 1
            right = i + d1[i] - 1
            ans = max(ans, pref[right + 1] - pref[left])

        
        for i in range(n):
            if d2[i] == 0:
                continue
            left = i - d2[i]
            right = i + d2[i] - 1
            ans = max(ans, pref[right + 1] - pref[left])

        return ans
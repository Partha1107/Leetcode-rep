
from typing import List
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque()

        left = 0
        operations = 0
        ans = 0

        for right in range(n):
            x = nums[n - 1 - right]
            count = 1

            while dq and dq[-1][0] <= x:
                val, cnt = dq.pop()
                operations += (x - val) * cnt
                count += cnt

            dq.append([x, count])

            while operations > k:
                val = nums[n - 1 - left]
                operations -= dq[0][0] - val

                dq[0][1] -= 1

                if dq[0][1] == 0:
                    dq.popleft()

                left += 1

            ans += right - left + 1

        return ans

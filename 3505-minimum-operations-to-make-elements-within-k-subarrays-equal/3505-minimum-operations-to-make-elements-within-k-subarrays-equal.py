from heapq import heappush, heappop
from collections import Counter


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        low = []   # Max heap (store negative values)
        high = []  # Min heap

        low_count = Counter()
        high_count = Counter()

        delayed_low = Counter()
        delayed_high = Counter()

        low_size = 0
        high_size = 0

        sum_low = 0
        sum_high = 0

        def prune_low():
            while low:
                val = -low[0]

                if delayed_low[val] == 0:
                    break

                heappop(low)
                delayed_low[val] -= 1

        def prune_high():
            while high:
                val = high[0]

                if delayed_high[val] == 0:
                    break

                heappop(high)
                delayed_high[val] -= 1

        def balance():
            nonlocal low_size, high_size
            nonlocal sum_low, sum_high

            prune_low()
            prune_high()

            while low_size > high_size + 1:
                val = -heappop(low)

                low_count[val] -= 1
                high_count[val] += 1

                low_size -= 1
                high_size += 1

                sum_low -= val
                sum_high += val

                heappush(high, val)
                prune_low()

            while low_size < high_size:
                val = heappop(high)

                high_count[val] -= 1
                low_count[val] += 1

                high_size -= 1
                low_size += 1

                sum_high -= val
                sum_low += val

                heappush(low, -val)
                prune_high()

        def add(val):
            nonlocal low_size, high_size
            nonlocal sum_low, sum_high

            prune_low()

            if not low or val <= -low[0]:
                heappush(low, -val)
                low_count[val] += 1

                low_size += 1
                sum_low += val
            else:
                heappush(high, val)
                high_count[val] += 1

                high_size += 1
                sum_high += val

            balance()

        def remove(val):
            nonlocal low_size, high_size
            nonlocal sum_low, sum_high

            if low_count[val] > 0:
                low_count[val] -= 1
                delayed_low[val] += 1

                low_size -= 1
                sum_low -= val

                prune_low()

            else:
                high_count[val] -= 1
                delayed_high[val] += 1

                high_size -= 1
                sum_high -= val

                prune_high()

            balance()

        def get_cost():
            median = -low[0]

            return (
                median * low_size - sum_low
                + sum_high - median * high_size
            )

        # Step 1: Calculate the cost of every window
        costs = [0] * (n - x + 1)

        for i in range(n):
            add(nums[i])

            if i >= x:
                remove(nums[i - x])

            if i >= x - 1:
                costs[i - x + 1] = get_cost()

        # Step 2: Dynamic programming
        INF = float("inf")

        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):

                # Option 1: Skip current element
                dp[i][j] = dp[i - 1][j]

                # Option 2: Select a window of size x
                if i >= x and dp[i - x][j - 1] != INF:

                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - x][j - 1] + costs[i - x]
                    )

        return dp[n][k]
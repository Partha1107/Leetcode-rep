class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        
        def digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        
       
        sorted_idx = sorted(range(n), key=lambda i: (digit_sum(nums[i]), nums[i]))
        
        
        perm = [0] * n
        for target_pos, orig_idx in enumerate(sorted_idx):
            perm[orig_idx] = target_pos
        
        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i]:
                continue
            
            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = perm[j]
                cycle_len += 1
            swaps += cycle_len - 1
        
        return swaps
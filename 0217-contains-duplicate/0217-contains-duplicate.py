class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Create a set to store numbers we've already seen
        seen = set()
        
        for num in nums:
            # If the number is already in the set, we found a duplicate
            if num in seen:
                return True
            # Otherwise, add the number to the set
            seen.add(num)
            
        # If the loop finishes without finding a duplicate
        return False
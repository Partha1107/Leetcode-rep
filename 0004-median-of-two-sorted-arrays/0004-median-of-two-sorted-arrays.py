class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        # Make nums1 the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x = len(nums1)
        y = len(nums2)

        low = 0
        high = x

        while low <= high:

            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            # Correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:

                # Even total length
                if (x + y) % 2 == 0:
                    return (
                        max(maxLeftX, maxLeftY) +
                        min(minRightX, minRightY)
                    ) / 2.0

                # Odd total length
                return max(maxLeftX, maxLeftY)

            # Move left
            elif maxLeftX > minRightY:
                high = partitionX - 1

            # Move right
            else:
                low = partitionX + 1
# https://leetcode.com/problems/two-sum/description/
from itertools import combinations


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []


    def twoSum_brute_force(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum_dict(self, nums, target):
        # Dictionary to store number -> index mapping
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement exists in our hash map
            if complement in seen:
                return [seen[complement], i]

            # Store the current number and its index
            seen[num] = i

        print(seen)
        return None

if __name__ == '__main__':
    print(Solution().twoSum_dict([2, 7, 11, 15], 9))

    # print(f1)
    # f2 = Solution().twoSum([3, 2, 4], 6)
    # print(f2)
    # f3 = Solution().twoSum_brute_force([3, 3], 6)
    # print(f3)


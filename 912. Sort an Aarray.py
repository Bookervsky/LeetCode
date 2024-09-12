class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        return self.merge(self.sortArray(left), self.sortArray(right))

    def merge(self,left,right): # Merge two sorted numays
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            # Append the remaining part
        result.extend(left[i:])
        result.extend(right[j:])
        return result
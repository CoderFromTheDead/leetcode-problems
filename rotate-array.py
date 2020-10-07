'''
Link - https://leetcode.com/problems/rotate-array/
'''
class Solution:
    #A function to reverse the array.
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
                
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)#Reverse all the elements
        self.reverse(nums, 0, k - 1)#Reverse first k elements
        self.reverse(nums, k, n - 1)#Reverse the remaining n-k elements.

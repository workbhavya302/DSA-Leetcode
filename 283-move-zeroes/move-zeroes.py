class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                # Swap elements
                #nums[write], nums[read] = nums[read], nums[write]
                temp = nums[write]
                nums[write] = nums[read]
                nums[read] = temp
                write += 1

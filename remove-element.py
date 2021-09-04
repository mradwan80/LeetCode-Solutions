#remove all occurances of a specific value from list elements

class Solution:
    def removeElement(self, nums, val: int) -> int:
        size=len(nums)
        for i in range(size-1,-1,-1):
            if nums[i]==val:
                nums.pop(i)

nums=[3,2,2,3]
print(nums)

sol = Solution()
sol.removeElement(nums,3)

print(nums)

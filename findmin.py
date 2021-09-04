#find the minimum in a sorted array with binary search
#the array is shifted many times, so min is not necessarily the first element

class Solution:
    def findMin(self, nums) -> int:
        lgt=len(nums)
        
        if lgt==1:
            return nums[0]
        
        i=lgt // 2
        if nums[i-1]>nums[i]:
            return nums[i]
        else:
            if nums[i]>nums[lgt-1]:
                return self.findMin(nums[i:lgt])
            else:
                return self.findMin(nums[0:i])

sol = Solution()
min=sol.findMin([1,2])
print(min)
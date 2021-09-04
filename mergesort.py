class Solution:
    def sortArray(self, nums):
        

        if len(nums)<2:
            return nums
        elif len(nums)==2:
            if nums[0]<=nums[1]:
                return nums
            else:
                return [nums[1],nums[0]]
        
        mid=len(nums)//2
        
        l1=self.sortArray(nums[:mid])
        l2=self.sortArray(nums[mid:])
        
        res=[]
        
        p1=0
        p2=0
        while p1<len(l1) or p2<len(l2):
            
            if p2>=len(l2):
                res.append(l1[p1])
                p1=p1+1
            elif p1>=len(l1):
                res.append(l2[p2])
                p2=p2+1
            elif l1[p1]<l2[p2]:
                res.append(l1[p1])
                p1=p1+1
            else:
                res.append(l2[p2])
                p2=p2+1
                
        return res    
                
sol = Solution()
print(sol.sortArray([5,2,3,1]))
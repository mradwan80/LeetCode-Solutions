#re-sort a list, so that all even numbers come first, then all odd numbers

class Solution:
    def sortArrayByParity(self, nums):
        odd=[]
        even=[]
        for el in nums:
            if el%2==0:
                even.append(el)
            else:
                odd.append(el)
        
        outp=even
        
        for el in odd:
            outp.append(el)
            
        return outp

nums=[3,1,2,4]
print(nums)

sol=Solution()
outp = sol.sortArrayByParity(nums)
print(outp)
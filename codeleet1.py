class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        res=False
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i!=j and arr[i]==2*arr[j]:
                    res=True
                    
        return res
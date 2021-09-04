#find two values that sum to a target, given an array of values sorted in an ascending order
#not allowed to return the same index (even if 2*list[index]==target indeed)
#idea would be to traverse linearly, and each element, seach for the compliment value in the sublist of element on its right

def binary_search(list, index, target):
    first=index+1
    last=len(list)-1

    while first<=last:
        mid=(first+last)//2
        if list[mid]==target:
            return mid
        elif list[mid]>target:
            last=mid-1
        else:
            first=mid+1

    return -1

def find_two(list, target):

    for i in range(len(list)):
        cand=binary_search(list, i, target-list[i])
        if cand!=-1:
            return [i+1,cand+1]

    return [-1,-1]

numbers, target = [2,7,11,15], 9
#numbers=  [2,7,11,15]
target = 9
ll=find_two(numbers, target)
print (ll)

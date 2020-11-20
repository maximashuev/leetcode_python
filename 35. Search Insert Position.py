"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
"""

def searchInsert( nums, target):
    lo=0
    hi=len(nums)-1
    while lo <= hi:
        mid=(hi+lo)//2
        mid_val=nums[mid]
        if target == mid_val:
            print("result=",mid)
            return mid
        elif target>mid_val:
            lo=mid+1
        else:
            hi=mid-1
    print("result=",lo)
    return lo

searchInsert(nums = [-1,2,3,5,7,9,10], target = 0)
searchInsert(nums = [1], target = 0)

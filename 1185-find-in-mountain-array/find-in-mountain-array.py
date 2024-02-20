# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int,mountain_arr: 'MountainArray') -> int:
        low = 0
        high = mountain_arr.length()-1
        low1 = 0
        high1= high
        low2 = 0
        high2 = high
        while low<=high:
            mid = (low+high)//2
            mid_1 = mid-1
            mid2 = mid+1
            if mid_1<0:
                high1 = mid2
                low1 = 0
                high2 = mountain_arr.length()-1
                low2 = mid2
                break
            a = mountain_arr.get(mid_1) 
            b = mountain_arr.get(mid)
            c = mountain_arr.get(mid2)
            print(mid_1,low2,high2)
            if a<b>c:
                high1 = mid
                low1 = 0
                high2 = mountain_arr.length()-1
                low2 = mid
                break
            if a<b<c:
                low = mid+1
            else:
                high = mid-1
        print(low1,high1,"###")
        while low1<=high1:
            mid = (low1+high1)//2
            b = mountain_arr.get(mid)
            if b == target:
                return mid
            if b<target:
                low1 = mid+1
            else:
                high1 = mid-1
            print(low1,high1)
        print("###")
        
        while low2<=high2:
            mid = (low2+high2)//2
            b = mountain_arr.get(mid)
            if b == target:
                return mid
            if b>target:
                low2 = mid+1
            else:
                high2 = mid-1
            print(low,high)
        return -1
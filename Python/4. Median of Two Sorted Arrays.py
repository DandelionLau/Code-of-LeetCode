import math

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        temp = nums1
        temp.extend(nums2)              # connect two list
        newList = sorted(temp)
        newListLength = len(newList)
        mid = math.floor(len(newList)/2)
        if newListLength%2 == 1:
            return newList[mid]
        else:
            return 0.5*(newList[mid-1] + newList[mid])

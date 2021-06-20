"""
@FileName: 496. Next Greater Element I.py
@Description: Implement 496. Next Greater Element I
@Author: Ryuk
@CreateDate: 2021/06/20
@LastEditTime: 2021/06/20
@LastEditors: Please set LastEditors
@Version: v0.1
"""

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        equal_flag = False
        larger_flag = False
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    equal_flag = True

                if equal_flag:
                    if nums2[j] > nums1[i]:
                        result.append(nums2[j])
                        larger_flag = True
                        break

                if larger_flag:
                    break

            if larger_flag is False:
                result.append(-1)
            equal_flag = False
            larger_flag = False

        return result

def main():
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    sol = Solution()
    result = sol.nextGreaterElement(nums1, nums2)
    print(result)



if __name__ == '__main__':
    main()
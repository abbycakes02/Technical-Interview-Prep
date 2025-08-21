class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # 2 pointer at the end, one at element m
        # loop thru the array
        # check if nums2[ptr] >= nums[ptr3]
        # overwrite nums[ptr2]
        # decrement ptr2, ptr
        #else:
        # update curr element to equal last
        # decrement curr, last
        end1 = (m + n) - 1
        end2 = n-1
        merge_pos = m-1
        while end2 >= 0:
            if merge_pos >= 0 and nums1[merge_pos] > nums2[end2]:
                nums1[end1] = nums1[merge_pos]
                #print(end1, merge_pos)
                end1 -= 1
                merge_pos -= 1
            else:
                nums1[end1] = nums2[end2]
                end1 -= 1
                end2 -= 1
        return nums1


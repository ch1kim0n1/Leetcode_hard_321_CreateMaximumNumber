class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick(nums, t):
            if t == 0:
                return []
            if t == len(nums):
                return nums

            drop = len(nums) - t
            stack = []

            for x in nums:
                while drop and stack and stack[-1] < x:
                    stack.pop()
                    drop -= 1
                stack.append(x)

            return stack[:t]

        def merge(a, b):
            i = j = 0
            la, lb = len(a), len(b)
            res = []

            while i < la or j < lb:
                ii, jj = i, j

                while ii < la and jj < lb and a[ii] == b[jj]:
                    ii += 1
                    jj += 1

                if jj == lb or (ii < la and a[ii] > b[jj]):
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1

            return res

        m, n = len(nums1), len(nums2)
        best = []

        for take1 in range(max(0, k - n), min(k, m) + 1):
            candidate = merge(
                pick(nums1, take1),
                pick(nums2, k - take1)
            )

            if candidate > best:
                best = candidate

        return best

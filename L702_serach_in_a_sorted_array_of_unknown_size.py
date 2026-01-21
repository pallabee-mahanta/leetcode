# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        # Since the size of the array is unknown, we need to determine the search
        #   range first, i.e., the right index of the array
        # initiate the array size as [0,1], keep doubling the size until we find
        #    target > reader.get[r].
        l, r = 0, 1
        while target > reader.get(r):
            r = r * 2

        # After we determined the search range, we can do a traditional binary
        #  search
        while l <= r:
            m = (l + r) // 2
            print(l, m, r)
            # we find the target, return the index
            if reader.get(m) == target:
                return m
            # Since we didn't find the target, we eliminate the half that the
            #   target isn't in.
            else:
                if reader.get(m) < target:
                    l = m + 1
                else:
                    r = m - 1
        # when it's outside the while loop, the algorithm can't find the target,
        #   return -1
        return -1


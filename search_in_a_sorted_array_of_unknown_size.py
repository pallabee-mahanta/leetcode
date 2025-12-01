# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        l = 0
        h = 1
        if (target == reader.get(0)):   return 0
        while (reader.get(h) < target):
            l = h
            h = 2 * l
        print(l, h)
        while (l <= h):
            mid = l + (h - l) / 2
            print(reader.get(mid))
            if (reader.get(mid) == target):
                return mid
            elif (reader.get(mid) < target):
                l = mid + 1
            else:
                h = mid - 1

        return -1

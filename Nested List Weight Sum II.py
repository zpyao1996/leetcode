# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        depth = self.getdepth(nestedList)
        weighted_sum = 0
        while nestedList:
            next_nestedlist = []
            for nested_int in nestedList:
                if NestedInteger.isInteger(nested_int):
                    weighted_sum += depth * NestedInteger.getInteger(nested_int)
                else:
                    next_nestedlist.extend(NestedInteger.getList(nested_int))
            depth -= 1
            nestedList = next_nestedlist
        return weighted_sum

    def getdepth(self, nestedList):
        depth = 0
        while nestedList:
            depth += 1
            next_nestedlist = []
            for nested_int in nestedList:
                next_nestedlist.extend(NestedInteger.getList(
                    nested_int))
            nestedList = next_nestedlist
        return depth
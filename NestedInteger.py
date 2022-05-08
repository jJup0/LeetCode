from typing import List, Union


class NestedInteger:

    @staticmethod
    def nested_list_to_NestedInteger_list(l: List[Union[int, List[int]]]) -> List["NestedInteger"]:
        res = []
        for value in l:
            if type(value) == int:
                res.append(NestedInteger(True, value))
            elif type(value) == list:
                res.append(NestedInteger(False, NestedInteger.nested_list_to_NestedInteger_list(value)))
        return res

    def __init__(self, isInteger, value):
        self.isInteger_ = isInteger
        self.integer = self.list = None
        if isInteger:
            self.integer = value
        else:
            self.list = value

    def __repr__(self):
        if self.isInteger():
            return f"{self.getInteger()}"
        else:
            return f"{self.getList()}"

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return self.isInteger_

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self.integer

    def getList(self) -> List["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self.list

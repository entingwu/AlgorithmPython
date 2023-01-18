# Input: nestedList = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]

# Input: nestedList = [1,[4,[6]]]
# Output: [1,4,6]

class NestedIterator:
    # def __init__(self, nestedList: [NestedInteger]):
    #
    # def next(self) -> int:
    #
    # def hasNext(self) -> bool:

    def parseNestedList(self, nested_list, result):
        if type(nested_list) is int:
            return result.append(nested_list)
        for item in nested_list:
            self.parseNestedList(item, result)
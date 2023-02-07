class SegmentTreeNode:

    def __init__(self, start, end, x):
        # intervals [start, end]
        self.start = start
        self.end = end
        self.interval_sum = x
        # left, right child
        self.left = None
        self.right = None

class SegmentTree:

    def __init__(self, nums: dict[int], start: int, end: int):
        self.root = self.construct(nums, start, end)

    def construct(self, nums: dict[int], start: int, end: int):
        if start > end:
            return None

        node = SegmentTreeNode(start, end, 0)
        if start < end:
            mid = start + (end - start) // 2
            node.left = self.construct(nums, start, mid)    # [start, mid]
            node.right = self.construct(nums, mid + 1, end) # [mid+1, end]
            if node.left:
                node.interval_sum += node.left.interval_sum
            if node.right:
                node.interval_sum += node.right.interval_sum
        else:
            node.interval_sum = nums[start] # same as nums[end]
        return node

    # 单点修改
    def modify(self, root, index, value):
        if root.start == index and root.end == index:
            root.interval_sum = value
            return

        mid = root.start + (root.end - root.start) // 2
        if root.start <= index <= mid: # [start, mid]
            self.modify(root.left, index, value)
        if mid < index <= root.end:    # [mid+1, end]
            self.modify(root.right, index, value)
        root.interval_sum = root.left.interval_sum + root.right.interval_sum

    # 区间查询
    # [start, end] 查询区间
    def query(self, root, start, end):
        if root.start == start and root.end == end:
            return root.interval_sum

        result = 0
        # mid 当前节点管辖区间
        mid = root.start + (root.end - root.start) // 2
        # 左右子树均存在查询区间的子区间
        if start <= mid < end:
            result += self.query(root.left, start, mid)
            result += self.query(root.right, mid + 1, end)
        elif start >= mid + 1: # mid [start, end], query right tree
            result += self.query(root.right, start, end)
        elif end <= mid: # [start, end] mid, query left tree
            result += self.query(root.left, start, end)
        return result


class IntervalSum:

    # 区间指的是下标区间
    def __init__(self, A):
        self.st = SegmentTree(A, 0, len(A) - 1) # [start, end]

    """ The sum from start to end """
    def query(self, start, end):
        return self.st.query(self.st.root, start, end)

    def modify(self, index, value):
        self.st.modify(self.st.root, index, value)

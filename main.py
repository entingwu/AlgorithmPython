# This is a sample Python script.
from BinarySearch.FindPeakElement import FindPeakElement
from BinarySearch.SearchInRotatedSortedArray import SearchInRotatedSortedArray
from TwoPointer.SortColors import SortColors

# Press ⌃R to execute it or replace it with your code.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # p0 = ValidPalindrome()
    # s = "A man, a plan, a canal: Panama"
    # #print(p0.is_palindrome(s))
    # print(p0.valid_palindrome("aba"))

    # Sort
    # p0_1 = SortIntegers()
    # a = [3, 2, 1, 4, 5]
    # p0_1.sort_integers(a)
    # print(a)

    # BinarySearch
    # p0_3 = BinarySearch()
    # nums = [1, 2, 2, 4, 5, 5]
    # target = 2
    # print(p0_3.findPosition(nums, target))

    # p0_4 = Searcha2DMatrix()
    # matrix = [[1,3,5,7], [10,11,16,20], [23,30,34,50]]
    # print(p0_4.search_matrix(matrix, 11))

    # p0_5 = SearchInRotatedSortedArray()
    # array = [4,5,1,2,3]
    # print(p0_5.search(array, 1))

    p0_6 = FindPeakElement()
    a = [1]
    print(p0_6.find_peak(a))

    # 56. Two Sum
    # p1_1 = TwoSum()
    # numbers = [2, 4, 6, 9]
    # target = 10
    # print(p1_1.two_sum_1(numbers, target))

    # 607. Two Sum
    # p1 = TwoSumDS()
    # p1.add(1)
    # p1.add(3)
    # p1.add(5)
    # p1.add(2)
    # print(p1.find(4))
    # print(p1.find(7))

    # p2 = TwoSumTwoPointers()
    # p2.add(1)
    # p2.add(3)
    # p2.add(5)
    # #p2.add(2)
    # print(p2.find(4))
    # print(p2.find(7))

    # 57. 3Sum
    # p3 = ThreeSum()
    # print(p3.three_sum([2, 7, 11, 15]))
    # print(p3.three_sum([-1, 0, 1, 2, -1, -4]))

    # p4 = TriangleCount()
    # print(p4.triangle_count([3, 4, 6, 7]))

    # p4_1 = SortColors()
    # nums = [3, 2, 2, 1, 4]
    # p4_1.sort_colors2(nums, 4)
    # print(nums)

    # p5 = ImplementQueueByLinkedList()
    # p5.enqueue(1)
    # p5.enqueue(2)
    # p5.enqueue(3)
    # print(p5.dequeue())
    # p5.enqueue(4)
    # print(p5.dequeue())

    # BFS
    # node1 = Node(1)
    # node2 = Node(2)
    # node3 = Node(3)
    # node1.neighbors.append(node2)
    # node1.neighbors.append(node3)
    # node4 = Node(4)
    # node5 = Node(5)
    # node2.neighbors.append(node4)
    # node2.neighbors.append(node5)
    # node6 = Node(6)
    # node7 = Node(7)
    # node3.neighbors.append(node6)
    # node3.neighbors.append(node7)
    # p6 = BFSTemplate()
    # p6.bfs(node1)

    # BinaryTreePaths
    # treeNode1 = TreeNode(1)
    # treeNode2 = TreeNode(2)
    # treeNode3 = TreeNode(3)
    # treeNode5 = TreeNode(5)
    # treeNode1.left = treeNode2
    # treeNode1.right = treeNode3
    # treeNode2.right = treeNode5
    # p7 = BinaryTreePaths()
    # paths = p7.binary_tree_paths(treeNode1)
    # print(paths)

    # CloneGraph
    # graphNode1 = UndirectedGraphNode(1)
    # graphNode2 = UndirectedGraphNode(2)
    # graphNode4 = UndirectedGraphNode(4)
    # graphNode1.neighbors.append(graphNode2)
    # graphNode1.neighbors.append(graphNode4)
    # graphNode2.neighbors.append(graphNode1)
    # graphNode2.neighbors.append(graphNode4)
    # graphNode4.neighbors.append(graphNode1)
    # graphNode4.neighbors.append(graphNode2)
    # p8 = CloneGraph()
    # p8.clone_graph(graphNode1)

    # NumberOfIslands
    # grid = [
    #     [1, 1, 0, 0, 0],
    #     [0, 1, 0, 0, 1],
    #     [0, 0, 0, 1, 1],
    #     [0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 1]
    # ]
    # p8_1 = NumberOfIslands()
    # print(p8_1.num_islands(grid))

    # Zombie in Matrix
    # p8_2 = ZombieInMatrix()
    # grid = [[0,1,2,0,0], [1,0,0,2,1], [0,1,0,0,0]]
    # print(p8_2.zombie(grid))

    # BinaryTreeVerticalOrderTraversal
    # treeNode3 = TreeNode(3)
    # treeNode9 = TreeNode(9)
    # treeNode20 = TreeNode(20)
    # treeNode15 = TreeNode(15)
    # treeNode7 = TreeNode(7)
    # treeNode3.left = treeNode9
    # treeNode3.right = treeNode20
    # treeNode20.left = treeNode15
    # treeNode20.right = treeNode7
    # p9 = BinaryTreeVerticalOrderTraversal()
    # results = p9.vertical_order(treeNode3)
    # for column_result in results:
    #     print(column_result)
    # p9_1 = BinaryTreeLevelOrderTraversal()
    # results = p9_1.level_order(treeNode3)
    # for level_result in results:
    #     print(level_result)

    # p9_1_2 = WallsAndGates()
    # rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    # print(p9_1_2.walls_and_gates(rooms))

    # InvertBinaryTree
    # treeNode1: TreeNode = TreeNode(1)
    # treeNode2 = TreeNode(2)
    # treeNode3 = TreeNode(3)
    # treeNode4 = TreeNode(4)
    # treeNode1.left = treeNode2
    # treeNode1.right = treeNode3
    # treeNode3.left = treeNode4
    # p9_1 = BinaryTreeLevelOrderTraversal()
    # p9_2 = InvertBinaryTree()
    # treeNode1 = p9_2.invert_binary_tree(treeNode1)
    # results = p9_1.level_order(treeNode1)
    # for level_result in results:
    #     print(level_result)
    # p9_3 = BinaryTreeLongestConsecutiveSequence()
    # treeNode1 = TreeNode(1)
    # treeNode2 = TreeNode(2)
    # treeNode3 = TreeNode(3)
    # treeNode4 = TreeNode(4)
    # treeNode5 = TreeNode(5)
    # treeNode0 = TreeNode(0)
    # treeNode4.right = treeNode5
    # treeNode3.right = treeNode4
    # treeNode3.left = treeNode2
    # treeNode1.right = treeNode3
    # print(p9_3.longest_consecutive(treeNode1))

    # DFS
    # Subsets
    # nums = [1, 2]
    # p10 = Subsets()
    # #print(p10.subsets(nums))
    # print(p10.subsets_bfs(nums))

    # Permutations
    # nums = [1, 2, 3]
    # p11 = Permutations()
    # print(p11.permute(nums))

    # LetterCombinationsOfPhoneNumber
    # p11_1 = LetterCombinationsOfPhoneNumber()
    # digits = "23"
    # print(p11_1.letter_combinations(digits))

    # kSumII
    # p11_2 = KSum()
    # array = [1, 2, 3, 4]
    # k = 2
    # target = 5
    # print(p11_2.k_sum_i_i(array, k, target))

    # NQueens
    # n = 4
    # p12 = NQueens()
    # print(p12.solve_n_queens(n))

    # LongestPalindromeSubstring
    # s = "abcdzdcab"
    # p13 = LongestPalindromeSubstring()
    # print(p13.longest_palindrome_3(s))

    # Memorization
    # p14 = Triangle()
    # triangle = [[2], [3,4], [6,5,7], [4,1,8,3]]
    # print(p14.minimum_total(triangle))

    # p14_1 = BashGame()
    # print(p14_1.can_win_bash(12))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

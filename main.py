# This is a sample Python script.
from TwoPointer.LongestSquareStreakInAnArray import LongestSquareStreakInAnArray

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

    # p0_6 = FindPeakElement()
    # print(p0_6.find_peak([1]))

    # p0_7 = WoodCut()
    # l = [4, 6, 7, 8]
    # k = 3
    # print(p0_7.wood_cut(l, k))

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

    # p4_2 = GrumpyBookstoreOwner()
    # customers = [1,0,1,2,1,1,7,5]
    # grumpy = [0,1,0,1,0,1,0,1]
    # x = 3
    # print(p4_2.max_satisfied(customers, grumpy, x))

    # p4_3 = PickApples()
    # A = [6, 1, 4, 6, 3, 2, 7, 4]
    # K, L = 3, 2
    # print(p4_3.pick_apples(A, K, L))
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
    # paths = p7.binary_tree_paths2(treeNode1)
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

    # p9_1_3 = TopologicalSort()
    # node0 = Node(0)
    # node1 = Node(1)
    # node2 = Node(2)
    # node3 = Node(3)
    # node0.neighbors.append(node1)
    # node0.neighbors.append(node2)
    # node1.neighbors.append(node3)
    # node2.neighbors.append(node3)
    # graph = {node0, node1, node2, node3}
    # print(p9_1_3.topSort(graph))
    # p9_1_3_1 = CourseSchedule()
    # preresquisites = [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]] # [[1,0], [2,0], [3,1], [3,2]]
    # print(p9_1_3_1.can_finish(10, preresquisites))
    #
    # p9_1_3_2 = SequenceReconstruction()
    # org = [1, 2, 3]
    # seqs = [[1,2], [1,3], [2,3]]
    # p9_1_3_2.sequence_reconstruction(org, seqs)

    # p9_1_4 = WordLadder()
    # dict = {"hot", "dot", "dog", "lot", "log"}
    # print(p9_1_4.ladder_length("hit", "cog", dict))

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
    # p9_2_1 = DiameterOfBinaryTree()
    # print(p9_2_1.diameter_of_binary_tree(treeNode1))
    # p9_2_2 = LongestPathOnTheTree()
    # n = 5
    # starts = [0, 0, 2, 2]
    # ends = [1, 2, 3, 4]
    # lens = [1, 2, 5, 6]
    # print(p9_2_2.longest_path(n, starts, ends, lens))
    # p9_2_3 = NaryTreePreorderTraversal()
    # node6 = Node(6, [])
    # node5 = Node(5, [])
    # node3 = Node(3, [node5, node6])
    # node1 = Node(1, [node3, Node(2, []), Node(4, [])])
    # print(p9_2_3.preorder(node1))

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

    # p9_4 = FlatternBinaryTreeToLinkedList()
    # treeNode1 = TreeNode(1)
    # treeNode2 = TreeNode(2)
    # treeNode3 = TreeNode(3)
    # treeNode1.left = treeNode2
    # treeNode1.right = treeNode3
    # p9_4.flatten(treeNode1)
    # p9_4.print(treeNode1)

    # p9_5 = KthSmallestElementInaBST()
    # treeNode1 = TreeNode(1)
    # treeNode2 = TreeNode(2)
    # treeNode3 = TreeNode(3)
    # treeNode1.left = None
    # treeNode1.right = treeNode2
    # print(p9_5.kth_smallest(treeNode1, 2))

    # p9_6 = AlienDictionary()
    # words = ["wrt", "wrf", "er", "ett", "rftt"]
    # print(p9_6.alien_order(words))

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

    # p11_1_1 = TravelingSalesmanProblem()
    # tuple = [[1,2,1], [2,3,2], [1,3,3]]
    # print(p11_1_1.min_cost(3, tuple))

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

    # p11_3 = StringPermutation()
    # str = "abb"
    # print(p11_3.string_permutation2(str))

    # p11_4 = CombinationSum()
    # candidates = [2, 2, 3]
    # target = 5
    # print(p11_4.combination_sum(candidates, target))

    # p11_5 = WordSearch()
    # boards = [["a", "t"], ["c", "d"]]
    # words = ["cat", "at"]
    # print(p11_5.word_search_i_i(boards, words))

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

    # p14_2 = WildcardMatching()
    # source = "aa"
    # pattern = "a*"
    # print(p14_2.is_match(source, pattern))

    # p14_3 = WordPattern()
    # pattern = "aba"
    # str = "redbluered"
    # print(p14_3.word_pattern_match(pattern, str))

    # p14_4 = WordBreak()
    # s = "lintcode"
    # dict = ["de","ding","co","code","lint"]
    # print(p14_4.word_break(s, dict))

    # p15 = Rehashing()
    # listNone9 = ListNode(9)
    # listNone21 = ListNode(21, listNone9)
    # listNone14 = ListNode(14)
    # hashTable = [None, listNone21, listNone14, None]
    # p15.rehashing(hashTable)

    # p15_1_1 = UniqueNumberOfOccurences()
    # arr = [1,2,2,1,1,3]
    # print(p15_1_1.uniqueOccurrences(arr))

    # p15_1 = UglyNumber()
    # print(p15_1.nth_ugly_number(7))

    # p15_2 = KClosestPoints()
    # points = [Point(4, 6), Point(4, 7), Point(4, 4), Point(2, 5), Point(1, 1)]
    # origin = Point(0, 0)
    # print(p15_2.k_closest(points, origin, 3))

    # p16 = Backpack()
    # m = 10
    # array = [3, 4, 8, 5]
    # p16.back_pack(m, array)

    # p16_1 = KnightShortestPath()
    # grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # print(p16_1.shortest_path2(grid))

    # Prefix Sum
    # p17_1 = SubarraySumEqualsToK()
    # nums = [3, 1, -1, 5, 7] #[2, 1, -1, 4, 2, -3]
    # k = 12 #3
    # print(p17_1.subarraySum([1], 0))

    # p17_2 = MaximumSubarray()
    # nums = [-2, 2, -3, 4, -1, 2, 1, -5, 3]
    # print(p17_2.max_sub_array([-1]))

    # p17_3 = ShortestSubarrayWithSumAtLeastK()
    # a = [5, -1, 2, 3, -2]
    # k = 8
    # print(p17_3.shortest_subarray(a, k))

    # p17_4 = MinimumSizeSubarraySum()
    # nums = [2, 3, 1, 2, 4, 3]
    # s = 7
    # print(p17_4.minimum_size(nums, s))

    #p18 = CircularSentence()
    #print(p18.isCircularSentence("eetcoda"))
    # p18_1 = DividePlayersIntoTeamsOfEqualSkill()
    # skill = [3, 2, 5, 1, 3, 4] # [2,1,5,2]
    # print(p18_1.dividePlayers([2, 2, 2, 2]))
    # p18_2 = MinimumScoreOfaPathBetweenTwoCities()
    # roads = [[1,2,9], [2,3,6], [2,4,5], [1,4,7]]
    # roads1 = [[1,2,2],[1,3,4],[3,4,7]]
    # n = 4
    # print(p18_2.minScore(n, roads))

    # Union Find
    # p19_1 = GraphValidTree()
    # edges = [[1,2], [1,3], [2,3]]
    # #print(p19_1.valid_tree(4, edges))
    # p19_1.addEdge(1, 2)
    # print(p19_1.isValidTree())
    # p19_1.addEdge(1, 3)
    # print(p19_1.isValidTree())
    # p19_1.addEdge(1, 5)
    # print(p19_1.isValidTree())
    # p19_1.addEdge(3, 5)
    # print(p19_1.isValidTree())

    p20_1 = LongestSquareStreakInAnArray()
    nums =  [4,3,6,16,8,2] # [2, 3, 5, 6, 7]
    print(p20_1.longestSquareStreak(nums))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

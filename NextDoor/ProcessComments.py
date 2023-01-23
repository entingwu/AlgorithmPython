import collections
from typing import List
class Comment:
    def __init__(self, id=None, parent_id=None):
        self.id = id
        self.parent_id = parent_id

class CommentNode:
    def __init__(self, id=None, children=None):
        self.id = id
        self.children = children

class ProcessComments:
    def flat_to_tree(self, comments: List[Comment]) -> List[CommentNode]:
        graph = collections.defaultdict(set)
        id_to_comment = {}
        for comment in comments:
            if comment.parent_id is not None:
                graph[comment.parent_id].add(comment.id)
                id_to_comment[comment.id] = comment
        print(graph)

        results = []
        for comment in comments:
            if comment.parent_id is None: # root
                root = self.dfs(graph, comment, id_to_comment)
                results.append(root)
        return results

    # Return the CommentNode which id is node.id, children is List[CommentNode]
    def dfs(self, graph, node, id_to_comment) -> CommentNode:
        if node.id not in graph: # leaf
            return CommentNode(node.id)

        children = set()
        for neighbor_id in graph[node.id]:
            neighbor = id_to_comment[neighbor_id]
            child = self.dfs(graph, neighbor, id_to_comment)
            children.add(child)
        return CommentNode(node.id, list(children))

    def print_tree(self, comment_nodes: List[CommentNode]):
        if comment_nodes is None:
            print("#")
            return
        for node in comment_nodes:
            print(node.id)
            self.print_tree(node.children)

    items = []
    def print_tree1(self, comment_nodes: List[CommentNode]):
        if comment_nodes is None:
            print(" ".join(self.items))
            return
        for node in comment_nodes:
            self.items.append(str(node.id))
            self.print_tree(node.children)
            self.items.pop()

    def flat_to_tree1(self, comments: List[Comment]) -> List[CommentNode]:
        parentToChildren = collections.defaultdict(set)
        roots = set()
        for comment in comments:
            id, parent_id = comment.id, comment.parent_id
            if parent_id is None:
                roots.add(id)
            else:
                parentToChildren[parent_id].add(id)

        results = []
        for parent_id, ids in parentToChildren.items():
            results.append(CommentNode(parent_id, ids))
        return results

    def print_tree2(self, comment_nodes: List[CommentNode]):
        queue = collections.deque(comment_nodes)
        visited = set()
        while queue:
            node = queue.popleft()
            print("%s" % node.id + " ")
            if node.children is None:
                print("#")
            else:
                for neighbor in node.children:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(node)

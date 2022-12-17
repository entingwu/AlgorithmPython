import functools

from UnionFind.UnionFind import UnionFind
'''
Definition for a Connection
'''

class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost

class MinimumSpanningTree:
    # 2. Prim
    def lowestCost(self, connections):
        name_to_id, id_to_name = {}, {}
        for connection in connections:
            if connection.city1 not in name_to_id:
                name_to_id[connection.city1] = len(name_to_id)
                id_to_name[len(id_to_name)] = connection.city1
            if connection.city2 not in name_to_id:
                name_to_id[connection.city2] = len(name_to_id)
                id_to_name[len(id_to_name)] = connection.city2

        n = len(name_to_id)
        graph = [[float('inf')] * n for _ in range(n)]
        edges = [[float('inf')] * n for _ in range(n)]
        for connection in connections:
            start = name_to_id[connection.city1]
            end = name_to_id[connection.city2]
            graph[start][end] = min(connection.cost, graph[start][end])
            graph[end][start] = min(connection.cost, graph[end][start])
            edges[start][end] = min(connection.cost, edges[start][end])
        print(graph)
        print(edges)

        mst, min_distance = [], [(0, 0)] * n
        visited = set([0])
        for i in range(1, n):
            min_distance[i] = (graph[0][i], 0) # 从0来的
        print(min_distance)

        for i in range(1, n):
            cost, next_node = float('inf'), -1
            for j in range(n):
                if j not in visited and cost > min_distance[j][0]:
                    next_node = j
                    cost = min_distance[j][0]
            if cost == float('inf'):
                return []

            visited.add(next_node)
            start, end = min_distance[next_node][1], next_node
            if edges[start][end] != float('inf') and edges[start][end] < edges[end][start]:
                mst.append(Connection(id_to_name.get(start), id_to_name.get(end), cost))
            if edges[end][start] != float('inf') and edges[end][start] < edges[start][end]:
                mst.append(Connection(id_to_name.get(end), id_to_name.get(start), cost))

            for j in range(n):
                if j not in visited and min_distance[j][0] > graph[next_node][j]:
                    min_distance[j] = (graph[next_node][j], next_node)

        mst.sort(key = functools.cmp_to_key(self.cmp))
        return mst




    # 1. Kruskal
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost1(self, connections):
        uf = UnionFind()
        for connection in connections:
            uf.add(connection.city1)
            uf.add(connection.city2)
        n = len(uf.father) # node
        m = len(connections) # edge
        connections.sort(key=functools.cmp_to_key(self.cmp))

        mst = []
        edges = 0
        for connection in connections:
            if edges == n - 1:
                break
            # 如果两点没有连在一起
            if not uf.is_connected(connection.city1, connection.city2):
                uf.merge(connection.city1, connection.city2)
                mst.append(connection)
                edges += 1
        if edges != n - 1:
            return []
        return mst


    def cmp(self, a, b):
        if a.cost != b.cost:
            if a.cost > b.cost:
                return 1
            return -1

        if a.city1 != b.city1:
            if a.city1 > b.city1:
                return 1
            return -1

        if a.city2 != b.city2:
            if a.city2 > b.city2:
                return 1
            return -1


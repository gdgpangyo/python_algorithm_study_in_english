"""
https://leetcode.com/problems/critical-connections-in-a-network/
1192. Critical Connections in a Network
Hard

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

"""

from collections import defaultdict

class Solution:

  def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
    def makeGraph():
      graph = defaultdict(list)
      for a,b in connections:
        graph[a].append(b)
        graph[b].append(a)
      return graph

    graph = makeGraph()
    connections = set(map(tuple,(map(sorted, connections))))
    rank = [-2] * n
    # print(connections)
    def dfs(node, depth):
      """
      node: traversing node
      depth: rank of the node
      """
      if rank[node] >= 0:
        return rank[node]

      rank[node] = depth
      min_depth = n

      for nei in graph[node]:
        if rank[nei] == depth -1:
          continue
        back_depth = dfs(nei, depth+1)
        if back_depth <= depth: # cycle found
          connections.discard(tuple(sorted((node, nei))))

        min_depth = min(min_depth, back_depth)

      return min_depth

    dfs(0,0)
    return list(connections)
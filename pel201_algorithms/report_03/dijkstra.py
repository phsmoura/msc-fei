from collections import defaultdict


class Node_Distance:
  def __init__(self, name, dist):
    self.name = name
    self.dist = dist


class Graph:
  def __init__(self, node_count):
    self.adj_list = defaultdict(list)
    self.node_count = node_count

  def add_into_adj_list(self, src, node_dist):
    self.adj_list[src].append(node_dist)

  def print_results(self, source, distance):
    for i in range(self.node_count):
      print(f"Source Node ({source})  -> Destination Node({i})  : {distance[i]}")

  def dijkstra(self, source=0, verbose=False):
    # init distance to the infinity and beyond
    distance = [999] * self.node_count
    distance[source] = 0

    priority_queue = {source: 0}

    while priority_queue:
      current_node = min(priority_queue, key=priority_queue.get)

      if verbose:
        print(f"Node to be explored: {priority_queue[current_node]}")

      del priority_queue[current_node]

      for node_dist in self.adj_list[current_node]:
        adjnode = node_dist.name
        weight = node_dist.dist

        if verbose:
          print(f"Node discovered: {adjnode} - cost: {weight}")

        # Edge relaxation
        if distance[adjnode] > distance[current_node] + weight:
          distance[adjnode] = distance[current_node] + weight
          priority_queue[adjnode] = distance[adjnode]

    self.print_results(source, distance)

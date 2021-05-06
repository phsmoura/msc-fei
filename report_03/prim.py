class Node:
  """Create current_node as an oject"""

  def __init__(self, arg_id):
    self._id = arg_id


class Graph:
  def __init__(self, source, adj_list):
    self.source = source
    self.adj_list = adj_list

  def prim(self, verbose=False):
    """
    Priority queue is implemented as a dict, using Node as a key

    param bool: if 'True', show messages about what this method is doing
    """
    min_span_tree_cost = 0
    priority_queue = {Node(self.source): min_span_tree_cost}
    added = [False] * len(self.adj_list)

    while priority_queue:
      current_node = min(priority_queue, key=priority_queue.get)
      cost = priority_queue[current_node]

      if verbose:
        print(f"Node to be explored: {priority_queue[current_node]}")

      del priority_queue[current_node]

      if not added[current_node._id]:
        min_span_tree_cost += cost
        added[current_node._id] = True

        for item in self.adj_list[current_node._id]:
          if verbose:
            print(f"Node discovered: {item[0]} - cost: {item[1]}")

          adjcurrent_node = item[0]
          adjcost = item[1]

          if added[adjcurrent_node] == False:
            priority_queue[Node(adjcurrent_node)] = adjcost

          if verbose:
            print(
              f"Added current_node ({adjcurrent_node}, {adjcost}) to priority queue"
            )

    return min_span_tree_cost

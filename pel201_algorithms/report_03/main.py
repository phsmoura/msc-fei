from prim import Graph as Prim
from dijkstra import Graph as Dijkstra
from dijkstra import Node_Distance

def _prim():
    # node: [(adjacent_node, cost)]
    graph = {
        0: [(1,1), (2,2), (3,1), (4,1), (5,2), (6,1)],
        1: [(0,1), (2,2), (6,2)],
        2: [(0,2), (1,2), (3,1)],
        3: [(0,1), (2,1), (4,2)],
        4: [(0,1), (3,2), (5,2)],
        5: [(0,2), (4,2), (6,1)],
        6: [(0,1), (2,2), (5,1)]
    }

    g1 = Prim(0, graph)
    cost = g1.prim()
    print(cost)

def _dijkstra():
    node_count = 6
    g1 = Dijkstra(node_count)

    # Node 0: <1,5> <2,1> <3,4>
    g1.add_into_adj_list(0, Node_Distance(1, 5))
    g1.add_into_adj_list(0, Node_Distance(2, 1))
    g1.add_into_adj_list(0, Node_Distance(3, 4))

    # Node 1: <0,5> <2,3> <4,8> 
    g1.add_into_adj_list(1, Node_Distance(0, 5))
    g1.add_into_adj_list(1, Node_Distance(2, 3))
    g1.add_into_adj_list(1, Node_Distance(4, 8))

    # Node 2: <0,1> <1,3> <3,2> <4,1>
    g1.add_into_adj_list(2, Node_Distance(0, 1))
    g1.add_into_adj_list(2, Node_Distance(1, 3))
    g1.add_into_adj_list(2, Node_Distance(3, 2))
    g1.add_into_adj_list(2, Node_Distance(4, 1))

    # Node 3: <0,4> <2,2> <4,2> <5,1>
    g1.add_into_adj_list(3, Node_Distance(0, 4))
    g1.add_into_adj_list(3, Node_Distance(2, 2))
    g1.add_into_adj_list(3, Node_Distance(4, 2))
    g1.add_into_adj_list(3, Node_Distance(5, 1))

    # Node 4: <1,8> <2,1> <3,2> <5,3>
    g1.add_into_adj_list(4, Node_Distance(1, 8))
    g1.add_into_adj_list(4, Node_Distance(2, 1))
    g1.add_into_adj_list(4, Node_Distance(3, 2))
    g1.add_into_adj_list(4, Node_Distance(5, 3))

    # Node 5: <3,1> <4,3> 
    g1.add_into_adj_list(5, Node_Distance(3, 1))
    g1.add_into_adj_list(5, Node_Distance(4, 3))

    g1.dijkstra(0,verbose=True)
    print("\n")
    g1.dijkstra(5)

if __name__ == "__main__":
    _prim()
    _dijkstra()

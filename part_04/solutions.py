from graph import Graph, degrees, out_degrees


# Solution for calculating the total degrees in a directed graph
def total_degrees(graph):
    """
    Return a dictionary of total degrees for each node in a
    directed graph.
    """
    if not graph.is_directed:
        raise ValueError("Cannot call total_degrees() on an undirected graph")

    # The total degree of a node is the same as the total number of
    # edges connected to that node. So you can get the total degree
    # by calling `degrees()` on an undirected graph with the same
    # nodes and edges as `graph`.
    undirected_graph = Graph(graph.nodes, graph.edges, is_directed=False)
    return degrees(undirected_graph)


# Solution #1 for calculating the in degrees of a directed graph
# This solution uses the `total_degrees()` function degined above.
# Although it works, it is not ideal because it calls both
# `total_degrees()` and `out_degrees()`, both of which end up calling
# `_degrees()`. In other words, it builds the adjacency list twice.


def in_degrees1(graph):
    """
    Return a dictionary of in degrees for each node in a
    directed graph
    """
    # Since total degree = in degree + out degree, you can calculate
    # the in degrees by subtracting the out degrees from the total
    # degrees for each node
    graph_total_degrees = total_degrees(graph)
    graph_out_degrees = out_degrees(graph)
    return {
        node: graph_total_degrees[node] - graph_out_degrees[node]
        for node in graph.nodes
    }


# Solution #2 for calculating the in degrees of a directed graph
def in_degrees2(graph):
    """
    Return a dictionary of in degrees for each node in a
    directed graph
    """
    # If you reverse the edges of a directed graph then out neighbors
    # in the reversed graph are in neighbors in the original graph.
    reversed_edges = [(node2, node1) for node1, node2 in graph.edges]
    reversed_graph = Graph(graph.nodes, reversed_edges, is_directed=True)
    return out_degrees(reversed_graph)


# ~~~~~~~~~~~~~~~~~ BONUS ~~~~~~~~~~~~~~~~~


def min_degree(graph):
    """Return the minimum degree of an undirected graph."""
    return min(degrees(graph).values())


def max_degree(graph):
    """Return the maximum degree of an undirected graph."""
    return max(degrees(graph).values())


def min_in_degree(graph):
    """Return the minimum in degree of a directed graph."""
    return min(in_degrees2(graph).values())


def max_in_degree(graph):
    """Return the maximum in degree of a directed graph."""
    return max(in_degrees2(graph).values())


def min_out_degree(graph):
    """Return the minimum out degree of a directed graph."""
    return min(out_degrees(graph).values())


def max_out_degree(graph):
    """Return the maximum out degree of a directed graph."""
    return max(out_degrees(graph).values())


def min_total_degree(graph):
    """Return the minimum total degree of a directed graph."""
    return min(total_degrees(graph).values())


def max_total_degree(graph):
    """Return the maximum total degree of a directed graph."""
    return max(total_degrees(graph).values())

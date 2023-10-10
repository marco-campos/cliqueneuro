import numpy as np
import networkx as nx
import math
import matplotlib.pyplot as plt

def generate_random_graph_matrix(N):
    """Generates the matrix for a complete graph with N-nodes 
    where the weights are randomly sampled from a uniform distribution.
    """
    b = np.random.uniform(0,1,size=(N,N))
    b_symm = (b + b.T)/2
        
    rows, cols = len(b_symm), len(b_symm[0])
    
    for i in range(rows):
        for j in range(cols):
            if i == j:  # Check if the current element is on the diagonal
                b_symm[i][j] = 1  # Set the diagonal element to 1
    return b_symm

def get_off_diagonal_entries(matrix):
    """Returns a dictionary for the weights of the graph where the keys are the 
    pairs of vertexes corresponding to the edges.
    """
    n = len(matrix)
    result_dict = {}

    for i in range(n):
        for j in range(i + 1, n):
            result_dict[(i, j)] = matrix[i][j]

    return result_dict

def get_edge_filtration(off_diagonal):
    """Returns a sorted list where the elements are tuples from the off-diagonal entries."""
    filtration = [(coords, value) for coords, value in off_diagonal.items()]
    
    # Sort the list of tuples based on the values
    filtration.sort(key=lambda x: x[1])
    return filtration

def find_cliques_recursive(G, nodes, d, start_node=None, curr_clique=None):
    """
    A recursive function to find cliques of size up to d.
    """
    if curr_clique is None:
        curr_clique = []
    if start_node is None:
        cliques = []
        for node in nodes:
            cliques += find_cliques_recursive(G, nodes, d, node, [node])
        return cliques
    else:
        cliques = [curr_clique]
        if len(curr_clique) < d:
            neighbors = list(set(G.neighbors(start_node)) & set(nodes))
            for neighbor in neighbors:
                if neighbor > start_node:  # Avoid duplicates
                    cliques += find_cliques_recursive(G, nodes, d, neighbor, curr_clique + [neighbor])
        return cliques

def cliques_up_to_d(G, d):
    """
    Find all cliques in the graph of size up to d.

    Parameters:
    - G: the input graph.
    - d: the maximum size of cliques to be returned.

    Returns:
    - A list of cliques (each clique is a list of nodes).
    """
    nodes = list(G.nodes())
    cliques = find_cliques_recursive(G, nodes, d)
    return [clique for clique in cliques if len(clique) <= d]

def get_betti_curve(persistence, dimension):
    betti_curve = []
    filtered_tuples = [(start, end) for dim, (start, end) in persistence if dim == dimension]

    if len(filtered_tuples) > 0:
        # Determine the overall time span for the plot
        min_start = min(start for start, _ in filtered_tuples)
        max_end = max(end if type(end) != float else 1 for _, end in filtered_tuples)  # Convert "inf" to 1
    
        num_points = max(1000, 2*len(filtered_tuples))
        # Create a range of x values for the plot
        x = np.linspace(0, 1, num_points)
        
        # Initialize the curve as an array of zeros
        curve = np.zeros_like(x)
        
        # Create step functions for each (start, end) range and sum them
        for start, end in filtered_tuples:
            curve += np.where((x >= start) & (x <= end), 1, 0)
    else:
        x, curve = [],[]
    return x, curve



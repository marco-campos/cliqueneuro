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



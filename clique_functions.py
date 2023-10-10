from graph_gen import * 
from visualize_tools import *

from simplicial import *

import math
import gudhi
from IPython.display import display, HTML
import matplotlib.pyplot as plt
from tqdm import tqdm


def generate_graph_filtration(edge_filtration):
    # Create an empty list to store the graphs
    graphs = []
    
    # Initialize an empty graph
    G = nx.Graph()
    
    for edge, value in edge_filtration:
        G.add_edge(*edge)
        graphs.append(G.copy())

    if len(graphs) != len(edge_filtration):
        raise ValueError("Sizes of graph and filtration don't match")
    
    graph_filtration = []
    
    for n, graph in enumerate(graphs):
        graph_filtration.append((edge_filtration[n][1], graph))
    return graph_filtration


def get_clique_complex_filtration(graph_filtration, N):
    clique_filtration = []
    
    for n, graph in enumerate(graph_filtration):
        current_cliques = nx.enumerate_all_cliques(graph[1])
        current_clique_simplices = []
        for clique in current_cliques:
            if len(clique)>2:
                current_clique_simplices.append(clique)
        clique_filtration.append((graph_filtration[n], current_clique_simplices))

    complex_filtration = []

    clique_complex = SimplicialComplex()
    
    for n in range(N):
        clique_complex.addSimplex(id=n)
    
    edges_used = []
    cliques_used = []
    
    for alpha_n in clique_filtration:
        edges = alpha_n[0][1].edges
        for edge in edges:
            if list(edge) in edges_used:
                pass
            else:
                clique_complex.addSimplexWithBasis(bs = list(edge))
                edges_used.append(list(edge))
        cliques = alpha_n[1]
        for clique in cliques:
            if list(clique) in cliques_used:
                pass
            else:
                # TODO Make this work for cliques of dimension 4 and higher.
                clique_complex.addSimplexWithBasis(bs =list(clique))
                cliques_used.append(list(clique))
        complex_filtration.append((alpha_n[0][0], clique_complex.copy()))
    return complex_filtration


def generate_betti_curve(complex_filtration):
    betti_curve = []

    for complex in complex_filtration:
        current_betti_numbers = complex[1].bettiNumbers()
        if len(current_betti_numbers) < 3:
            current_betti_numbers[2]=0
        betti_curve.append((complex[0],current_betti_numbers))
    return betti_curve

def gudhi_filtration(filtration, N):
    clique_filtration = []
    
    for n, graph in enumerate(filtration):
        current_cliques = cliques_up_to_d(graph[1], 4)
        current_clique_simplices = []
        for clique in current_cliques:
            if len(clique)>2 and len(clique)<5:
                current_clique_simplices.append(clique)
        clique_filtration.append((filtration[n], current_clique_simplices))

    print("Cliques Computed")

    st = gudhi.SimplexTree()
    edges_used = []
    cliques_used = []

    print("Building Clique Complex")
    
    for alpha_n in tqdm(clique_filtration):
        alpha = alpha_n[0][0]
        edges = alpha_n[0][1].edges
        
        for edge in edges:
            if list(edge) in edges_used:
                pass
            else:
                st.insert(list(edge), filtration = alpha)
                edges_used.append(list(edge))
        cliques = alpha_n[1]
        for clique in cliques:
            if list(clique) in cliques_used:
                pass
            else:
                st.insert(list(clique), filtration = alpha)
                cliques_used.append(list(clique))
    return st

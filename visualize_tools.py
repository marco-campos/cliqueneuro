import math
import matplotlib.pyplot as plt
from IPython.display import display, HTML

from graph_gen import *

def generate_ngon_points(n):
    """Generates the coordinates for points on an n-gon to aid with 
    visualization of the filtration"""
    if n < 3:
        raise ValueError("n must be at least 3 for an n-gon.")
    
    points = {}

    for i in range(n):
        angle = 2 * math.pi * i / n  # Calculate the angle for each point
        x = math.cos(angle)  # Calculate x-coordinate
        y = math.sin(angle)  # Calculate y-coordinate
        points[i] = (x, y)  # Add the point to the dictionary

    return points


def plot_betti_curves(test_betti):
    # Create a list of unique x-coordinates
    x_values = [x[0] for x in test_betti]
    
    # Initialize a color map for distinguishing curves
    color_map = plt.get_cmap('viridis')
    
    # Create a figure and axis
    fig, ax = plt.subplots()

    y0 = [y[1][0] for y in test_betti]
    y1 = [y[1][1] for y in test_betti]
    y2 = [y[1][2] for y in test_betti]

    # # Plot each curve with a unique color
    # for i, (alpha, y_values) in enumerate(test_betti):
    #     y = [y_values[1], y_values[2]]
    #     color = color_map(i / len(test_betti))  # Get a unique color
    #     label = f'Time = {alpha}'
    # ax.plot(x_values, y0, label="B0", color="blue")
    ax.plot(x_values, y1, label="B1", color="purple")
    ax.plot(x_values, y2, label="B2", color="red")

    # Set labels and legend
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Betti Curves')
    ax.legend()
    
    # Show the plot
    plt.show()


def vis_graphs(edge_filtration):
    
    # Create an empty list to store the graphs
    graphs = []
    
    # Initialize an empty graph
    G = nx.Graph()
    
    fixed_positions = generate_ngon_points(len(edge_filtration))
    
    for edge, value in edge_filtration:
        G.add_edge(*edge)
        # You can add optional visualization code here to display the graph at each step
        # nx.draw(G, with_labels=True)
        # plt.show()
        pos = fixed_positions 
        graphs.append(G.copy())
    
    num_graphs = len(edge_filtration)
    num_cols = min(num_graphs, 3)
    num_rows = (num_graphs + num_cols - 1) // num_cols
    
    fig, ax = plt.subplots(num_rows, num_cols, figsize=(15, 10))
    
    for i, (edge, value) in enumerate(edge_filtration):
        G.add_edge(*edge)
        graphs.append(G.copy())
    
        # Optional: Visualize the graphs
        row, col = divmod(i, num_cols)
        nx.draw(graphs[i], with_labels=True, pos=pos, ax=ax[row, col])
        ax[row, col].set_title(f"Graph {i+1}\nAlpha = {value:.2f}")
    
    # Remove empty subplots if there are fewer graphs than expected
    for i in range(num_graphs, num_rows * num_cols):
        fig.delaxes(ax.flat[i])
        
    plt.tight_layout()  # Ensure the graphs don't overlap
    plt.show()

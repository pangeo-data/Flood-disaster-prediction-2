from typing import List, Optional, Dict

from matplotlib.lines import Line2D

from variables import *

from pgmpy.models import BayesianModel
import networkx as nx
import matplotlib.pyplot as plt

__node_positions = {
    PER_UNIT_GDP: (10, 12), ELEVATION: (22, 12), RAINFALL_FREQUENCY: (30, 12), RIVER_DENSITY: (42, 12),
    POPULATION_DENSITY: (2, 9),
    ROAD_DENSITY: (10, 6), SLOPE: (22, 6), RAINFALL_AMOUNT: (34, 6),
    FLOOD: (22, 0)
}

__GREEN = 'green'
__WHITE = 'white'
__RED = 'RED'


def __plot_bayesian_network(model: BayesianModel, title: str, color_map: List[str] = None, legend: Optional[Dict] = None):
    plt.figure(figsize=(10, 6))

    node_names = {n: '\n'.join(n.split(' ')) for n in model.nodes()}

    if color_map is None:
        color_map = ['white'] * len(model.nodes)

    nx.draw(model, pos=__node_positions, node_size=5000, with_labels=True, labels=node_names,
            linewidths=1, node_color=color_map)

    # Set the color of the nodes edges as black
    ax = plt.gca()  # to get the current axis
    ax.collections[0].set_edgecolor('black')

    if legend is not None:
        ax.legend(legend['handles'], legend['labels'], prop={'size': 15}, loc='lower right')

    plt.title(title)

    plt.show()


def display_bayesian_network(model: BayesianModel):
    __plot_bayesian_network(model, "Flood Risk Bayesian Network")


def display_markov_blanket(model: BayesianModel, variable, markov_blanket):
    color_map = []
    legend = {
        'handles': [
            Line2D([0], [0], marker='o', color='black', label='Circle', markerfacecolor=__GREEN, markersize=15),
            Line2D([0], [0], marker='o', color='black', label='Circle', markerfacecolor=__RED, markersize=15)
        ],
        'labels': ['Selected variable', 'Markov blanket node']

    }
    for node in model.nodes:
        if node == variable:
            color_map.append(__GREEN)
        elif node in markov_blanket:
            color_map.append(__RED)
        else:
            color_map.append(__WHITE)

    __plot_bayesian_network(model, "Markov Blanket for variable: {}".format(variable), color_map, legend)

from Knapsack import knapsack
from allele_domain import allele_domain
from Item import item
from population import population
from visualizer import GAVisualizer
import os

import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.patches import Rectangle
# import matplotlib.gridspec as gridspec


MAX_WIDTH = 30  
MAX_HEIGHT = 20
MAX_PRICE = 5000
POPULATION_SIZE = 40

def main():
    shelf = allele_domain()
    # item(name, width, height, price)
    # add_item(item, quantity)
    shelf.add_item(item("k1", 20, 4, 338.984), 2)
    shelf.add_item(item("k2", 12, 17, 849.246), 6)
    shelf.add_item(item("k3", 20, 12, 524.022), 2)
    shelf.add_item(item("k4", 16, 7, 263.303), 9)
    shelf.add_item(item("k5", 3, 6, 113.436), 3)
    shelf.add_item(item("k6", 13, 5, 551.072), 3)
    shelf.add_item(item("k7", 4, 7, 86.166), 6)
    shelf.add_item(item("k8", 6, 18, 755.094), 8)
    shelf.add_item(item("k9", 14, 2, 223.516), 7)
    shelf.add_item(item("k10", 9, 11, 369.560), 5)
    print(shelf)

    # knapsack(width, height, max_price)
    environment = knapsack(MAX_WIDTH, MAX_HEIGHT, MAX_PRICE)
    
    # population(knapsack, shelf)
    pop = population(environment, shelf, POPULATION_SIZE)
    pop.evaluate()
    os.system('cls')
    print('INICIO TOTAL')
    pop.print_population()
    

    visualizer = pop.evolve(generations=5000, elite_size=4)
    
    # Plot final solution
    plt.figure(figsize=(15, 10))
    
    # Plot history
    history_fig = visualizer.plot_history()
    history_fig.savefig('evolution_history.png')
    
    # Plot best solution
    solution_fig = visualizer.plot_knapsack_solution(
        pop.chromossomes[0], 
        environment
    )
    solution_fig.savefig('best_solution.png')

    visualizer.compare_initial_final(environment)

    
    # Show interactive viewer if in Jupyter notebook
    try:
        visualizer.create_interactive_viewer(environment)
    except ImportError:
        print("Interactive viewer requires Jupyter notebook")
    
    plt.show()

if __name__ == "__main__":
    main()

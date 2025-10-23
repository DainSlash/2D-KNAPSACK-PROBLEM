import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.gridspec as gridspec

class GAVisualizer:
    def __init__(self):
        self.history = {
            'best_aptitude': [],
            'avg_aptitude': [],
            'best_price': [],
            'generation_best': []
        }
        
    def update_history(self, population, generation):
        aptitudes = [c.aptitude for c in population.chromossomes]
        best_aptitude = min(aptitudes)
        avg_aptitude = sum(aptitudes) / len(aptitudes)
        best_price = population.chromossomes[0].get_price()
        
        self.history['best_aptitude'].append(best_aptitude)
        self.history['avg_aptitude'].append(avg_aptitude)
        self.history['best_price'].append(best_price)
        self.history['generation_best'].append(population.chromossomes[0])

    def plot_knapsack_solution(self, chromossome, knapsack, generation=None):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Plot knapsack boundaries
        ax.add_patch(Rectangle((0, 0), knapsack.width, knapsack.height, 
                             fill=False, color='black', linewidth=2))
        
        # Plot items with random colors and labels
        colors = plt.cm.Set3(np.linspace(0, 1, len(chromossome.alleles)))
        for allele, color in zip(chromossome.alleles, colors):
            ax.add_patch(Rectangle((allele.x, allele.y), 
                                 allele.item.width, 
                                 allele.item.height,
                                 facecolor=color, 
                                 alpha=0.5,
                                 edgecolor='black'))
            # Add item name and price
            plt.text(allele.x + allele.item.width/2, 
                    allele.y + allele.item.height/2,
                    f'{allele.item.name}\n${allele.item.price:.0f}',
                    ha='center', va='center')

        ax.set_xlim(-1, knapsack.width + 1)
        ax.set_ylim(-1, knapsack.height + 1)
        ax.set_aspect('equal')
        title = f"Knapsack Solution"
        if generation is not None:
            title += f" - Generation {generation}"
        plt.title(title)
        plt.xlabel("Width")
        plt.ylabel("Height")
        return fig

    def plot_history(self):
        fig = plt.figure(figsize=(15, 10))
        gs = gridspec.GridSpec(2, 2)
        
        # Aptitude evolution
        ax1 = fig.add_subplot(gs[0, :])
        ax1.plot(self.history['best_aptitude'], 'g-', label='Best Aptitude')
        ax1.plot(self.history['avg_aptitude'], 'b--', label='Average Aptitude')
        ax1.set_title('Aptitude Evolution')
        ax1.set_xlabel('Generation')
        ax1.set_ylabel('Aptitude')
        ax1.legend()
        ax1.grid(True)
        
        # Price evolution
        ax2 = fig.add_subplot(gs[1, 0])
        ax2.plot(self.history['best_price'], 'r-')
        ax2.set_title('Best Solution Price Evolution')
        ax2.set_xlabel('Generation')
        ax2.set_ylabel('Price')
        ax2.grid(True)
        
        # Final statistics
        ax3 = fig.add_subplot(gs[1, 1])
        ax3.axis('off')
        stats = (
            f"Final Statistics:\n\n"
            f"Best Aptitude: {self.history['best_aptitude'][-1]:.2f}\n"
            f"Best Price: ${self.history['best_price'][-1]:.2f}\n"
            f"Improvement: {((self.history['best_aptitude'][0] - self.history['best_aptitude'][-1]) / self.history['best_aptitude'][0] * 100):.1f}%"
        )
        ax3.text(0.1, 0.5, stats, fontsize=12)
        
        plt.tight_layout()
        return fig

    def create_interactive_viewer(self, knapsack):
        from ipywidgets import interact, IntSlider
        
        def view_generation(generation):
            self.plot_knapsack_solution(
                self.history['generation_best'][generation],
                knapsack,
                generation
            )
            plt.show()
            
        interact(
            view_generation,
            generation=IntSlider(
                min=0,
                max=len(self.history['generation_best'])-1,
                step=1,
                description='Generation:'
            )
        )
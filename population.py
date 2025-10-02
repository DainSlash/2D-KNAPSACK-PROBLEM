from allele import allele
from chromossome import chromossome
import random

class population:
    def __init__(self, knapsack, shelf, population_size):
        self.environment = knapsack
        self.allele_domain = shelf
        self.population_size = population_size

        self.chromossomes = []
        self.generate_initial_population()

    def generate_initial_population(self):
        for _ in range(self.population_size):
            chromossome_alleles = []
            possible_items = self.allele_domain.get_items()
            for i in range(len(possible_items)):
                x = random.randint(0, self.environment.width - possible_items[i].width)
                y = random.randint(0, self.environment.height - possible_items[i].height)
                chromossome_alleles.append(allele(random.choice(possible_items), x, y))
                
            self.chromossomes.append(chromossome(chromossome_alleles))

    def print_population(self):
        for chromossome in self.chromossomes:
            chromossome.print_chromossome()
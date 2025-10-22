from allele import allele
from chromossome import chromossome
import random

MUTATION_RATE = 0.01

class population:
    def __init__(self, knapsack, shelf, population_size):
        self.environment = knapsack
        self.allele_domain = shelf
        self.population_size = population_size

        self.chromossomes = []
        self.generate_initial_population()
        
        self.population_apt = 0 
        self.population_probability = 0

    def evaluate(self):
        self.population_apt = 0
        self.population_probability = 0
        
        for chromossome in self.chromossomes:
            self.population_apt += chromossome.calculate_aptitude(self.environment)
        
        self.chromossomes.sort(key=lambda c: c.aptitude, reverse=False)
        
        for chromossome in self.chromossomes:    
            self.population_probability += chromossome.calculate_selection_probability_initial(self.population_apt)
        for chromossome in self.chromossomes:    
            chromossome.calculate_selection_probability_final(self.population_probability)

    

    def generate_initial_population(self):
        for _ in range(self.population_size):
            chromossome_alleles = []
            possible_items = self.allele_domain.get_items()
            for i in range(len(possible_items)):
                x = random.randint(0, self.environment.width - possible_items[i].width)
                y = random.randint(0, self.environment.height - possible_items[i].height)
                chromossome_alleles.append(allele(random.choice(possible_items), x, y))
                
            self.chromossomes.append(chromossome(chromossome_alleles))

    def roulette_selection(self):
        r = random.random()
        sum_prob = 0
        
        for chromossome in self.chromossomes:
            sum_prob += chromossome.selection_probability
            if sum_prob >= r:
                return chromossome
                
        return self.chromossomes[-1]

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, len(parent1.alleles)-1)
        
        child1_alleles = parent1.alleles[:crossover_point] + parent2.alleles[crossover_point:]
        child2_alleles = parent2.alleles[:crossover_point] + parent1.alleles[crossover_point:]
        
        return chromossome(child1_alleles), chromossome(child2_alleles)

    def mutate(self, chromossome):
        if random.random() < MUTATION_RATE:
            for allele in chromossome.alleles:
                allele.mutation(self.allele_domain.get_items(),
                                self.environment.height,
                                self.environment.width)
        return chromossome

    def elitism(self, elite_size):
        return self.chromossomes[:elite_size]

    def reproduce(self, new_population):
        while len(new_population) < self.population_size:
                parent1 = self.roulette_selection()
                parent2 = self.roulette_selection()
                
                if parent1 and parent2:
                    child1, child2 = self.crossover(parent1, parent2)
                    # child1 = self.mutate(child1)
                    # child2 = self.mutate(child2)
    
                    new_population.append(child1)
                    if len(new_population) < self.population_size:
                        new_population.append(child2)
        
        self.chromossomes = new_population


    def evolve(self, generations=100, elite_size=2):
        for generation in range(generations):
            elite = self.elitism(elite_size)
            new_population = []
            new_population.extend(elite)
            
            
            self.reproduce(new_population)
            
            self.evaluate()
            
            print(f"\nGeração {generation+1}")
            print(f"Melhor aptidão: {self.chromossomes[0].aptitude}")
            print(f"Melhor preço: {self.chromossomes[0].get_price()}")


    def print_population(self):
        for chromossome in self.chromossomes:
            chromossome.print_chromossome()
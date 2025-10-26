from allele import allele
from chromossome import chromossome
from visualizer import GAVisualizer

import random

MUTATION_RATE = 0.15
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
            self.population_apt += chromossome.calculate_aptitude(self.environment, self.allele_domain)
        
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
                normal_orientation = random.random() >= 0.5
                chromossome_alleles.append(allele(random.choice(possible_items), x, y, normal_orientation))
                
            self.chromossomes.append(chromossome(chromossome_alleles))

    def roulette_selection(self):
        r = random.random()
        sum_prob = 0
        
        for chromossome in self.chromossomes:
            sum_prob += chromossome.selection_probability
            if sum_prob >= r:
                # print(r)
                # print(sum_prob)
                # chromossome.print_chromossome()
                return chromossome
                
        return self.chromossomes[-1]

    def crossover(self, parent1, parent2):
        go_cross  = random.random()
        if go_cross < 0.80:
            crossover_point = random.randint(1, len(parent1.alleles)-2) ## -2? pega o index_final - 1 / index_final = (tamanho -1)
            
            child1_alleles = parent1.alleles[:crossover_point] + parent2.alleles[crossover_point:]
            child2_alleles = parent2.alleles[:crossover_point] + parent1.alleles[crossover_point:]
        else:
            child1_alleles = parent1.alleles[:]
            child2_alleles = parent2.alleles[:]
        
        return chromossome(child1_alleles), chromossome(child2_alleles)

    def mutate(self, chromossome):
        if random.random() < MUTATION_RATE:
            for allele in chromossome.alleles:
                allele.mutation(self.allele_domain.get_items(),
                                self.environment.height,
                                self.environment.width)
        return chromossome

    def elitism(self, elite_size):

        import pickle
        return [pickle.loads(pickle.dumps(chrom)) for chrom in self.chromossomes[:elite_size]]

    def reproduce(self, new_population):
        while len(new_population) < self.population_size:
            parent1 = self.roulette_selection()
            parent2 = self.roulette_selection()
            
            if parent1 and parent2:
                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)

                new_population.append(child1)
                if len(new_population) < self.population_size:
                    new_population.append(child2)
        
        self.chromossomes = new_population.copy()


    def evolve(self, generations=5000, elite_size=2):
        visualizer = GAVisualizer()
        for generation in range(generations):
            elite = self.elitism(elite_size)
            print(f"Populacao: {generation}")
            print("TAMANHO DA ELITE: ")
            print(len(elite))
            
            new_population = []
            new_population.extend(elite)
            print("\n\nNOVO POPULACAO: ELITE")
            for c in new_population:
                c.print_chromossome()
                print("\n")

            self.reproduce(new_population)
            #for c in set(self.chromossomes) - set(elite):
            #    c = self.mutate(c)

            self.evaluate()
            
            visualizer.update_history(self, generation)
            #self.print_population()
            print(f"Melhor aptidão: {self.chromossomes[0].aptitude}")
            print(f"Melhor preço: {self.chromossomes[0].get_price()}")
        self.print_population()
        return visualizer


    def print_population(self):
        for chromossome in self.chromossomes[::-1]:
            chromossome.print_chromossome()
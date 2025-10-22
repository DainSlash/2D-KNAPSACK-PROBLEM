impot random

def get_parents(population):
    # Seleciona dois cromossomos aleatórios da população como pais
    parent1 = random.choice(population.chromossomes)
    parent2 = random.choice(population.chromossomes)
    return parent1, parent2
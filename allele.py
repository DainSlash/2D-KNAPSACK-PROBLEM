import random
GEN_MUTATION_RATE = 0.2

class allele:
    def __init__(self, item, x, y):
        self.item = item
        self.x = x
        self.y = y
    
    def mutation(self, itens, max_height, max_width):
        mutation_rate = GEN_MUTATION_RATE
        mutated = False

        # Decide quais genes vão mutar
        mutate_item = random.random() < mutation_rate
        mutate_x = random.random() < mutation_rate
        mutate_y = random.random() < mutation_rate

        # Se nenhum gene foi escolhido para mutar, força a mutação de um aleatório
        if not (mutate_item or mutate_x or mutate_y):
             gene = random.choice(['item', 'x', 'y'])
             if gene == 'item':
                 mutate_item = True
             elif gene == 'x':
                 mutate_x = True
             else:
                 mutate_y = True

        if mutate_item:
            self.item = random.choice(itens)
        if mutate_x:
            self.x = random.randint(0, max_width - self.item.width)
        if mutate_y:
            self.y = random.randint(0, max_height - self.item.height)
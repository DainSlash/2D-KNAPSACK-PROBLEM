import random
GEN_MUTATION_RATE = 0.25

class allele:
    def __init__(self, item, x, y, orientation):
        self.item = item
        self.x = x
        self.y = y
        self.normal_orientation = orientation
    
    def get_width(self):
        return self.item.width if self.normal_orientation else self.item.height
    
    def get_height(self):
        return self.item.height if self.normal_orientation else self.item.width

    def mutation(self, itens, max_height, max_width):
        mutation_rate = GEN_MUTATION_RATE
        mutated = False

        # Decide quais genes vão mutar
        mutate_item = random.random() < mutation_rate
        mutate_x = random.random() < mutation_rate
        mutate_y = random.random() < mutation_rate
        mutate_orientation = random.random() < mutation_rate

        # Se nenhum gene foi escolhido para mutar, força a mutação de um aleatório
        if not (mutate_item or mutate_x or mutate_y or mutate_orientation):
             gene = random.choice(['item', 'x', 'y', 'normal_orientation'])
             if gene == 'item':
                 mutate_item = True
             elif gene == 'x':
                 mutate_x = True
             elif gene == 'y':
                 mutate_y = True
             elif gene == 'normal_orientation':
                 mutate_orientation = True

        if mutate_item:
            self.item = random.choice(itens)
            pass
        if mutate_x:
            self.x = random.randint(0, max_width - self.get_width())
            pass
        if mutate_y:
            self.y = random.randint(0, max_height - self.get_height())
        if mutate_orientation:
            self.normal_orientation = not self.normal_orientation
            pass
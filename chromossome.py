class chromossome:
    overlapping_area = 0
    real_area = 0
    density = 0
    
    fits_in_knapsack = True
    aptitude = 0
    selection_probability = 0.0

    def __init__(self, aleles):
        self.alleles = aleles


    def calculate_aptitude(self, knapsack):
        self.aptitude = 0
        self.aptitude = max(0, knapsack.max_price - self.get_price()) + (2 * max(0, self.get_price() - knapsack.max_price))
        return self.aptitude

    def calculate_selection_probability_initial(self, population_apt):
        self.selection_probability = 0.0

        if (self.aptitude > 0):
            self.selection_probability = ((1/self.aptitude)/population_apt) * 100
        else:
            self.selection_probability = 0.0

        return self.selection_probability
        

    def calculate_selection_probability_final(self, population_probability):
        if (population_probability > 0):
            self.selection_probability /= population_probability
        else:
            self.selection_probability = 0.0

        return self.selection_probability
        

    def get_price(self):
        return sum([allele.item.price for allele in self.alleles])
    
    def get_area(self):
        return sum([allele.item.get_area() for allele in self.alleles])
    
    def print_chromossome(self):
        # for allele in self.alleles:
        #     print(f"Item: {allele.item.name}, x: {allele.x}, y: {allele.y}, price: {allele.item.price}, area: {allele.item.get_area()}")
    
        print(f"Total price: {self.get_price()}, Total area: {self.get_area()}, Aptitude: {self.aptitude}, Selection Probability: {self.selection_probability}")
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
        # for allele in self.alleles:
        #     if (allele.x + allele.item.width <= knapsack.width) and (allele.y + allele.item.height <= knapsack.height):
        #         self.aptitude += allele.item.price
        return self.aptitude


    def get_price(self):
        return sum([allele.item.price for allele in self.alleles])
    
    def get_area(self):
        return sum([allele.item.get_area() for allele in self.alleles])
    
    def print_chromossome(self):
        for allele in self.alleles:
            print(f"Item: {allele.item.name}, x: {allele.x}, y: {allele.y}, price: {allele.item.price}, area: {allele.item.get_area()}")
        print(f"Total price: {self.get_price()}, Total area: {self.get_area()}")
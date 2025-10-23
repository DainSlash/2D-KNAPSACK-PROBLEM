OVELAPPING_WEIGHT = 98.2
OVERFLOW_WEIGHT = 100
EXCESS_ITEM_WEIGHT = 1000
PRICE_WEIGHT = 2
AREA_WEIGHT = 0.5
from math import log2

class chromossome:
    overlapping_area = 0
    real_area = 0
    density = 0
    
    fits_in_knapsack = True
    aptitude = 0
    selection_probability = 0.0

    def __init__(self, aleles):
        self.alleles = aleles

        self.overlapping_area = 0
        self.overflow_area = 0
        self.used_area = 0
        self.excess_items = 0
        self.fits_in_knapsack = True
        self.aptitude = 0
        self.selection_probability = 0.0

    def calculate_overlapping_area(self):
        self.overlapping_area = 0
        for i in range(len(self.alleles)):
            for j in range(i + 1, len(self.alleles)):
                x_overlap = max(0, 
                                min(self.alleles[i].x + self.alleles[i].item.width, self.alleles[j].x + self.alleles[j].item.width)
                                  - 
                                max(self.alleles[i].x, self.alleles[j].x))
                
                y_overlap = max(0, 
                                min(self.alleles[i].y + self.alleles[i].item.height, self.alleles[j].y + self.alleles[j].item.height)
                                 - 
                                max(self.alleles[i].y, self.alleles[j].y))
                
                self.overlapping_area += (x_overlap * y_overlap)
                
        #self.overlapping_area = (log2(self.overlapping_area) * self.overlapping_area)

        return self.overlapping_area

    def calculate_overflow_area(self, knapsack):
        self.overflow_area = 0
        for allele in self.alleles:
            x_overflow = max(0, (allele.x + allele.item.width) - knapsack.width)
            y_overflow = max(0, (allele.y + allele.item.height) - knapsack.height)
            
            self.overflow_area += (x_overflow * allele.item.height + 
                                 y_overflow * allele.item.width - 
                                 x_overflow * y_overflow)
        return self.overflow_area

    def check_quantity_constraints(self, allele_domain):
        self.excess_items = 0
        item_counts = {}
        
        for allele in self.alleles:
            item_name = allele.item.name
            item_counts[item_name] = item_counts.get(item_name, 0) + 1
        
        for item_name, count in item_counts.items():
            max_allowed = allele_domain.get_max_item_quantity(self.alleles[0].item)
            if count > max_allowed:
                self.excess_items += count - max_allowed
        
        return self.excess_items

    def calculate_used_area(self):
        self.used_area = sum(allele.item.get_area() for allele in self.alleles)
        return self.used_area

    def calculate_aptitude(self, knapsack, allele_domain):
        overlapping_penalty = (self.calculate_overlapping_area() * OVELAPPING_WEIGHT)
        overflow_penalty = (self.calculate_overflow_area(knapsack) * OVERFLOW_WEIGHT)
        excess_items_penalty = self.check_quantity_constraints(allele_domain) * EXCESS_ITEM_WEIGHT
        used_area = self.calculate_used_area()
        price_penalty = (max(0, self.get_price() - knapsack.max_price) + max(0, knapsack.max_price - self.get_price())) ** PRICE_WEIGHT
        
        area_utilization = used_area / knapsack.get_area()
        area_penalty = 0 #(1 - area_utilization) * knapsack.get_area() * AREA_WEIGHT
        
        self.aptitude = overlapping_penalty + overflow_penalty#(overlapping_penalty + 
                        #overflow_penalty + 
                        #excess_items_penalty + 
                        #price_penalty + 
                        #area_penalty)
        
        self.fits_in_knapsack = (overflow_penalty == 0 and 
                                overlapping_penalty == 0 and 
                                excess_items_penalty == 0 and
                                self.get_price() <= knapsack.max_price)
        
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
        print(f"Chromossome Status:")
        # print(f"Total price: ${self.get_price():.2f}")
        # print(f"Total area: {self.get_area():.2f}")
        # print(f"Overlapping area: {self.overlapping_area:.2f}")
        # print(f"Overflow area: {self.overflow_area:.2f}")
        # print(f"Excess items: {self.excess_items}")
        # print(f"Fits in knapsack: {self.fits_in_knapsack}")
        # print(f"Aptitude: {self.aptitude:.2f}")
        # print(f"Selection Probability: {self.selection_probability:.4f}")
        print(f"Total price: {self.get_price()}, Total area: {self.get_area()}, Aptitude: {self.aptitude}, Selection Probability: {self.selection_probability}")

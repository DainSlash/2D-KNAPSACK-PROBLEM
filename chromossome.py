OVERLAPPING_WEIGHT = 600
OVERFLOW_WEIGHT = 60.0
EXCESS_ITEM_WEIGHT = 10000
PRICE_WEIGHT = 50
DENSITY_WEIGHT = 80.0
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
                                min(self.alleles[i].x + self.alleles[i].get_width(), self.alleles[j].x + self.alleles[j].get_width())
                                  - 
                                max(self.alleles[i].x, self.alleles[j].x))
                
                y_overlap = max(0, 
                                min(self.alleles[i].y + self.alleles[i].get_height(), self.alleles[j].y + self.alleles[j].get_height())
                                 - 
                                max(self.alleles[i].y, self.alleles[j].y))
                
                self.overlapping_area += (x_overlap * y_overlap)
                
        #self.overlapping_area = (log2(self.overlapping_area) * self.overlapping_area)

        return self.overlapping_area

    def calculate_overflow_area(self, knapsack):
        self.overflow_area = 0
        for allele in self.alleles:
            x_overflow = max(0, (allele.x + allele.get_width()) - knapsack.width)
            y_overflow = max(0, (allele.y + allele.get_height()) - knapsack.height)
            
            self.overflow_area += (x_overflow * allele.get_height() + 
                                 y_overflow * allele.get_width() - 
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

    def calculate_total_area(self):
        self.used_area = sum(allele.item.get_area() for allele in self.alleles)
        return self.used_area

    def calculate_used_area(self, knapsack):
        if not self.alleles:
            self.used_area = 0
            return 0

        total_area = 0
        
        for allele in self.alleles:
            max_right = max((allele.x + allele.get_width()) for allele in self.alleles if allele.x >= 0 and allele.y >= 0)
            max_bottom = max((allele.y + allele.get_height()) for allele in self.alleles if allele.x >= 0 and allele.y >= 0)
            min_left = min(allele.x for allele in self.alleles if allele.x >= 0 and allele.y >= 0)
            min_top = min(allele.y for allele in self.alleles if allele.x >= 0 and allele.y >= 0)
            
            total_area = (max_right - min_left) * (max_bottom - min_top) if self.alleles else 0
            
            self.used_area = total_area
            return self.used_area


    def calculate_aptitude(self, knapsack, allele_domain):
        overlapping_penalty = self.calculate_overlapping_area() * OVERLAPPING_WEIGHT
        overflow_penalty = (self.calculate_overflow_area(knapsack) * OVERFLOW_WEIGHT)
        price_penalty = (max(0, self.get_price() - knapsack.max_price) + max(0, knapsack.max_price - self.get_price()))* PRICE_WEIGHT
        excess_items_penalty = self.check_quantity_constraints(allele_domain) * EXCESS_ITEM_WEIGHT

        
        used_area = self.calculate_used_area(knapsack)
        total_item_area = self.calculate_total_area()
        area_utilization = total_item_area / used_area
        density_penalty = max(0, (1 - area_utilization)) * DENSITY_WEIGHT * used_area * total_item_area
        
        self.fits_in_knapsack = (overflow_penalty == 0 and 
                                overlapping_penalty == 0 and 
                                excess_items_penalty == 0 and
                                self.get_price() <= knapsack.max_price)
        
        
        self.aptitude = (overlapping_penalty 
                        + overflow_penalty 
                        + price_penalty 
                        + excess_items_penalty 
                        + density_penalty)
        
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

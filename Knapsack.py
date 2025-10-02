class knapsack:
    def __init__(self, width, height, max_price):
        self.width = width
        self.height = height
        self.max_price = max_price
        

        self.ks = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

    def test_chromossome(self, chromossome):
        self.actual_value = sum([allele.item.price for allele in chromossome])
        
        pass


    def print_solution(self):
        self._print_items()
        print('='*self.width*3)
        self._print_ks_info()
        print('='*self.width*3)
        self._print_ks_matrix()


    def get_area(self):
        return self.height * self.width

    def _print_ks_info(self):
        print(f"Knapsack height: {self.height}, width: {self.width}, max value: {self.max_price}")
        print(f"Actual value: {self.actual_value}")
        print(f"Number of items: {len(self.items)}")
        print(f"Area: {self.get_area()}")

    def _print_ks_matrix(self):
        print("Knapsack matrix:")
        for row in self.ks:
            print(row)

    def _print_items(self):
        print("Items:")
        for item in self.items:
            print(f"{item.name}: height={item.height}, width={item.width}, price={item.price}") 
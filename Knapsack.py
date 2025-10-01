class knapsack:
    def __init__(self, height, width, items, max_value):
        self.height = height
        self.width = width
        self.items = items
        self.max_value = max_value
        self.actual_value = sum([item.price for item in items])
        

        self.ks = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

    def print_solution(self):
        self._print_items()
        print('='*self.width*3)
        self._print_ks_info()
        print('='*self.width*3)
        self._print_ks_matrix()


    def _print_ks_info(self):
        print(f"Knapsack height: {self.height}, width: {self.width}, max value: {self.max_value}")
        print(f"Actual value: {self.actual_value}")
        print(f"Number of items: {len(self.items)}")

    def _print_ks_matrix(self):
        print("Knapsack matrix:")
        for row in self.ks:
            print(row)

    def _print_items(self):
        print("Items:")
        for item in self.items:
            print(f"{item.name}: height={item.height}, width={item.width}, price={item.price}") 
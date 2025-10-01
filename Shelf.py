class shelf:
    def __init__(self):
        # Tupla (item, quantidade)
        self._items = []

    def add_item(self, item, quantity):
        if quantity <= 0:
            self._items.append((item, 1))
        self._items.append((item, quantity))

    def get_itens(self):
        return self._items

    def print_shelf(self):
        for item, quantity in self._items:
            print(f"{item} quantity={quantity}")
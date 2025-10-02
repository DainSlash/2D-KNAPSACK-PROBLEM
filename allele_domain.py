class allele_domain:
    def __init__(self):
        # Dicionário {item.name: (item, quantidade)}
        self._items = {}

    def add_item(self, item, quantity):
        if quantity <= 0:
            quantity = 1
        if item.name in self._items:
            current_quantity = self._items[item.name][1]
            self._items[item.name] = (item, current_quantity + quantity)
        self._items[item.name] = (item, quantity)

    def get_max_item_quantity(self, item):
        if item.name in self._items:
            return self._items[item.name][1]
        return 0

    def get_items(self):
        return [item for item, _ in self._items.values()]

    def __str__ (self):
        result = "Allele Domain:\n"
        for name, (item, quantity) in self._items.items():
            result += f"{item} quantity={quantity}\n"
        return result
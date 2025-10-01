class item:
    def __init__(self, name, height, width, price):
        self.name = name
        self.height = height
        self.width = width
        self.price = price
    
    def __str__ (self):
        return f"{self.name}: height={self.height}, width={self.width}, price={self.price}"
class item:
    def __init__(self, name, width, height, price):
        self.name = name
        self.width = width
        self.height = height
        self.price = price
    
    def get_area(self):
        return self.height * self.width

    def __str__ (self):
        return f"{self.name}: height={self.height}, width={self.width}, area={self.get_area()}, price={self.price}"
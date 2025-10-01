from Knapsack import knapsack
from Item import item
from Shelf import shelf

def main():
    s = shelf()
    # item(name, height, width, price)
    # add_item(item, quantity)
    s.add_item(item("k1", 4, 20, 338.984), 2)
    s.add_item(item("k2", 17, 12, 849.246), 6)
    s.add_item(item("k3", 12, 20, 524.022), 2)
    s.add_item(item("k4", 7, 16, 263.303), 9)
    s.add_item(item("k5", 6, 3, 113.436), 3)
    s.add_item(item("k6", 5, 13, 551.072), 3)
    s.add_item(item("k7", 7, 4, 86.166), 6)
    s.add_item(item("k8", 18, 6, 755.094), 8)
    s.add_item(item("k9", 2, 14, 223.516), 7)
    s.add_item(item("k10", 11, 9, 369.560), 5)
    s.print_shelf()


    # height, width, shelf, max_value
    # ks = knapsack(20, 20, shelf, 500)
    # ks.print_solution()

if __name__ == "__main__":
    main()
def evaluate(population, MAX_PRICE):
    apt_sum = 0
    minsum = 0
    
    for chromossome in population.chromossomes:
        #aptitude tende a 0
        # Penaliza++ se ultrapassar o preço máximo
        chromossome.aptitude = max(0, MAX_PRICE - chromossome.get_price()) + (2 * max(0, chromossome.get_price() - MAX_PRICE))
        apt_sum += chromossome.aptitude
    
    population.chromossomes.sort(key=lambda c: c.aptitude, reverse=False)
    for chromossome in population.chromossomes:
        if(chromossome.aptitude > 0):
            chromossome.selection_probability = ((1/chromossome.aptitude)/ apt_sum)*100
        else:
            chromossome.selection_probability = 0.0
        minsum = minsum + chromossome.selection_probability

    print("\nChromossome:")
    for chromossome in population.chromossomes:
        if(minsum > 0):
            chromossome.selection_probability = chromossome.selection_probability / minsum
        else:
            chromossome.selection_probability = 0.0
        print(f"Price: {chromossome.get_price()}\nAptitude: {chromossome.aptitude}\nSelection Probability: {chromossome.selection_probability}\n")

    return population
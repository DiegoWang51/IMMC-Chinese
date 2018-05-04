import fitness
import random
import copy
import matplotlib.pyplot as plt
import matplotlib.font_manager as fonter
myfont = fonter.FontProperties(fname="Songti.ttc")

def initPopulation(size, length):
    
    population = []
    peak = 1.322
    flat = 0.832
    valley = 0.369
    highest = 3.22
    
    for i in range(size):
        levels = [1 for i in range(8)]+[2 for i in range(8)]+[3 for i in range(8)]
        individual = []
        for j in range(length):
            pfv = levels.pop(random.randrange(len(levels)))
            if pfv == 1: # peak
                individual.append(random.uniform(peak, highest))
            elif pfv == 2: # flat
                individual.append(random.uniform(flat, highest))
            elif pfv == 3: # valley
                individual.append(random.uniform(valley, highest))  
        population.append(individual)
    return population

def crossOver(individualA, individualB):
    newIndividual = []
    for i in range(len(individualA)):
##        if random.randint(0, 1) == 0:
##            newIndividual.append(individualA[i])
##        else:
##            newIndividual.append(individualB[i])
        newIndividual.append(random.uniform(individualA[i], individualB[i]))
    return newIndividual


populationN = 24 # number of features (genes) in an individual (24)
populationM = 200 # number of individuals in the population (100)
elitePercentage = 0.1
iterTimes = 40

population = initPopulation(populationM, populationN)

for iterTime in range(iterTimes):
    
    # sort using the fitness function
    population.sort(key=fitness.fitness, reverse=True)
    
    # select the best individuals
    elites = copy.deepcopy(population[:int(elitePercentage*populationM)])

    # crossover
    population = copy.deepcopy(elites)
    while len(population) < populationM:
        # randomly select two individual from a the population to make one new
        newIndividual = crossOver(*random.sample(population, 2))
        population.append(newIndividual)

    # mutation
    for individual in population:
        if random.random() < 0.9: continue
        randomIndex = random.randint(0, populationN-1)
        individual[randomIndex] += random.uniform(-0.1, 0.1)

    # sort using the fitness function, again
    population.sort(key=fitness.fitness, reverse=True)

##    print(fitness.fitness(population[0]))

population.sort(key=sum)
plt.plot([i for i in range(1, 25)], population[0])
plt.show()

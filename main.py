import numpy
from deap import base, algorithms, creator, tools
import random
import matplotlib.pyplot as plt
import numpy as np
import forShortestWay
import graph_show


cntVertex = 31
start = 0
end = 29
# end = random.randint(1, cntVertex+1)
minDistance = 1
maxDistance = 20
pointInLayer = 3
LENGTH_CHROM = cntVertex

inf = 1000000
pInf = 0.5
POPULATION_SIZE = 1000
P_CROSSOVER = 0.9
P_MUTATION = 0.3
MAX_GENERATIONS = 30
HALL_OF_FAME_SIZE = 1

hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

# vertex, distances = forShortestWay.initMatrix(length=LENGTH_CHROM,
#                                               pInf=pInf,
#                                               inf=inf,
#                                               minDistance=minDistance,
#                                               maxDistance=maxDistance)
vertex, distances = forShortestWay.pointInint(length=LENGTH_CHROM,
                                              pInf=pInf,
                                              inf=inf,
                                              minDistance=minDistance,
                                              maxDistance=maxDistance,
                                              cntPoint=pointInLayer)

# print(vertex)
# print(distances)

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("randomOrder", random.sample, range(LENGTH_CHROM), LENGTH_CHROM)
toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.randomOrder, 1)
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)

population = toolbox.populationCreator(n=POPULATION_SIZE)

def dikstryFitness(individual):
    summ = 0
    ind = individual[0]
    s = min(start, end)
    e = max(start, end)
    first_index = s
    for i in ind:
        distance = distances[first_index][i]
        summ += distance
        first_index = i
        if i == e:
            break
    return summ,


def cxOrdered(ind1, ind2):
    tools.cxOrdered(ind1[0], ind2[0])

    return ind1, ind2


def mutShuffleIndexes(individual, indpb):
    first_index = start
    index = 0
    for _ in range(sum(range(LENGTH_CHROM))):
        if index == LENGTH_CHROM:
            break
        v = individual[0][index]
        distance = distances[first_index][v]
        if distance == inf:
            individual[0].insert(LENGTH_CHROM-1, individual[0].pop(individual[0].index(v)))
        else:
            first_index = v
            index += 1
    tools.mutShuffleIndexes(individual[0], indpb)

    return individual,


toolbox.register("evaluate", dikstryFitness)
toolbox.register("select", tools.selTournament, tournsize=10)
toolbox.register("mate", cxOrdered)
toolbox.register("mutate", mutShuffleIndexes, indpb=1.0/LENGTH_CHROM/10)

stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("min", np.min)
stats.register("mean", np.mean)

population, logbook = algorithms.eaSimple(population, toolbox,
                                          cxpb=P_CROSSOVER,
                                          halloffame=hof,
                                          mutpb=P_MUTATION,
                                          ngen=MAX_GENERATIONS,
                                          stats=stats,
                                          verbose=True)

maxFitnessValues, meanFitnessValues = logbook.select("min", "mean")

best = hof.items[0]
print(best[0])
# print(distances)

plt.plot(maxFitnessValues, color='red')
plt.plot(meanFitnessValues, color='green')
plt.xlabel('Поколение')
plt.ylabel('Макс/средняя приспособленность')
plt.title('Зависимость максимальной и средней приспособленности от поколения')

plt.show()

fig, ax = plt.subplots()
graph_show.show_graph(ax=ax,
                      vertex=vertex,
                      distances=distances,
                      best=best[0],
                      start=start,
                      end=end,
                      inf=inf)
plt.show()

def create_schedule():
    from DisplayData import DisplayData
    from Population import Population
    from GeneticAlgorithm import GeneticAlgorithm
    from Data import Data
    import time
    import random as rnd
    import sqlite3
    import collections
    from insert_values_db import insert_schedules

    POPULATION_SIZE = 20

    data = Data()
    displayMgr = DisplayData(data)
    displayMgr.print_available_data()
    generationNumber = 0
    print("\n> Generation # " + str(generationNumber))
    population = Population(POPULATION_SIZE, data)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    displayMgr.print_generation(population)
    geneticAlgorithm = GeneticAlgorithm(data=data)
    start_time = time.time()
    while population.get_schedules()[0].get_fitness() != 1.0:
        generationNumber += 1
        print("\n> Generation # " + str(generationNumber))
        population = geneticAlgorithm.evolve(population)
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    print("\n\n")
    print("--- %.2f seconds ---" % (time.time() - start_time))

    insert_schedules(population.get_schedules()[0])

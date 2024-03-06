# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:24:15 2022

@author: agademer & tdrumond

Template for exercise 1
(genetic algorithm module specification)
"""

import random as rd
import cities as ct #Importing the cities module

class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm 

        Args:
            chromosome (list[]): a list representing the individual's chromosome
            fitness (float): the individual's fitness (the higher, the better the fitness)
        """
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""
        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'


class GASolver:
    def __init__(self, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []

    def reset_population(self, pop_size=50):
        """Creates a new population
        
        Args:
            pop_size(int, optional): Size of the population. Defaults to 50.
        """
        for i in range(pop_size): #Creating pop_size different individuals
            chromosome = ct.default_road(city_dict)
            rd.shuffle(chromosome)
            fitness = - ct.road_length(city_dict, chromosome)
            new_individual = Individual(chromosome, fitness) #Creating a new individual with chromosome and fitness
            self._population.append(new_individual) #Adding it to the population
        pass  
    def evolve_for_one_generation(self):
        """ Apply the process for one generation : 
            -	Sort the population (Descending order)
            -	Selection: Remove x% of population (less adapted)
            -   Reproduction: Recreate the same quantity by crossing the 
                surviving ones 
            -	Mutation: For each new Individual, mutate with probability 
                mutation_rate i.e., mutate it if a random value is below   
                mutation_rate
        """
        
        #Sort the population
        """min = self._population[0].fitness
        for i in range(len(self._population)):
            for j in range(len(self._population)-i-1):
                if   self._population[j].__lt__(self._population[j+1]): ##C: Checking if j individual fits less than j+1 one##
                    self._population[j], self._population[j+1] = self._population[j+1], self._population ##C: Then swap them if its the case##"""
        
        self._population.sort(reverse=True)
        
        #Selection
        popped_out = int(self._selection_rate*len(self._population)) #The number of individual to pop
        for i in range(popped_out):
            self._population.pop() ##Supressing the last element of the array popped_out times 
        
        ##Reproduction: we need to create popped_out new elements that are merge of fittest individuals in the population
        #we don't choose our parents randomly, we decide to take the best individuals to generate childs so it's more efficient
        new_born_counter = 0
        while new_born_counter != popped_out:
            for i in range(len(self._population)):
                for j in range(len(self._population)-i-1):
                    if i != j and new_born_counter<popped_out:
                        #Crossover
                        crossover_point = len(self._population[0].chromosome) // 2

                        #Take the first half from the first parent
                        cross_chromosome = self._population[i].chromosome[:crossover_point]

                        # Take the second half from the second parent, skipping any cities already present in the child
                        for city in self._population[j].chromosome[crossover_point:]:
                            if city not in cross_chromosome:
                                cross_chromosome.append(city)
                        
                        # Handle the case where the chromosome size is reduced by crossover
                        if len(cross_chromosome) < len(self._population[i].chromosome):
                            possible_cities = ct.default_road(city_dict)
                            for city in possible_cities:
                                if city not in cross_chromosome:
                                    cross_chromosome.append(city)
 
                        ##Mutation##
                        if rd.random() < self._mutation_rate:
                            #define randomly the positions of the cities to swap
                            position1 = rd.randint(0, len(cross_chromosome)-1)
                            position2 = rd.randint(0, len(cross_chromosome)-1)

                            #swap the cities
                            temp = cross_chromosome[position1]
                            cross_chromosome[position1] = cross_chromosome[position2]
                            cross_chromosome[position2] = temp
                        
                        cross_fitness = - ct.road_length(city_dict, cross_chromosome)
                        new_cross_individual = Individual(cross_chromosome, cross_fitness)
                        self._population.append(new_cross_individual)
                        new_born_counter += 1

    def show_generation_summary(self):
        """ Print some debug information on the current state of the population """
        print("Generation summary:")
        print(f"Current population: {self._population}")
        print(f"Population size: {len(self._population)}")
        print(f"Best individual: {self.get_best_individual()}")
        print(f"Best fitness score: {self.get_best_individual().fitness}")

    def get_best_individual(self):
        """ Return the best Individual of the population """
        self._population.sort(reverse=True)
        return (self._population[0])

    def evolve_until(self, max_nb_of_generations=500, threshold_fitness=None):
        """ Launch the evolve_for_one_generation function until one of the two condition is achieved : 
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        nb_of_generation = 0
        while (threshold_fitness and self.get_best_individual().fitness < threshold_fitness) or nb_of_generation < max_nb_of_generations:
            self.evolve_for_one_generation()
            nb_of_generation += 1



city_dict = ct.load_cities('cities.txt') #create the list of cities that is in the text file
solver = GASolver()
solver.reset_population()
solver.evolve_until()

best = solver.get_best_individual()
ct.draw_cities(city_dict, best.chromosome)

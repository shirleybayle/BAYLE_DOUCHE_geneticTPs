# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:24:15 2022

@author: agademer & tdrumond

Template for exercise 1
(genetic algorithm module specification)
"""

import random as rd
import mastermind as mm ##C: Importing the mastermind module##
MATCH = mm.MastermindMatch(secret_size=4) ##C: Selecting the mastermind match to find##


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
        ##C: Adding the population creation##
        for i in range(pop_size): ##C: Creating pop_size different individuals##
            chromosome = MATCH.generate_random_guess()
            fitness = MATCH.rate_guess(chromosome)
            new_individual = Individual(chromosome, fitness) ##C: Combining fitness + chromosome in indiv##
            self._population.append(new_individual) ##C: Adding them to the population##
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
        
        ##C: Sort the population##
        min = self._population[0].fitness
        for i in range(len(self._population)):
            for j in range(len(self._population)-i-1):
                if   self._population[j].__lt__(self._population[j+1]): ##C: Checking if j individual fits less than j+1 one##
                    self._population[j], self._population[j+1] = self._population[j+1], self._population ##C: Then swap them if its the case##
        
        ##C:Selection##
        popped_out = int(self._selection_rate*len(self._population)) ##C: The number of individual to pop##
        for i in range(popped_out):
            self._population.pop() ##Supressing the last element of the array popped_out times ##
        ##Reproduction: we need to create popped_out new elements that are merge of fittest individuals in the population,
        ## Our first idea is to create an Alpha Male, the fittest individuals will inseminate a certain portion of individual, giving it first half to the 2nd best individuals, then the third etc...##
        new_born_counter = 0
        while new_born_counter != popped_out:
            for i in (len(self._population)):
                for j in (len(self._population)-i-1):
                    if i != j:
                        cross_chromosome = [self._population[i].chromosome[0],self._population[i].chromosome[1],self._population[j].chromosome[2],self._population[j].chromosome[3]]
                        ##Mutation##
                        if rd.random() < self._mutation_rate:
                            cross_chromosome[rd.randint(0,3)] = (mm.get_possible_colors())[rd.randint(0,len(mm.get_possible_colors))-1]
                        
                        
                        cross_fitness = MATCH.rate_guess(cross_chromosome)
                        new_cross_individual = Individual(cross_chromosome, cross_fitness)
                        self._population.append(new_cross_individual)
                        new_born_counter += 1






                

        pass  # REPLACE WITH YOUR CODE

    def show_generation_summary(self):
        """ Print some debug information on the current state of the population """
        pass  # REPLACE WITH YOUR CODE

    def get_best_individual(self):
        """ Return the best Individual of the population """
        pass  # REPLACE WITH YOUR CODE

    def evolve_until(self, max_nb_of_generations=500, threshold_fitness=None):
        """ Launch the evolve_for_one_generation function until one of the two condition is achieved : 
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        pass  # REPLACE WITH YOUR CODE

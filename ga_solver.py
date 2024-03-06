# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(generic genetic algorithm module)
"""
import random as rd


class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm

        Args:
            chromosome (list[]): a list representing the individual's
            chromosome
            fitness (float): the individual's fitness (the higher the value,
            the better the fitness)
        """
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""
        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'


class GAProblem:
    """Defines a Genetic algorithm problem to be solved by ga_solver"""
    def __init__(self):
        """Initiates the problem (add any argument useful for your specific problem)"""
        pass
    
    def compute_fitness(self, chrom):
       """Computes the fitness of a chromosome given"""
       pass

    def generate_chromosome(self):
        """Generates a chromosome"""
        pass
    
    def generate_crossed_chromosome(self, parent1, parent2):
        """Generates a child chromosome from two parents"""
        pass
        
    def generate_mutant(self, chromosome):
        """Generates a mutation for the chromosome given"""
        pass


class GASolver:
    def __init__(self, problem: GAProblem, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            problem (GAProblem): GAProblem to be solved by this ga_solver
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._problem = problem
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []

    def reset_population(self, pop_size=50):
        """ Initialize the population with pop_size random Individuals """
        for i in range(pop_size): #Creating pop_size different individuals
            chromosome = self._problem.generate_chromosome()
            fitness = self._problem.compute_fitness(chromosome)
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
        self._population.sort(reverse=True)
        
        #Selection
        popped_out = int(self._selection_rate*len(self._population)) #The number of individual to pop
        for i in range(popped_out):
            self._population.pop() ##Supressing the last element of the array popped_out times 
        
        #Reproduction
        #we don't choose our parents randomly, we decide to take the best individuals to generate childs so it's more efficient
        new_born_counter = 0
        while new_born_counter != popped_out:
            for i in range(len(self._population)):
                for j in range(len(self._population)-i-1):
                    if i != j and new_born_counter<popped_out:
                        #Reproduction
                        cross_chromosome = self._problem.generate_crossed_chromosome(self._population[i].chromosome, self._population[j].chromosome)
                        
                        ##Mutation##
                        if rd.random() < self._mutation_rate:
                            cross_chromosome = self._problem.generate_mutant(cross_chromosome)
                        
                        cross_fitness = self._problem.compute_fitness(cross_chromosome)
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

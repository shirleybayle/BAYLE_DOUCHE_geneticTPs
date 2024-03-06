# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving TSP example)
"""
from ga_solver import GAProblem
import cities
import random as rd

class TSProblem(GAProblem):
    """Implementation of GAProblem for the traveling salesperson problem"""
    
    def __init__(self, city_dict):
        """Initiates the dictionary of cities to connect"""
        self._city_dict = city_dict
    
    def compute_fitness(self, chrom):
        """Computes the fitness of a chromosome given"""
        fitness = - cities.road_length(city_dict, chrom)
        return fitness

    def generate_chromosome(self):
        """Generates a chromosome"""
        chromosome = cities.default_road(city_dict)
        rd.shuffle(chromosome)
        return chromosome
    
    def generate_crossed_chromosome(self, parent1, parent2):
        """Generates a child chromosome from two parents"""
        #Crossover
        crossover_point = len(parent1) // 2

        #Take the first half from the first parent
        cross_chromosome = parent1[:crossover_point]

        # Take the second half from the second parent, skipping any cities already present in the child
        for city in parent2[crossover_point:]:
            if city not in cross_chromosome:
                cross_chromosome.append(city)
                        
        # Handle the case where the chromosome size is reduced by crossover
        if len(cross_chromosome) < len(parent1):
            possible_cities = cities.default_road(city_dict)
            for city in possible_cities:
                if city not in cross_chromosome:
                    cross_chromosome.append(city)

        return cross_chromosome
        
    def generate_mutant(self, chromosome):
        """Generates a mutation for the chromosome given"""
        #define randomly the positions of the cities to swap
        position1 = rd.randint(0, len(chromosome)-1)
        position2 = rd.randint(0, len(chromosome)-1)

        #swap the cities
        temp = chromosome[position1]
        chromosome[position1] = chromosome[position2]
        chromosome[position2] = temp

        return chromosome




if __name__ == '__main__':

    from ga_solver import GASolver

    city_dict = cities.load_cities("cities.txt")
    problem = TSProblem(city_dict)
    solver = GASolver(problem)
    solver.reset_population()
    solver.evolve_until()
    cities.draw_cities(city_dict, solver.get_best_individual().chromosome)

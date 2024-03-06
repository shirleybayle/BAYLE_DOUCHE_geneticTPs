# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving Mastermind example)
"""
from ga_solver import GAProblem
import mastermind as mm
import random as rd


class MastermindProblem(GAProblem):
    """Implementation of GAProblem for the mastermind problem"""
    
    def __init__(self, match):
        """Initiates the match to find"""
        self._match = match
        self._threshold_fitness=match.max_score()
    
    def compute_fitness(self, chrom):
       """Computes the fitness of a chromosome given"""
       fitness = match.rate_guess(chrom)
       return fitness

    def generate_chromosome(self):
        """Generates a chromosome"""
        chromosome = match.generate_random_guess()
        return chromosome
    
    def generate_crossed_chromosome(self, parent1, parent2):
        """Generates a child chromosome from two parents"""
        x_point = rd.randrange(0, len(parent1))
        new_chrom = parent1[0:x_point] + parent2[x_point:]
        return new_chrom
        
    def generate_mutant(self, chromosome):
        """Generates a mutation for the chromosome given"""
        chromosome[rd.randint(0,3)] = rd.choice(mm.get_possible_colors())
        return chromosome


if __name__ == '__main__':

    from ga_solver import GASolver

    match = mm.MastermindMatch(secret_size=6)
    problem = MastermindProblem(match)
    solver = GASolver(problem)

    solver.reset_population()
    solver.evolve_until(problem._threshold_fitness)

    print(
        f"Best guess {solver.get_best_individual()}")
    print(
        f"Problem solved? {match.is_correct(solver.get_best_individual().chromosome)}")

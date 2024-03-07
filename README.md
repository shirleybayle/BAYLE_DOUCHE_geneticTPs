# BAYLE_DOUCHE_geneticTPs
# How to use ga_solver.py to solve a problem with genetic ;)
To use the provided `GASolver` class, start by importing the module and creating a custom problem class that inherits from `GAProblem`, implementing methods for computing fitness, generating chromosomes, creating crossed chromosomes, and introducing mutations. 
Instantiate your problem class and then create a `GASolver` object by passing the problem instance. Optionally, adjust parameters like selection rate and mutation rate. 
Initialize the population using the `reset_population` method, specifying the size if needed. Execute one generation at a time with the `evolve_for_one_generation` method, displaying a summary if desired. 
Retrieve the best individual with `get_best_individual`. Use `evolve_until` to continue evolving until a maximum number of generations is reached or a fitness threshold is met. 
Monitor progress with the generation summary and, upon completion, obtain the final solution from the best individual.
Customize the problem class according to your specific genetic algorithm requirements.

import random

# Sample Input
courses = ["CSE110", "MAT110", "PHY112"]
timeslots = 3

# Parameters
num_courses = len(courses)
num_timeslots = timeslots
chromosome_length = num_courses * num_timeslots
population_size = 10
mutation_rate = 0.1
generations = 100

def generate_chromosome():
    """Generates a random valid chromosome."""
    chromosome = [0] * chromosome_length
    for i in range(num_courses):
        slot = random.randint(0, num_timeslots - 1)
        chromosome[slot * num_courses + i] = 1
    return chromosome if calculate_fitness(chromosome) > float('-inf') else generate_chromosome()

def calculate_fitness(chromosome):
    """Calculates the fitness score of a chromosome."""
    fitness = 0
    course_count = [0] * num_courses  # Tracks how many times each course is scheduled

    # Overlap penalty
    overlap_penalty = 0
    for t in range(num_timeslots):
        slot_segment = chromosome[t * num_courses:(t + 1) * num_courses]
        active_courses = sum(slot_segment)
        if active_courses > 1:
            overlap_penalty += active_courses - 1  # Penalty is active_courses - 1
        for i in range(num_courses):
            course_count[i] += slot_segment[i]

    # Course count penalty
    course_count_penalty = 0
    for count in course_count:
        course_count_penalty += abs(count - 1)  # Corrected penalty formula

    # Total fitness
    fitness = -(overlap_penalty + course_count_penalty)
    print(overlap_penalty, course_count_penalty)
    return fitness


def crossover(parent1, parent2):
    """Performs single-point crossover between two parents."""
    point = random.randint(1, chromosome_length - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


def mutate(chromosome):
    """Mutates a chromosome with a given probability."""
    for i in range(chromosome_length):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

def select_parent(population, fitnesses):
    """Selects a parent using roulette-wheel selection."""
    total_fitness = sum(fitnesses)
    if total_fitness <= 0:  # Avoid issues with zero or negative total fitness
        return random.choice(population)  # Pick a random parent

    pick = random.uniform(0, total_fitness)
    current = 0
    for i, fitness in enumerate(fitnesses):
        current += fitness
        if current > pick:
            return population[i]

    # Fallback in case of floating-point issues
    return random.choice(population)



# Genetic Algorithm
def genetic_algorithm():

    population = [generate_chromosome() for _ in range(population_size)]

    for generation in range(generations):
        fitnesses = [calculate_fitness(chromosome) for chromosome in population]
        
        if all(f == float('-inf') for f in fitnesses):
            raise ValueError("All chromosomes have invalid fitness.")

        new_population = []

        for _ in range(population_size // 2):
            parent1 = select_parent(population, fitnesses)
            parent2 = select_parent(population, fitnesses)
            if parent1 is None or parent2 is None:
                continue
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutatation(child1), mutatation(child2)])

        population = new_population

        print("Population:", population)
        print("Fitnesses:", fitnesses)

    best_chromosome = max(population, key=calculate_fitness)
    best_fitness = calculate_fitness(best_chromosome)

    print(f"Best Chromosome: {''.join(map(str, best_chromosome))}")
    print(f"Fitness: {best_fitness}")


# Tournament Selection
def tournament_select(population, fitnesses, tournament_size=3):
    """
    Selects a parent using tournament selection.
    
    Args:
        population (list): The list of chromosomes.
        fitnesses (list): The list of fitness values corresponding to the population.
        tournament_size (int): Number of chromosomes in each tournament (default is 3).
    
    Returns:
        list: The selected parent chromosome.
    """
    # Randomly select tournament_size individuals from the population
    tournament_indices = random.sample(range(len(population)), tournament_size)
    tournament = [(population[i], fitnesses[i]) for i in tournament_indices]
    
    # Select the chromosome with the highest fitness
    best_chromosome = max(tournament, key=lambda x: x[1])[0]
    
    return best_chromosome

# Genetic Algorithm with Tournament Selection
def genetic_algorithm_with_tournament_selection():

    population = [generate_chromosome() for _ in range(population_size)]

    for generation in range(generations):
        fitnesses = [calculate_fitness(chromosome) for chromosome in population]
        
        if all(f == float('-inf') for f in fitnesses):
            raise ValueError("All chromosomes have invalid fitness.")

        new_population = []

        for _ in range(population_size // 2):
            parent1 = tournament_select(population, fitnesses, tournament_size=3)
            parent2 = tournament_select(population, fitnesses, tournament_size=3)
            if parent1 is None or parent2 is None:
                continue
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutatation(child1), mutatation(child2)])

        population = new_population

        print("Population:", population)
        print("Fitnesses:", fitnesses)

    best_chromosome = max(population, key=calculate_fitness)
    best_fitness = calculate_fitness(best_chromosome)

    print(f"Best Chromosome: {''.join(map(str, best_chromosome))}")
    print(f"Fitness: {best_fitness}")


# Two Point Crossover
def two_point_crossover(parent1, parent2):
    """
    Perform two-point crossover on two parents to generate two offspring.
    
    Args:
        parent1 (list): Binary chromosome of the first parent.
        parent2 (list): Binary chromosome of the second parent.

    Returns:
        tuple: Two offspring chromosomes.
    """
    length = len(parent1)

    # Randomly choose two crossover points ensuring point2 > point1
    point1 = random.randint(0, length - 2)
    point2 = random.randint(point1 + 1, length - 1)

    print(f"Chosen crossover points: {point1}, {point2}")

    # Create offspring by swapping segments between the two points
    offspring1 = (
        parent1[:point1] +
        parent2[point1:point2] +
        parent1[point2:]
    )
    offspring2 = (
        parent2[:point1] +
        parent1[point1:point2] +
        parent2[point2:]
    )

    return offspring1, offspring2

# Genetic Algorithm with Two Point Crossover
def genetic_algorithm_with_two_point_crossover():

    population = [generate_chromosome() for _ in range(population_size)]

    for generation in range(generations):
        fitnesses = [calculate_fitness(chromosome) for chromosome in population]
        
        if all(f == float('-inf') for f in fitnesses):
            raise ValueError("All chromosomes have invalid fitness.")

        new_population = []

        for _ in range(population_size // 2):
            parent1 = select_parent(population, fitnesses)
            parent2 = select_parent(population, fitnesses)
            if parent1 is None or parent2 is None:
                continue
            child1, child2 = two_point_crossover(parent1, parent2)
            new_population.extend([mutatation(child1), mutatation(child2)])

        population = new_population

        print("Population:", population)
        print("Fitnesses:", fitnesses)

    best_chromosome = max(population, key=calculate_fitness)
    best_fitness = calculate_fitness(best_chromosome)

    print(f"Best Chromosome: {''.join(map(str, best_chromosome))}")
    print(f"Fitness: {best_fitness}")


genetic_algorithm()
genetic_algorithm_with_tournament_selection()
genetic_algorithm_with_two_point_crossover()

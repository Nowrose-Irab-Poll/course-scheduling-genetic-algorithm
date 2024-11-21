# Genetic Algorithm for Course Scheduling

## Problem Description
This project implements a genetic algorithm to solve a course scheduling problem. The goal is to schedule a set of courses into a fixed number of timeslots per day while satisfying the following constraints:

1.    No Overlap: A timeslot cannot have more than one course scheduled.
2.    Unique Scheduling: Each course must be scheduled exactly once.

The solution uses a chromosome-based representation, fitness evaluation, and evolutionary principles to find an optimal or near-optimal schedule.

## Chromosome Representation
- A chromosome is represented as a binary string of length 𝑁 × 𝑇 N×T, where:
  - N: Number of courses.
  - T: Number of timeslots.
- The chromosome is divided into 𝑇 T segments, each representing a timeslot. Each bit in a segment indicates whether a course is scheduled in that timeslot.

### Example
For 3 courses (CSE110, MAT110, PHY112) and 3 timeslots, a sample chromosome might look like this:
```
110110010
```
- Timeslot 1: 110 (CSE110 and MAT110 are scheduled).
- Timeslot 2: 110 (CSE110 and MAT110 are scheduled).
- Timeslot 3: 010 (MAT110 is scheduled).

## Fitness Function
The fitness function evaluates the quality of a schedule based on the following penalties:
1. Overlap Penalty:
   - For each timeslot, if 𝑥 x courses are scheduled, the penalty is 𝑥 − 1 x−1.
3. Course Count Penalty:
   - For each course, if it is scheduled 𝑥 x times, the penalty is ∣ 𝑥 − 1 ∣ ∣x−1∣.

## Fitness Score:
  Fitness=−(Overlap Penalty+Course Count Penalty)

## Algorithm Workflow
1.  Initialization:
    - A population of random chromosomes is generated.
3.  Fitness Evaluation:
    - Each chromosome is evaluated using the fitness function.
4.  Selection:
    - Parents are selected using roulette-wheel selection.
5.  Crossover:
    - Single-point crossover is applied to generate offspring.
6.  Mutation:
    - Random mutation is applied to introduce diversity.
7.  Iteration:
    - Steps 2–5 are repeated for a fixed number of generations.
8.  Output:
    - The best chromosome and its fitness score are printed.

## Input and Output

### Input
- Courses: ["CSE110", "MAT110", "PHY112"]
- Timeslots: 3

### Output
- Best Chromosome: The binary string representing the optimal schedule.
- Fitness: The fitness score of the best chromosome.
- 
### Example Output
```
Best Chromosome: 110110010
Fitness: -6
```

## Improvements and Future Work
-  Extend the algorithm to support:
  - Different weights for penalties.
  - Variable timeslot lengths.
  - Course priorities or dependencies.
- Integrate visualization tools for schedule representation.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions
Contributions, issues, and feature requests are welcome! Feel free to open a pull request or raise an issue on GitHub.


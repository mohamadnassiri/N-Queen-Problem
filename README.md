# N-Queen Problem
N Queen Problem (Backtracking, Genetic, Heuristic)

This Python program implements three different algorithms to solve the N-Queens problem: Backtracking, Genetic Algorithm, and a Heuristic (Nearest Neighbor) Algorithm.

## Table of Contents

- [N-Queens Problem](#n-queens-problem)
- [Algorithms](#algorithms)
 - [Backtracking Algorithm](#backtracking-algorithm)
 - [Genetic Algorithm](#genetic-algorithm)
 - [Heuristic (Nearest Neighbor) Algorithm](#heuristic-nearest-neighbor-algorithm)
- [How to Use](#how-to-use)
- [Performance](#performance)

## N-Queens Problem

The N-Queens problem is a classic problem in computer science that involves placing N queens on an N×N chessboard such that no two queens attack each other. A solution to the N-Queens problem is a placement of N queens on the chessboard where no two queens share the same row, column, or diagonal.

## Algorithms

### Backtracking Algorithm

The backtracking algorithm is a recursive approach to solving the N-Queens problem. It places queens on the board one by one, checking for safety at each step. If a safe position is found, the algorithm proceeds to the next queen. If no safe position is available, it backtracks to the previous queen and tries a different position.

### Genetic Algorithm

The genetic algorithm is an evolutionary algorithm that attempts to solve the N-Queens problem by generating and evolving a population of candidate solutions. It starts with a random population of solutions and iteratively applies genetic operators such as selection, crossover, and mutation to generate new and potentially better solutions.

### Heuristic (Nearest Neighbor) Algorithm

The heuristic (nearest neighbor) algorithm is a greedy approach that tries to place queens on the board in a way that minimizes the number of attacks between queens. It starts by placing the first queen randomly and then places subsequent queens in the position with the least number of attacks from the previously placed queens.

## How to Use

1. Run the program.
2. Enter the value of N for the N-Queens problem.
3. Choose the algorithm you want to use (1 - Backtracking, 2 - Genetic, 3 - Heuristic).
4. For large values of N (> 8) with the Backtracking algorithm, you will be prompted to confirm if you want to continue, as the number of solutions can be very large.
   
## Performance

The performance of the algorithms varies depending on the value of N and the complexity of the problem. The Backtracking algorithm is generally slower for larger values of N, while the Genetic and Heuristic algorithms can provide reasonably good solutions in a shorter time. However, the quality of the solutions may vary.

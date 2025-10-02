import random
import copy
import time


SOLUTIONS = (1, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184,
             14772512, 95815104, 666090624, 4968057848, 39029188884, 314666222712, 2691008701644,
             24233937684440, 227514171973736, 2207893435808352, 22317699616364044)

def is_safe(board, row, col, n):
    
    if any(board[row][j] == 1 for j in range(col)):
        return False

    
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i, j = i - 1, j - 1

    
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i, j = i + 1, j - 1

    return True

def solve_backtracking_all(board, col, n, solutions):
    if col == n:
        solutions.append([row[:] for row in board])
        return

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_backtracking_all(board, col + 1, n, solutions)
            board[row][col] = 0

def solve_n_queens_backtracking(n):
    board = [[0 for j in range(n)] for i in range(n)]
    solutions = []
    start_time = time.time()
    solve_backtracking_all(board, 0, n, solutions)
    end_time = time.time()
    execution_time = round(end_time - start_time, 4)
    return solutions, execution_time


def fitness(solution, n):
    attacks = 0
    for i in range(n):
        for j in range(i + 1, n):
            if solution[i] == solution[j] or abs(solution[i] - solution[j]) == j - i:
                attacks += 1
    return attacks

def tournament_selection(population, n):
    tournament = random.sample(population, 2)
    if fitness(tournament[0], n) < fitness(tournament[1], n):
        return tournament[0]
    else:
        return tournament[1]

def crossover(parent1, parent2):
    child = [-1] * len(parent1)
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child[start:end] = parent1[start:end]
    remaining = [i for i in parent2 if i not in child]
    j = end
    for i in range(len(child)):
        if child[i] == -1:
            child[i] = remaining.pop(0)
    return child

def mutate(child, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(child)), 2)
        child[i], child[j] = child[j], child[i]
    return child

def genetic_algorithm(population_size, n, generations, mutation_rate):
    population = [random.sample(range(n), n) for _ in range(population_size)]
    for generation in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1 = tournament_selection(population, n)
            parent2 = tournament_selection(population, n)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
    best_solution = min(population, key=lambda x: fitness(x, n))
    return best_solution

def solve_n_queens_genetic(n, population_size=100, generations=1000, mutation_rate=0.1):
    start_time = time.time()
    solution = genetic_algorithm(population_size, n, generations, mutation_rate)
    end_time = time.time()
    execution_time = round(end_time - start_time, 4)
    return solution, execution_time


def count_attacks(solution, row, col, n):
    attacks = 0
    for i in range(col):
        if solution[i] == row or \
           abs(solution[i] - row) == col - i:
            attacks += 1
    return attacks

def nearest_neighbor(n):
    solution = [-1] * n
    solution[0] = random.randint(0, n-1)
    for col in range(1, n):
        min_attacks = float('inf')
        min_row = -1
        for row in range(n):
            if row not in solution:
                attacks = count_attacks(solution, row, col, n)
                if attacks < min_attacks:
                    min_attacks = attacks
                    min_row = row
        solution[col] = min_row
    return solution

def solve_n_queens_heuristic(n):
    start_time = time.time()
    solution = nearest_neighbor(n)
    end_time = time.time()
    execution_time = round(end_time - start_time, 4)
    return solution, execution_time

def board_to_list(board, n):
    """Convert board to list of lists for display"""
    return [[1 if board[i][j] == 1 else 0 for j in range(n)] for i in range(n)]

def solution_to_board(solution, n):
    """Convert solution list to board"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        board[i][solution[i]] = 1
    return board
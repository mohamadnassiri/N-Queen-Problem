import random
import copy
import time

SOLUTIONS = (1, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184,
             14772512, 95815104, 666090624, 4968057848, 39029188884, 314666222712, 2691008701644,
             24233937684440, 227514171973736, 2207893435808352, 22317699616364044)

def get_board_size():
    n = int(input("Enter the value of N for the N-Queens problem: "))
    return n


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

def solve_backtracking(board, col, n, count):
    if col == n:
        print_board(board, n)
        count[0] += 1  
        return False  

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            print(f"Placing a queen at ({row}, {col})")
            print_board(board, n)

            solve_backtracking(board, col + 1, n, count)  

            board[row][col] = 0
            print(f"Backtracking from ({row}, {col})")
            print_board(board, n)

    return False  

def solve_n_queens_backtracking(n):
    board = [[0 for j in range(n)] for i in range(n)]
    print("\nBacktracking Algorithm:")
    count = [0]  
    cont = check_solutions(n, SOLUTIONS)
    if cont == 'y':
        start_time = time.time()
        solve_backtracking(board, 0, n, count)  
        if count[0] == 0:
            print("No solution found for N =", n)
        else:
            print("Solutions found for N =", n)
        end_time = time.time()
        execution_time = round(end_time - start_time, 4)  
        print(f"Time taken to solve: {execution_time} seconds")
        print(f"Problem solved {count[0]} times.")



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
    print("Genetic Algorithm:")
    print(f"Initial population: {population}")
    for generation in range(generations):
        print(f"Generation {generation + 1}:")
        new_population = []
        for _ in range(population_size // 2):
            parent1 = tournament_selection(population, n)
            parent2 = tournament_selection(population, n)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
            print(f"  New child: {child}")
        population = new_population
    best_solution = min(population, key=lambda x: fitness(x, n))
    print(f"Best solution found: {best_solution}")
    return best_solution

def solve_n_queens_genetic(n, population_size=100, generations=1000, mutation_rate=0.1):
    start_time = time.time()
    solution = genetic_algorithm(population_size, n, generations, mutation_rate)
    end_time = time.time()
    execution_time = round(end_time - start_time, 4)  
    print("Solution for N =", n)
    for i in range(n):
        row = [''] * n
        for j in range(n):
            if solution[i] == j:
                row[j] = '♕ '
            else:
                if (i + j) % 2 == 0:
                    row[j] = '■ '
                else:
                    row[j] = '□ '
        print(''.join(row))
    print(f"Time taken to solve: {execution_time} seconds")

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
    print(f"Initial solution: {solution}")
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
        print(f"Placing a queen at ({min_row}, {col}), with {min_attacks} attacks")
    return solution

def solve_n_queens_heuristic(n):
    start_time = time.time()
    print("Heuristic Algorithm (Nearest Neighbor):")
    solution = nearest_neighbor(n)
    end_time = time.time()
    execution_time = round(end_time - start_time, 4)  
    print("Solution for N =", n)
    for i in range(n):
        row = [''] * n
        for j in range(n):
            if solution[i] == j:
                row[j] = '♕ '
            else:
                if (i + j) % 2 == 0:
                    row[j] = '■ '
                else:
                    row[j] = '□ '
        print(''.join(row))
    print(f"Time taken to solve: {execution_time} seconds")

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("♕ ", end="")
            else:
                if (i + j) % 2 == 0:
                    print("■ ", end="")
                else:
                    print("□ ", end="")
        print()


def check_solutions(n, SOLUTIONS):
    if n > 8:
        cont = input('\nA board of size {} has {} solutions. This will probably take a while. '
                     'Would you still like to continue? (y/n)\n>>> '
                     ''.format(n, '{:,}'.format(SOLUTIONS[n])))
        while cont not in ['y', 'n']:
            cont = input('Please enter "y" or "n":\n>>> ')
        return cont
    else:
        return 'y'


def main():
    n = get_board_size()
    algorithm_choice = input("Choose the algorithm (1 - Backtracking, 2 - Genetic, 3 - Heuristic): ")

    if algorithm_choice == "1":
        solve_n_queens_backtracking(n)
    elif algorithm_choice == "2":
        solve_n_queens_genetic(n)
    elif algorithm_choice == "3":
        solve_n_queens_heuristic(n)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
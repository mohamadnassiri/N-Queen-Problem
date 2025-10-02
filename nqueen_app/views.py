from django.shortcuts import render
from .solvers import solve_n_queens_backtracking, solve_n_queens_genetic, solve_n_queens_heuristic, solution_to_board

def home(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        algorithm = request.POST.get('algorithm')
        if algorithm == '1':
            boards, execution_time = solve_n_queens_backtracking(n)
            description = f"Backtracking algorithm explored all possible queen placements systematically, finding {len(boards)} unique solutions for N={n}."
        elif algorithm == '2':
            solution, execution_time = solve_n_queens_genetic(n)
            boards = [solution_to_board(solution, n)]
            description = f"Genetic algorithm used evolutionary principles with population size 100, running for 1000 generations with 10% mutation rate to find an approximate solution."
        elif algorithm == '3':
            solution, execution_time = solve_n_queens_heuristic(n)
            boards = [solution_to_board(solution, n)]
            description = f"Heuristic (Nearest Neighbor) algorithm placed queens by selecting the row with minimum conflicts at each column to find a solution."
        else:
            boards, execution_time, description = [], 0, "Invalid algorithm selected."
        return render(request, 'result.html', {'boards': boards, 'time': execution_time, 'n': n, 'algorithm': algorithm, 'description': description})
    return render(request, 'home.html')

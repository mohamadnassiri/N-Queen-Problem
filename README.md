# N-Queen Problem Web Solver

A **web-based implementation** of the N-Queens problem with a modern glassy dark theme, allowing users to **solve and visualize the N-Queens problem** using different algorithms.

## Features

* Solve the N-Queens problem for any N between 1 and 10.
* Display all solutions visually and interactively.
* Choose solving algorithms:

  * **Backtracking**: Find all solutions.
  * **Genetic Algorithm**: Approximate solution using genetic algorithm.
  * **Heuristic (Nearest Neighbor)**: Use a nearest neighbor heuristic.
* Modern dark glass-like UI similar to Windows 11.
* **Toggle Solutions View** button to show/hide solutions.
* Interactive buttons for **Try Again** and **Back to Top / Down**.
* Responsive design for mobile and desktop.
* Beautiful styling for **homepage, forms, chess boards, and solution cards**.

## Demo

![Homepage screenshot](screenshots/Home.png)
![Solutions screenshot](screenshots/Solutions.png)

## Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/mohamadnassiri/N-Queen-Problem.git
cd N-Queen-Problem
```

2. Create and activate a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the server:

```bash
python manage.py runserver
```

5. Open your browser and visit:

```
http://127.0.0.1:8000/
```

## Algorithms

* **Backtracking**: Standard recursive algorithm to find all solutions.
* **Genetic Algorithm**: Evolutionary algorithm for approximate solution.
* **Heuristic (Nearest Neighbor)**: Approximate solution using nearest neighbor strategy.

## Technologies Used

* **Python 3.x**
* **Django** web framework
* **Bootstrap 5** for responsive UI
* **FontAwesome** icons
* Modern CSS with glassy dark theme

## License

This project is licensed under the MIT License.

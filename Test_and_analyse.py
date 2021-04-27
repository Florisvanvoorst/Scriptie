import random

from Rubiks_Cube.solver   import Solver
from Rubiks_Cube.cube     import Cube
from Rubiks_Cube.optimize import optimize_moves

SOLVED_CUBE_STR = "OOOOOOOOOYYYGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBRRRRRRRRR"
MOVES           = ["L", "R", "U", "D", "F", "B", "M", "E", "S"]

def run():
  count     = 0
  successes = 0
  failures  = 0

  beginner_avg_opt_moves     = 0.0
  beginner_avg_moves         = 0.0
  intermediate_avg_opt_moves = 0.0
  intermediate_avg_moves     = 0.0
  expert_avg_opt_moves       = 0.0
  expert_avg_moves           = 0.0

  while count < 1000:
    count += 1

    scramble_moves    = " ".join(random.choices(MOVES, k=300))
    beginner_cube     = Cube(SOLVED_CUBE_STR)
    intermediate_cube = Cube(SOLVED_CUBE_STR)
    expert_cube       = Cube(SOLVED_CUBE_STR)
    check_cube        = Cube(SOLVED_CUBE_STR)

    beginner_cube.sequence(scramble_moves)
    intermediate_cube.sequence(scramble_moves)
    expert_cube.sequence(scramble_moves)
    check_cube.sequence(scramble_moves)

    beginner     = Solver(beginner_cube)
    intermediate = Solver(intermediate_cube)
    expert       = Solver(expert_cube)

    beginner.solveBeginner()
    intermediate.solveIntermediate()
    expert.solveExpert()

    if (beginner_cube.is_solved() and intermediate_cube.is_solved() and expert_cube.is_solved()):
        successes += 1
        beginner_opt_moves     = optimize_moves(beginner.moves)
        intermediate_opt_moves = optimize_moves(intermediate.moves)
        expert_opt_moves       = optimize_moves(expert.moves)

        beginner_avg_moves         = (beginner_avg_moves * (successes - 1) + len(beginner.moves)) / float(successes)
        beginner_avg_opt_moves     = (beginner_avg_opt_moves * (successes - 1) + len(beginner_opt_moves)) / float(successes)
        intermediate_avg_moves     = (intermediate_avg_moves * (successes - 1) + len(intermediate.moves)) / float(successes)
        intermediate_avg_opt_moves = (intermediate_avg_opt_moves * (successes - 1) + len(intermediate_opt_moves)) / float(successes)
        expert_avg_moves           = (expert_avg_moves * (successes - 1) + len(expert.moves)) / float(successes)
        expert_avg_opt_moves       = (expert_avg_opt_moves * (successes - 1) + len(expert_opt_moves)) / float(successes)
    else:
        failures += 1
        print(f"Beginner: {beginner_cube.is_solved()}")
        print(f"Intermediate: {intermediate_cube.is_solved()}")
        print(f"Expert: {expert_cube.is_solved()}")
        print(f"Failed ({successes + failures}): {check_cube.flat_str()}")

    total = successes + failures
    if total == 1 or total == 10 or total == 100 or total == 1000:
      pass_percentage = 100 * successes / total
      print(f"{total}: {successes} successes ({pass_percentage:0.3f}% passing)")
      print(f" Beginner     = avg_moves={beginner_avg_moves:0.3f} avg_opt_moves={beginner_avg_opt_moves:0.3f}")
      print(f" Intermediate = avg_moves={intermediate_avg_moves:0.3f} avg_opt_moves={intermediate_avg_opt_moves:0.3f}")
      print(f" Expert       = avg_moves={expert_avg_moves:0.3f} avg_opt_moves={expert_avg_opt_moves:0.3f}")

if __name__ == '__main__':
  run()

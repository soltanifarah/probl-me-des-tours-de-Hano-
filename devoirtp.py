from collections import deque

class GeneralizedHanoiProblem:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.start_state = (tuple(range(num_disks, 0, -1)), (), (), (), (), ())
        self.goal_state = ((), (), (), (), (), tuple(range(num_disks, 0, -1)))

    def is_valid_move(self, state, src, dest):
        src_peg = state[src]
        dest_peg = state[dest]
        if not src_peg:# If the source peg is empty
            return False
        # If the destination peg is not empty
        # and the top disk of the source peg is larger than the top disk of the destination peg
        if dest_peg and src_peg[-1] > dest_peg[-1]:
            return False
        return True

    def apply_move(self, state, src, dest):
        src_peg = list(state[src])
        dest_peg = list(state[dest])
        # Remove the top disk from the source peg and store it in a variable
        disk = src_peg.pop()
        # Add the disk to the top of the destination  peg
        dest_peg.append(disk)
        new_state = list(state)
         #convert back tuple
        new_state[src] = tuple(src_peg)
        new_state[dest] = tuple(dest_peg)
        return tuple(new_state)

    def get_neighbors(self, state):
        neighbors = []
        for src in range(6):
            if state[src]:
                for dest in range(6):
                    if src != dest and self.is_valid_move(state, src, dest):
                        new_state = self.apply_move(state, src, dest)
                        neighbors.append(new_state)
        return neighbors

    def is_goal(self, state):
        return state == self.goal_state

    def bfs(self):
        visited = set()
        queue = deque([(self.start_state, [])])

        while queue:
            state, path = queue.popleft()

            if state in visited:
                continue

            if self.is_goal(state):
                return path

            visited.add(state)

            for neighbor in self.get_neighbors(state):
                new_path = path + [(state, neighbor)]
                queue.append((neighbor, new_path))

        return None

def print_solution(solution):
    if solution is None:
        print("Pas de solution trouvée.")
        return

    for i, (state, _) in enumerate(solution):
        print(f"Step {i}:")
        for j in range(6):
            peg = list(state[j])
            peg.reverse()
            print(f"{j+1}: ", end="")
            for disk in peg:
                print(disk, end=" ")
            print()
        print()

    print("Solution trouvée.")

for num_disks in range(6, 16):
    problem = GeneralizedHanoiProblem(num_disks)
    solution = problem.bfs()
    print(f"Solution for {num_disks} disks:")
    print_solution(solution)     

import heapq

class GeneralizedHanoiProblem:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.start_state = (tuple(range(num_disks, 0, -1)), (), (), (), (), ())
        self.goal_state = ((), (), (), (), (), tuple(range(num_disks, 0, -1)))

    def is_valid_move(self, state, src, dest):
        src_peg = state[src]
        dest_peg = state[dest]
        if not src_peg:
            return False
        if dest_peg and src_peg[-1] > dest_peg[-1]:
            return False
        return True

    def apply_move(self, state, src, dest):
        src_peg = list(state[src])
        dest_peg = list(state[dest])
        disk = src_peg.pop()
        dest_peg.append(disk)
        new_state = list(state)
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

    def heuristic(self, state):
# on comptabilise pour chaque disque le nombre de disques au-dessus
        a = 0
        for i, disk_above in enumerate(state):
            count = sum(disk > disk_above[j] for j, disk in enumerate(state[i]))      
        a += count


        b = 0
         #  iterates over all disks on the current peg except for the bottom disk 
        for peg in state:
            for i in range(1, len(peg)):
                 # Check if there if disk is small than disk below 
                if peg[i] < peg[i-1]:
                    b += 1
                    
#uncorrect position
        c = 0
         # Loop over each disk in the problem
        for i in range(self.num_disks):
             
               
            for j, peg in enumerate(state):
                    # this checks if the current disk i+1 (since the loop starts at i = 0) 
                    # is on the current peg peg, up to the second-to-last disk 
                if i+1 in peg[:len(peg)-1]:
                    break
                #- this checks if we've reached the last peg (i.e., j == 5)
                # and the current disk is not on that peg.
                if j == 5 and i+1 not in peg:
                     # If the current disk is not on any peg, increment the count
                    c += 1

        return a + 3*b + c


    def a_star(self):
        # Initialize variables
        visited = set()# set of visited states
        # priority queue of states to explore, initialized with the start state
        queue = [(self.heuristic(self.start_state), self.start_state, [])]

        while queue:
             # Pop the state with the lowest f-value lowest priority  from the priority queue
            heur, state, path = heapq.heappop(queue)
            for e in queue:
                print(e[0])
            print("------------------------------")
            print(heur)
            print("****************************")
  # Check if the state has already been visited
            if state in visited:
                continue
 # Check if the state is the goal state
            if self.is_goal(state):
                return path

        # Add the state to the set of visited states
            visited.add(state)
 # Explore the neighbors of the current state
            for neighbor in self.get_neighbors(state):
               
                   
                new_path = path + [(state, neighbor)]
                  # Compute the new path and f-value for the neighbor
                f = 0*len(new_path) + self.heuristic(neighbor)
                  # Add the neighbor to the priority queue
                heapq.heappush(queue, (f, neighbor, new_path))

    # If the priority queue is empty and no goal state has been found, return None
        return None

def print_solution(solution):
    if solution is None:
        print("0")
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

    print(f"Number of moves: {len(solution)}")

for num_disks in range(7,8):
    problem = GeneralizedHanoiProblem(num_disks)
    solution = problem.a_star()
    print(f"Solution for {num_disks} disks:")
    print_solution(solution)    
    


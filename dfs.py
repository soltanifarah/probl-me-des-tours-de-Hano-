class Hanoi:
    def __init__(self, pegs, disks):
        self.pegs = pegs
        self.disks = disks
        self.state = [list(range(1, disks+1))] + [[] for _ in range(pegs-1)]
        self.moves = 0

    def is_legal_move(self, src, dest):
        if not self.state[src]:
            return False
        if not self.state[dest]:
            return True
        return self.state[src][-1] < self.state[dest][-1]

    def move_disk(self, src, dest):
        self.state[dest].append(self.state[src].pop())
        self.moves += 1

    def dfs(self, src, dest, num_disks):
        if num_disks == 1:
    
            if self.is_legal_move(src, dest):
                self.move_disk(src, dest)
            return
        # Generate a list of temporary pegs that we can use during the move
        temp_pegs = [peg for peg in range(self.pegs) if peg not in (src, dest)]
            # Iterate over all available temporary pegs
            # Recursively move all but the bottom disk to the current temporary peg
        for peg in temp_pegs:
            self.dfs(src, peg, num_disks - 1)
             # Move the bottom disk from the source peg to the destination peg if it is legal
            if self.is_legal_move(src, dest):
                self.move_disk(src, dest)
            self.dfs(peg, dest, num_disks - 1)
            break

def main():
    pegs = 6
    disks = int(input("Enter the number of disks (between 6 and 15): "))
    if disks < 6 or disks > 15:
        print("Invalid number of disks. Please enter a value between 6 and 15.")
        return

    hanoi = Hanoi(pegs, disks)
    hanoi.dfs(0, pegs-1, disks)

    print(f"Total moves: {hanoi.moves}")
    print("Final state:")
    for peg in hanoi.state:
        print(peg)

if __name__ == "__main__":
    main()
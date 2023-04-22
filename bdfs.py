class Hanoi:
    def __init__(self, pegs, disks):
        self.pegs = pegs
        self.disks = disks
        self.state = [list(range(disks, 0, -1))] + [[] for _ in range(pegs - 1)]
        self.moves = 0

    def is_legal_move(self, src, dest):
        if not self.state[src]:
            return False
        if not self.state[dest]:
            return True
        return self.state[src][-1] < self.state[dest][-1]

    def move_disk(self, src, dest):
        if not self.state[src]:
            return
        disk = self.state[src][-1]
        self.state[dest].append(self.state[src].pop())
        self.moves += 1
        print(f"Move disk {disk} from peg {src + 1} to peg {dest + 1}")

    def bdfs(self, src, dest, num_disks):
        if num_disks <= 0:
            return

        if num_disks == 1:
                # If the move is legal, move the disk from the source peg to the destination peg
            if self.is_legal_move(src, dest):
                self.move_disk(src, dest)
            return

        spare = [peg for peg in range(self.pegs) if peg != src and peg != dest][0]
    # Recursively move all remaining disks from the spare peg to the destination peg
        self.bdfs(src, spare, num_disks - 1)
        self.move_disk(src, dest)
        self.bdfs(spare, dest, num_disks - 1)

def main():
    pegs = 6
    disks = int(input("Enter the number of disks (between 6 and 15): "))
    if disks < 6 or disks > 15:
        print("Invalid number of disks. Please enter a value between 6 and 15.")
        return

    hanoi = Hanoi(pegs, disks)
    hanoi.bdfs(0, pegs - 1, disks)

    print(f"\nTotal moves: {hanoi.moves}")
    print("Final state:")
    for peg in hanoi.state:
        print(peg)

if __name__ == "__main__":
    main()
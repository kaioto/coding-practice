
class Towers:


    def __init__(self, size):
        self.towers = [range(size, 0, -1), [], []]
        self.size = size
        self.last_move = [None, None]
        self.moves = 0

    def run_towers(self):
        while len(self.towers[2]) < self.size:
            if self._move(2,1):
                pass
            elif self._move(1,0):
                pass
            elif self._move(1,2):
                pass
            else:
                self._move(0,1)
            self.moves += 1
        print(self.towers)
        print("Completed in %d moves" % self.moves)

    def _move(self, to_addr, from_addr):
        if self.last_move != [from_addr, to_addr] and len(self.towers[from_addr]):
            if not (self.towers[to_addr] and self.towers[to_addr][-1] < self.towers[from_addr][-1]):
                self.last_move = [to_addr, from_addr]
                self.towers[to_addr].append(self.towers[from_addr].pop())
                return True
        return False

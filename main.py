from random import randrange

# Array = [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# Index = 4, Array[4] = 7
# Parent Index = math.floor(Index / 2), Parent Index of Array[4] = Array[math.floor(4/2)] or Array[2]
# Left Child =  Parent Index * 2, Array[4] = Left Child = Array[4*2] or Array[8]
# Right Child  = (Parent Index * 2) + 1 = Right Child = Array[4*2+1] or Array[9]
"""
                        10
                  9           8
               7     6     5     4
             3   2 1

        [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  top to bottom, left to right
"""

# heap = [0, ("player1", 40), ("player2", 29)]
#       heap[1][1] = 40
#                 [1] "player1": 40
#           [2] "player2": 29


class BattleGroundsHeap:
    def __init__(self, numOfPlayers):
        super().__init__()
        self.players = {}
        for x in range(0, numOfPlayers):
            self.players[f'Player {x+1}'] = 40

        self.battleground = []

        for k, v in self.players.items():
            self.battleground.append((k, v))

        self.heap = [0]
        for x in self.battleground:
            self.heap.append(x)
            self.__floatUp(len(self.heap) - 1)  # len(self.heap) - 1 = index

    def add(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def get(self):
        if len(self.heap) >= 2:
            # if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def rem(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.rem()
            self.__floatDown(1)
        elif len(self.heap) == 2:
            max = self.heap.rem()
        else:
            max = False

        return max

    def battleground_round(self):
        if len(self.heap) <= 2:
            if self.get() == False:
                print("Draw!")
                return
            else:
                print("Winner is", self.get())
                return self.get()

        else:
            _ = self.heap
            print("Battlers:", _[1:])

            self.heap = [0]
            for x in _[1:]:
                self.heap.append((x[0], x[1] - randrange(10)))
                if self.heap[-1][1] <= 0:
                    self.heap.pop(-1)

                self.__floatUp(len(self.heap) - 1)

            self.battleground_round()

    def __swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]

    def __floatUp(self, index):
        parent = index // 2

        if index <= 1:
            return
        elif self.heap[index][1] > self.heap[parent][1]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __floatDown(self, index):
        left = index * 2  # index
        right = left + 1  # index
        max = index  # index

        if len(self.heap) > left and self.heap[max][1] < self.heap[left][1]:
            max = left
        elif len(self.heap) > right and self.heap[max][1] < self.heap[right][1]:
            max = right

        if max != index:
            self.__swap(index, max)
            self.__floatDown(max)


if __name__ == "__main__":

    # players = {
    #     "player1": 40,
    #     "player2": 40,
    #     "player3": 40,
    #     "player4": 40,
    #     "player5": 40,
    #     "player6": 40,
    #     "player7": 40,
    #     "player8": 40,
    # }

    # battlegrounds = []

    # for k, v in players.items():
    #     battlegrounds.append((k, v))

    # print(battlegrounds)

    # desired output: [("player1", 40), ("player2", 40), ..., ("player8", 40)]

    n = int(input("How many battlers?\t\t"))

    BattleGroundsHeap(numOfPlayers=n).battleground_round()    

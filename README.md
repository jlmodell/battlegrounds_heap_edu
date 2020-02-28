# battlegrounds_heap_edu

Goal: emulate Hearthstone Battlegrounds as a max heap example to understand the principles

In a game of hearthstone battlegrounds, 8 players are matched up and begin with "n"- health.

Each round, players lose a certain amount of health and the groups are shuffled around so that the leader is at the top.

class BattleGroundsHeap requires a numOfPlayers and will init n numOfPlayers with 40 health.

(( note: not really how the game plays out, but this is simplified ))

.battleground_round()
   - emulate a "round" where every player loses a certain amount of health
   - the player with the highest health will float up to the top [O(log n)]   
   - recursively call battleground_round() until heap size is <= 2
   - if heap size == 2, determines the winner @ heap[1]
   - if heap size < 2, that means all players health went <= 0 and were removed from the heap
   - .get() function will allow you to get the player with max health in the heap if heap size >= 2 [O(1)]

sample output:

```
How many battlers?		5
Battlers: [('Player 1', 40), ('Player 2', 40), ('Player 3', 40), ('Player 4', 40)]
Battlers: [('Player 3', 39), ('Player 2', 34), ('Player 1', 34), ('Player 4', 33)]
Battlers: [('Player 3', 36), ('Player 2', 31), ('Player 1', 31), ('Player 4', 24)]
Battlers: [('Player 1', 31), ('Player 2', 28), ('Player 3', 29), ('Player 4', 24)]
Battlers: [('Player 1', 30), ('Player 2', 26), ('Player 3', 27), ('Player 4', 17)]
Battlers: [('Player 2', 23), ('Player 1', 21), ('Player 3', 19), ('Player 4', 12)]
Battlers: [('Player 2', 14), ('Player 1', 13), ('Player 3', 11), ('Player 4', 10)]
Battlers: [('Player 1', 11), ('Player 4', 10), ('Player 3', 11), ('Player 2', 8)]
Battlers: [('Player 4', 8), ('Player 1', 4), ('Player 3', 8), ('Player 2', 1)]
Battlers: [('Player 4', 2), ('Player 1', 2)]
Winner is ('Player 4', 1)
```

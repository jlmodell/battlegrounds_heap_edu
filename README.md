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
How many battlers?		4
Battlers: [('Player 1', 40), ('Player 2', 40), ('Player 3', 40), ('Player 4', 40)]
Battlers: [('Player 3', 40), ('Player 4', 37), ('Player 2', 39), ('Player 1', 31)]
Battlers: [('Player 4', 36), ('Player 3', 33), ('Player 2', 35), ('Player 1', 29)]
Battlers: [('Player 4', 30), ('Player 3', 28), ('Player 2', 26), ('Player 1', 25)]
Battlers: [('Player 3', 26), ('Player 4', 21), ('Player 2', 20), ('Player 1', 20)]
Battlers: [('Player 3', 20), ('Player 1', 20), ('Player 2', 17), ('Player 4', 12)]
Battlers: [('Player 3', 18), ('Player 1', 12), ('Player 2', 13), ('Player 4', 8)]
Battlers: [('Player 3', 9), ('Player 1', 6), ('Player 2', 6), ('Player 4', 1)]
Battlers: [('Player 1', 6), ('Player 3', 4), ('Player 2', 3)]
Winner is ('Player 1', 6)
```

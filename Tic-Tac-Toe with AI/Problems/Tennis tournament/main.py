winner_players = []

n = int(input())

for i in range(n):
    player = input().split()
    if player[1] == 'win':
        winner_players.append(player[0])

print(winner_players)
print(len(winner_players))

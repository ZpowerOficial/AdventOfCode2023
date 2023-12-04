def solve_puzzle(games):
    possible_games = []
    for game in games:
        game_id, rounds = game.split(':')
        game_id = int(game_id.split()[1])
        rounds = rounds.split(';')
        possible = True
        for round in rounds:
            cubes = round.split(',')
            for cube in cubes:
                parts = cube.split()
                count = int(parts[0])
                color = parts[1]
                if color == 'red' and count > 12:
                    possible = False
                    break
                elif color == 'green' and count > 13:
                    possible = False
                    break
                elif color == 'blue' and count > 14:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            possible_games.append(game_id)
    return sum(possible_games)

# Lendo o arquivo de entrada
with open('entradasdia2.txt', 'r') as file:
    games = file.readlines()

print(solve_puzzle(games))

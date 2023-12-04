def solve_puzzle_part2(games):
    total_power = 0
    for game in games:
        game_id, rounds = game.split(':')
        game_id = int(game_id.split()[1])
        rounds = rounds.split(';')
        min_red, min_green, min_blue = 0, 0, 0
        for round in rounds:
            cubes = round.split(',')
            for cube in cubes:
                parts = cube.split()
                count = int(parts[0])
                color = parts[1]
                if color == 'red':
                    min_red = max(min_red, count)
                elif color == 'green':
                    min_green = max(min_green, count)
                elif color == 'blue':
                    min_blue = max(min_blue, count)
        total_power += min_red * min_green * min_blue
    return total_power

# Lendo o arquivo de entrada
with open('entradasdia2.txt', 'r') as file:
    games = file.readlines()

print(solve_puzzle_part2(games))

result = 0
with open("input.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        game_id = int(line.split(":")[0].split()[1])
        tokens = []
        draws = line.split(":")[1].split(";")
        min_colors = {
            "blue":0,
            "red":0,
            "green":0
        }
        for draw in draws:
            token_str = draw.split(",")
            for token in token_str:
                token = token.split()
                number = int(token[0])
                clr = token[1]
                if number > min_colors[clr]:
                    min_colors[clr] = number
        color_power = min_colors["blue"]*min_colors["red"]*min_colors["green"]
        result += color_power
print(result)

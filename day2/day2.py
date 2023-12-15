max_blue = 14
max_red = 12
max_green = 13
result = 0
with open("input.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        game_id = int(line.split(":")[0].split()[1])
        tokens = []
        draws = line.split(":")[1].split(";")
        max_colors = {
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
                if number > max_colors[clr]:
                    max_colors[clr] = number
        valid = [
            max_colors["blue"] <= max_blue,
            max_colors["green"] <= max_green,
            max_colors["red"] <= max_red
        ]
        if all(valid):
            result += game_id
print(result)

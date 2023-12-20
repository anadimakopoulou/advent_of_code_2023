class Number:
    def __init__(self, value, location, is_part=True):
        self.value = value
        self.location = location
        self.is_part = is_part

def find_all(the_string, substring):
    # we know that the substring exists, it's a matter of finding it
    # substring will have dots(.) either on the right or on the left
    pass

non_numbers = ['!','@','#','$','%','^','&','*','(',')','_','-','=','+',',','<','?','>','`','~','/','\\'] # everything but the dot
str_digits = [str(i) for i in range(10)]
result = 0

def valid_location(location, rows, cols):
    y, x = location
    conditions = [
        x >= 0,
        y >= 0,
        x < cols,
        y < rows
    ]
    return all(conditions)

with open("input.txt","r",encoding='utf-8') as f:
    lines = f.readlines()
    rows = len(lines)
    columns = len(lines[0])
    parts = []
    # cheat: look up txt file
    # last_line = 140
    # last_line = 10
    all_symbols = []
    for line_number,line in enumerate(lines):
        line=line.strip()
        number_locations = {}
        y_location = line_number
        only_symbols_line = line
        only_numbers_line = line
        # for digit in str_digits:
        #     only_symbols_line = only_symbols_line.replace(digit,".")
        for symbol in non_numbers:
            only_numbers_line = only_numbers_line.replace(symbol,".")
        # only_symbols_line = only_symbols_line.replace("."," ").split()
        only_numbers_line = only_numbers_line.replace("."," ").split()
        # temp_line = line
        offset = 0
        for number in only_numbers_line:
            span = len(number)
            x_location = line.find(number, offset)
            try:
                if x_location > -1:
                    while line[x_location+span] in str_digits: # we have found substring, not the number
                        offset += span+1
                        x_location = line.find(number,offset)
            except IndexError:
                continue
            offset += span+1
            neighbors = []
            for s in range(span):
                y = y_location
                x = x_location + s
                if s == 0:
                    added = [(y-1,x-1), # upper left
                             (y-1,x), # up
                             (y,x-1), # left
                             (y+1,x-1), # down left
                             (y+1,x)] # down
                elif s == span-1:
                    added = [(y-1,x), # up
                             (y-1,x+1), # upper right
                             (y,x+1), # right
                             (y+1,x), # down
                             (y+1,x+1)] # down right
                else:
                    added = [(y-1,x), # up
                             (y+1,x)] # down
                neighbors.extend(added)
            # clean up neighbors
            neighbors = [n for n in neighbors if valid_location(n, rows,columns)]
            for n in neighbors:
                y,x = n
                found = False
                for symbol in non_numbers:
                    if lines[y][x] == symbol:
                        parts.append(number)
                        found=True
                        break
                if found:
                    break # we need only one neighbor to be symbol
    parts = [int(p) for p in parts]
    # print(parts)
    print(sum(parts))
    # 496971 is too low
    # 515470 is too high
    # 515411 is wrong (high/low?)

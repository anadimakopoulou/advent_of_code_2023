digits = list(map(str,list(range(10))))
digits_str = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}
def list_slice(l, start, end):
    return l if len(l) < (end-start) else l[start:end]

# another solution: for each number found written in letters,
# add the last letter again, eg string is dawaffwone12three,
# change it to dawaffonee12threee,
# then change all numbers written in letters with their digit
# counterparts, so string will become dawaff1e123e,
# then use previous code to find answer
with open("input.txt","r", encoding="utf-8") as f:
    lines = f.readlines()
    result = 0
    window_size = 15
    for line_number,line in enumerate(lines):
        line = line.strip()
        first_number = 0
        for index, _ in enumerate(line):
            s = "".join(list_slice(line, index, index+window_size))
            number_index = -1
            number_value = 0
            number_indices = {}
            for digit in digits:
                ind = s.find(digit)
                if ind > -1:
                    number_indices[digit] = ind
            if number_indices:
                str_digit = min(number_indices, key=number_indices.get) # get the key
                number_value = int(str_digit)
                number_index = min(number_indices.values()) # get the value

            string_index = -1
            string_value = 0
            string_indices = {}
            for key, value in digits_str.items():
                ind = s.find(key)
                if ind > -1:
                    string_indices[key] = ind
            if string_indices:
                str_number = min(string_indices, key=string_indices.get)
                string_value = digits_str[str_number]
                string_index = min(string_indices.values())
                    
            found = False
            if number_index > -1 or string_index > -1:
                found = True
            if number_index > -1 and string_index > -1:
                first_number = number_value if number_index < string_index else string_value
            elif number_index == -1 :
                first_number = string_value
            elif string_index == -1:
                first_number = number_value
            if found:
                break
        last_number = 0
        rev_line = line[::-1]
        for index, _ in enumerate(rev_line):
            s = "".join(list(reversed(list_slice(rev_line, index, index+window_size))))
            number_index = -1
            number_value = 0
            number_indices = {}
            for digit in digits:
                ind = s.rfind(digit)
                if ind > -1:
                    number_indices[digit] = ind
            if number_indices:
                str_digit = max(number_indices, key=number_indices.get) # get the key
                number_value = int(str_digit)
                number_index = max(number_indices.values()) # get the value    
            string_index = -1
            string_value = 0
            string_indices = {}
            for key, value in digits_str.items():
                ind = s.rfind(key)
                if ind > -1:
                    string_indices[key] = ind
            if string_indices:
                str_number = max(string_indices, key=string_indices.get)
                string_value = digits_str[str_number]
                string_index = max(string_indices.values())
            if number_index > string_index:
                last_number = number_value
            else:
                last_number = string_value
            
            found = False
            if string_index > -1 or number_index > -1:
                found = True
            if string_index > -1 and number_index > -1:
                last_number = number_value if number_index > string_index else string_value
            elif string_index > -1:
                last_number = string_value
            elif number_index > -1:
                last_number = number_value
            if found:
                break
            
        the_number = first_number*10 + last_number
        result += the_number
        # print(f"line number {line_number+1}: first number:{first_number}, last_number={last_number}")
    print(result)
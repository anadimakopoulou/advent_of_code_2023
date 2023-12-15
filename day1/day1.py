digits = list(map(str,list(range(10))))
with open("input.txt","r", encoding="utf-8") as f:
    lines = f.readlines()
    result = 0
    for line in lines:
        first_number = 0
        for char in line:
            if char in digits:
                first_number = int(char)
                break
        last_number = 0
        for char in line[::-1]:
            if char in digits:
                last_number = int(char)
                break
        the_number = first_number*10 + last_number
        result += the_number
        # print(f"first number:{first_number}, last_number={last_number}")
    print(result)
with open("input1.txt", "r") as data:
    lines = [line for line in data.read().splitlines()]
    score = 0
    for line in lines:
        numbers = []
        for i, c in enumerate(line):
            if c.isdigit():
                numbers.append(int(c))
            for dig, num in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[i:].startswith(num):
                    numbers.append(dig+1)
        calibration_value = (numbers[0]*10) + numbers[-1]
        score += calibration_value
print(score)
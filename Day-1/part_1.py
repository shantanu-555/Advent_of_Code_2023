with open("input1.txt", "r") as data:
    lines = [line for line in data.read().splitlines()]
    score = 0
    for line in lines:
        numbers = []
        for c in line:
            if c.isdigit():
                numbers.append(int(c))
        calibration_value = (numbers[0]*10) + numbers[-1]
        score += calibration_value
print(score)
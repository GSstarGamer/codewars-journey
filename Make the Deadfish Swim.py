def parse(data: str) -> list:
    currentValue = 0
    changes = []
    for letter in data:
        if letter == 'i':
            currentValue += 1
        elif letter == 'd':
            currentValue -= 1
        elif letter == 's':
            currentValue **= 2
        elif letter == 'o':
            changes.append(currentValue)
    return changes


print(parse('ioioio'))

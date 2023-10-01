def wave(people):
    return [people[:i].lower() + people[i:].capitalize() for i in range(len(list(people))) if list(people)[i] != ' ']


print(wave(' gap '))

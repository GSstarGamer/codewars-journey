def expanded_form(num):
    result = []
    for i, n in enumerate(str(num)[::-1]):
        if int(n) != 0:
            result.append(n + ('0' * i))
    result.reverse()
    return ' + '.join(result)


expanded_form(12)

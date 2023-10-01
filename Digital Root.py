def digital_root(n):
    x = [int(y) for y in str(n)]
    if len(list(str(sum(x)))) > 1:
        return digital_root(sum(x))
    else:
        return sum(x)


x = digital_root(493193)

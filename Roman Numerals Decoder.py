data = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def solution(roman: str) -> int:
    """complete the solution by transforming the roman numeral into an integer"""
    romanN = 0
    biggestNum = 0
    for letter in reversed(roman):
        num = data[letter]
        if num >= biggestNum:
            biggestNum = num
            romanN += num
        else:
            romanN -= num

    return romanN


print(solution('MDCLXVI'))

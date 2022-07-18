def solution(s, letter):
    count = 0
    for char in s:
        if char == letter:
            count += 1
    return count
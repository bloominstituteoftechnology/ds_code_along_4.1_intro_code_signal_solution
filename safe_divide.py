def solution(numerator, denominator):
    # check the value of the denominator
    if denominator == 0:
        # we will just return zero when divide by zero
        return 0
    else:
        return numerator / denominator

# 100% solution to FrogJmp on Codility
def solution(X, Y, D):
    if ((Y - X) % D) != 0:
        return ((Y - X) / D) + 1
    return ((Y - X) / D)
    pass
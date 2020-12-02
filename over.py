#Game termination and Winner declearation
def win(score1,score2,score3):
    if score1 >= 5:
        return 1
    elif score2 >= 5:
        return 2
    elif score3 >= 5:
        return 3
    elif score1 <= -5 and score2 <= -5 and score3<= -5:
        return -1
    else:
        return 0

def latest(scores):
    last = scores.pop()
    return last


def personal_best(scores):
    max_score = max(scores)
    return max_score


def personal_top_three(scores):
    top_three = sorted(scores, reverse=True)
    return top_three[:3]


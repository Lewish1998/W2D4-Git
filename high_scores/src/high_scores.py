def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    list = sorted(scores)
    return list[-1], list[-2], list[-3]

def reverse_scores_list(scores):
    list = sorted(scores)
    list.reverse()
    return list

def top_three_with_a_tie(scores):
    list = sorted(scores)
    list = reversed(list)
    scores = []
    if list[0] == list[1]:
        scores.append(list[0])
    if list[1] == list[2]:
        scores.append(list[1])
    if list[2] == list[3]:
        scores.append(list[2])
    return scores

def top_3_2_numbers(scores):
    list = sorted(scores)
    if len(list) > 2:
        return personal_top_three(scores)
    elif len(list) == 2:
        score = [list[-1], list[-2]]
        return score
    return score






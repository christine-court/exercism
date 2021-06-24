from unittest.main import main


def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_three_scores = []
    for i in range(3):
        top_three_scores.append(max(scores))
        scores.remove(max(scores))
        if len(scores) == 0:
            break

    return top_three_scores


if __name__ == "__main__":
    personal_top_three([10, 20, 30])

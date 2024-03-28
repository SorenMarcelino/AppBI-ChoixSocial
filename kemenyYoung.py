import itertools
import matplotlib.pyplot as plt

def kemenyYoung(data):

    print(data[0])

    pair_matrix = {}

    for candidate1 in data[0]:
        for candidate2 in data[0]:
            if candidate1 != candidate2:  # To avoid pairs like ('a', 'a')
                key = candidate1 + candidate2
                pair_matrix[key] = 0

    for col in data:
        for i in range(0, len(data[col]) - 1):
            for j in range(i + 1, len(data[col])):
                if i != j:
                    key = data[col][i] + data[col][j]
                    pair_matrix[key] += 1

    print(pair_matrix)
    ranks = list(itertools.permutations(data[0]))

    #sum_dominating_pairs(ranks[0], pair_matrix)

    ranks_score = {}

    for rank in ranks:
        ranks_score[rank] = sum_dominating_pairs(rank, pair_matrix)
        #dominating_pairs_sum = sum_dominating_pairs(rank, pair_matrix)

    print(ranks_score)
    print(max(ranks_score, key=ranks_score.get))

    ranks_score = dict(sorted(ranks_score.items(), key=lambda item: item[1], reverse=True))

    # Extract keys and values for plotting
    keys = ["".join(rank) for rank in ranks_score.keys()]
    values = list(ranks_score.values())

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(keys, values)
    plt.xlabel('Ranks')
    plt.ylabel('Scores')
    plt.title('Histogram of Ranks with Scores')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('fig_kemenyYoung/histoKemenyYoung.png')

    return (max(ranks_score, key=ranks_score.get), ranks_score)

def sum_dominating_pairs(rank, pair_scores):
    rank_score = 0
    for i in range(0, len(rank) - 1):
        for j in range(i+1, len(rank)):
            key = rank[i] + rank[j]
            if key in pair_scores.keys():
                rank_score += pair_scores[key]
    return rank_score
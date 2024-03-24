import itertools
import matplotlib.pyplot as plt
import numpy as np


def kemeny_young(csv):
    nombre_de_colonnes = len(csv.columns)
    nombre_de_lignes = len(csv.index)
    votants = []

    for colonne in range(nombre_de_colonnes):
        votants.append(csv.iloc[:, colonne].tolist())

    candidats = set(itertools.chain.from_iterable(votants))
    permutations = itertools.permutations(candidats)

    scores = dict()
    for perm in permutations:
        score = 0
        for vote in votants:
            for i in range(len(vote)):
                for j in range(i + 1, len(vote)):
                    if perm.index(vote[i]) < perm.index(vote[j]):
                        score += 1
        scores[perm] = score

    max_score = max(scores.values())
    gagnants = [perm for perm, score in scores.items() if score == max_score]

    plot_results(gagnants, scores)

    return gagnants, max_score

def plot_results(gagnants, scores):
    # Plot des résultats de chaque candidat
    candidats = list(gagnants[0])
    scores_sorted = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    scores_values = [score for _, score in scores_sorted]
    positions = np.arange(len(scores))

    plt.figure(figsize=(10, 6))
    plt.barh(positions, scores_values, align='center')
    plt.yticks(positions, ["".join(cand) for cand, _ in scores_sorted])
    plt.xlabel('Score')
    plt.title('Résultats des candidats')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    #plt.show()

    # Matrice d'incidence pour visualiser les scores de chaque paire de candidats
    matrice_incidence = np.zeros((len(candidats), len(candidats)))
    for perm, score in scores.items():
        for i, cand1 in enumerate(perm):
            for j, cand2 in enumerate(perm):
                if i != j:
                    matrice_incidence[candidats.index(cand1)][candidats.index(cand2)] += score

    plt.figure(figsize=(8, 6))
    plt.imshow(matrice_incidence, cmap='viridis')
    plt.colorbar(label='Score')
    plt.title('Matrice d\'incidence')
    plt.xticks(np.arange(len(candidats)), candidats, rotation=45)
    plt.yticks(np.arange(len(candidats)), candidats)
    #plt.show()
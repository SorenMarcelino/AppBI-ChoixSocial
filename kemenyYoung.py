import itertools

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
                for j in range(i+1, len(vote)):
                    if (perm.index(vote[i]) < perm.index(vote[j])):
                        score += 1
        scores[perm] = score

    max_score = max(scores.values())
    gagnants = [perm for perm, score in scores.items() if score == max_score]

    return gagnants, max_score
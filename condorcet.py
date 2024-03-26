import itertools
import matplotlib.pyplot as plt

import pandas as pd
from pyparsing import results


def condorcet(csv, title):
    nombre_de_colonnes = len(csv.columns)
    nombre_de_lignes = len(csv.index)
    votants = []

    for colonne in range(nombre_de_colonnes):
        votants.append(csv.iloc[:, colonne].tolist())

    """
        Builds a dictionary of scores
        for each permutation of two candidates
    """
    candidates = set()
    scores = dict()
    for voting in votants:
        for candidate in voting:
            candidates.add(candidate)
        for pair in list(itertools.permutations(voting, 2)):
            if pair not in scores:
                scores[pair] = 0
            if voting.index(pair[0]) < voting.index(pair[1]):
                scores[pair] += 1
    #print(candidates)
    #print(scores)

    # Obtenir la liste des candidats uniques
    candidates = list(set(itertools.chain.from_iterable(scores.keys())))

    # Créer un DataFrame pandas avec les candidats en colonnes et en index
    df = pd.DataFrame(index=candidates, columns=candidates)

    # Remplir le DataFrame avec les scores des candidats
    for candidat1 in candidates:
        for candidat2 in candidates:
            if candidat1 != candidat2:
                score = scores.get((candidat1, candidat2), 0)
                df.loc[candidat1, candidat2] = score

    # Inférer les types d'objets
    df = df.infer_objects()

    # Remplacer les valeurs NaN par 0
    df.fillna(0, inplace=True)

    # Trier les lignes et les colonnes par ordre alphabétique
    df = df.sort_index(axis=0)
    df = df.sort_index(axis=1)

    #print("Matrice des scores :")
    #print(df)

    # Affichage du plot avec les valeurs des scores dans les cases
    plt.figure(figsize=(10, 8))  # Ajustement de la taille de la figure
    plt.imshow(df, cmap='coolwarm', interpolation='nearest')
    plt.colorbar(label='Score')
    plt.xticks(range(len(df.columns)), df.columns, rotation=45)
    plt.yticks(range(len(df.index)), df.index)
    for i in range(len(df.index)):
        for j in range(len(df.columns)):
            # Arrondir les valeurs à deux chiffres après la virgule
            plt.text(j, i, '{:.2f}'.format(df.iloc[i, j]), ha='center', va='center', color='black')
    plt.title("Matrice des scores de Condorcet")
    plt.xlabel("Candidats")
    plt.ylabel("Candidats")
    plt.tight_layout()  # Ajustement automatique de l'espacement
    plt.savefig(f'fig_condorcet/matrice_condorcet/matriceCondorcet_{title}.png', dpi=300)  # Augmentation de la résolution

    """
        Analyses the dictionary of scores and
        gives the winner of every pair of candidates
    """
    results = dict()
    for match in list(itertools.combinations(candidates, 2)):
        reverse = tuple(reversed(match))
        if scores[match] > scores[reverse]:
            results[match] = match[0]
        else:
            results[match] = match[1]

    """
        If a candidates is the winner against
        every other candidate, declares him the winner
        (Note: does not detect Condorcet cycles yet)
    """
    winners = set()
    for candidate in candidates:
        candidate_score = 0
        for result in results:
            if candidate in result and results[result] == candidate:
                candidate_score += 1
        if candidate_score == len(candidates) - 1:
            winners.add(candidate)

    if len(winners) == 1:
        print("Le gagnant de Condorcet est :", winners.pop())
    elif len(winners) > 1:
        print("Il y a une égalité entre les candidats suivants pour le gagnant de Condorcet :", winners)
    else:
        print("Aucun gagnant de Condorcet trouvé.")

    # Affichage du plot bar des résultats de Condorcet pour tous les candidats
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(candidates)), [list(results.values()).count(c) for c in candidates], align='center')
    plt.xticks(range(len(candidates)), candidates)
    plt.xlabel('Candidats')
    plt.ylabel('Nombre de victoires de Condorcet')
    plt.title('Résultats de Condorcet pour tous les candidats')
    plt.savefig(f'fig_condorcet/results_condorcet/resultsCondorcet_{title}.png')

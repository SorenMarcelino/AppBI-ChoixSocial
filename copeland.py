import itertools
import matplotlib.pyplot as plt
import pandas as pd


def copeland(csv, title):
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

    # Affichage du plot avec les valeurs des scores dans les cases
    plt.figure(figsize=(8, 6))
    plt.imshow(df, cmap='coolwarm', interpolation='nearest')
    plt.colorbar(label='Score')
    plt.xticks(range(len(df.columns)), df.columns, rotation=45)
    plt.yticks(range(len(df.index)), df.index)
    for i in range(len(df.index)):
        for j in range(len(df.columns)):
            plt.text(j, i, df.iloc[i, j], ha='center', va='center', color='black')
    plt.title("Matrice des scores de Condorcet")
    plt.xlabel("Candidats")
    plt.ylabel("Candidats")
    plt.savefig('fig_condorcet/matriceCondorcet.png')

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
        print("Aucun gagant de Condorcet trouvé.")

    # Affichage du nombre de duels gagnés et perdus par chaque candidat
    duels_gagnes = {candidate: 0 for candidate in candidates}
    duels_perdus = {candidate: 0 for candidate in candidates}
    for result in results.values():
        duels_gagnes[result] += 1

    for candidate in candidates:
        duels_perdus[candidate] = len(candidates) - 1 - duels_gagnes[candidate]

    #print("Nombre de duels gagnés par chaque candidat :")
    #for candidate, wins in duels_gagnes.items():
        #print(f"{candidate}: {wins}")

    #print("Nombre de duels perdus par chaque candidat :")
    #for candidate, losses in duels_perdus.items():
        #print(f"{candidate}: {losses}")

    # Calcul de la différence entre le nombre de duels gagnés et perdus
    differences = {candidate: duels_gagnes[candidate] - duels_perdus[candidate] for candidate in candidates}

    max_difference = max(differences.values())
    max_candidate = [candidate for candidate, diff in differences.items() if diff == max_difference][0]
    print("La valeur la plus élevée dans differences est :", max_candidate, "avec un résultat de Copeland de", max_difference)

    print("Différence (nombre de duels gagnés - nombre de duels perdus) pour chaque candidat :")
    for candidate, diff in differences.items():
        print(f"{candidate}: {diff}")

    # Trier les candidats par ordre alphabétique
    sorted_candidates = sorted(candidates)

    # Affichage du plot bar des résultats de Condorcet pour tous les candidats
    #plt.figure(figsize=(10, 6))
    #plt.bar(range(len(sorted_candidates)), [list(results.values()).count(c) for c in sorted_candidates], align='center')
    #plt.xticks(range(len(sorted_candidates)), sorted_candidates)
    #plt.xlabel('Candidats')
    #plt.ylabel('Nombre de victoires de Condorcet')
    #plt.title('Résultats de Condorcet pour tous les candidats')
    #plt.savefig('fig_condorcet/resultsCondorcet.png')

    # Affichage du plot bar de la différence (nombre de duels gagnés - nombre de duels perdus) pour chaque candidat
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(sorted_candidates)), [differences[candidate] for candidate in sorted_candidates], align='center')
    plt.xticks(range(len(sorted_candidates)), sorted_candidates)
    plt.xlabel('Candidats')
    plt.ylabel('Différence (Nombre de duels gagnés - Nombre de duels perdus)')
    plt.title('Différence entre les duels gagnés et les duels perdus pour chaque candidat')
    plt.axhline(0, color='gray', linestyle='-', linewidth=0.8)  # Ajout de la ligne à l'abscisse 0
    plt.tight_layout()  # Ajustement de la disposition
    plt.savefig(f'fig_copeland/resultatsCopeland_{title}.png')

import matplotlib.pyplot as plt


def voteDeuxTours(csv):
    # Deux gagnants du premier tour
    premiere_ligne = csv.iloc[0]
    occurrences = premiere_ligne.value_counts()
    # print(occurrences)

    deux_plus_frequents = occurrences.nlargest(2)

    # Afficher le gagnant
    print(f"Les gagnants du premier tour sont :\n"
          f" {deux_plus_frequents.index[0]} avec {occurrences[deux_plus_frequents.index[0]]} votes\n"
          f" {deux_plus_frequents.index[1]} avec {occurrences[deux_plus_frequents.index[1]]} votes")

    # Gagnant du second tour
    valeur_a_supprimer1 = deux_plus_frequents.index[0]
    valeur_a_supprimer2 = deux_plus_frequents.index[1]
    csv = csv.drop(columns=csv.columns[csv.iloc[0] == valeur_a_supprimer1])
    csv = csv.drop(columns=csv.columns[csv.iloc[0] == valeur_a_supprimer2])

    while True:
        if (valeur_a_supprimer1 in csv.iloc[0].values) or (valeur_a_supprimer2 in csv.iloc[0].values):
            if not csv.empty:
                premiere_ligne = csv.iloc[0]
                occurrences[deux_plus_frequents.index[0]] += (premiere_ligne == deux_plus_frequents.index[0]).sum()
                occurrences[deux_plus_frequents.index[1]] += (premiere_ligne == deux_plus_frequents.index[1]).sum()
                # print(csv)
            else:
                # print("CSV vide, sortie de la boucle.")
                break

            if valeur_a_supprimer1 in csv.iloc[0].values:
                csv = csv.drop(columns=csv.columns[csv.iloc[0] == valeur_a_supprimer1])
            if valeur_a_supprimer2 in csv.iloc[0].values:
                csv = csv.drop(columns=csv.columns[csv.iloc[0] == valeur_a_supprimer2])
        else:
            csv = csv.iloc[1:, :]
            if csv.empty:
                # print("CSV vide, sortie de la boucle.")
                break

    if occurrences[deux_plus_frequents.index[0]] > occurrences[deux_plus_frequents.index[1]]:
        print(f"Le gagnant du second tour est :\n"
              f" {deux_plus_frequents.index[0]} avec {occurrences[deux_plus_frequents.index[0]]} votes")
    else:
        print(f"Le gagnant du second tour est :\n"
              f" {deux_plus_frequents.index[1]} avec {occurrences[deux_plus_frequents.index[1]]} votes")

    candidats = list(deux_plus_frequents.index)
    sorted_candidates = sorted(candidats)  # Trier les candidats par ordre alphabétique
    votes = [occurrences[candidat] for candidat in sorted_candidates]

    # Création du barplot
    plt.bar(sorted_candidates, votes, color=['blue', 'green'])  # Couleur différente pour chaque barre
    plt.xlabel('Candidats')
    plt.ylabel('Nombre de votes')
    plt.title('Résultats du second tour')
    plt.savefig('fig_voteDeuxTours/voteDeuxTours')

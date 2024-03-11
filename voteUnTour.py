import matplotlib.pyplot as plt


def voteUnTour(csv):
    premiere_ligne = csv.iloc[0]
    occurrences = premiere_ligne.value_counts()
    # print(occurrences)

    gagnant = occurrences.idxmax()

    # Afficher le gagnant
    print(f"Le gagnant du vote à 1 tour est : {gagnant} avec {occurrences[gagnant]} votes.")

    occurrences.plot(kind='bar')

    # Ajouter des étiquettes au diagramme
    plt.xlabel('Candidats')
    plt.ylabel('Voix')
    plt.title('Nombre de voix pour chaque candidat')

    # Afficher le diagramme
    plt.savefig('fig_voteUnTour/voteUnTour.png')


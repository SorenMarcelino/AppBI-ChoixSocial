import matplotlib.pyplot as plt


def voteUnTour(csv, title, is_merge):
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
    plt.title(f'Nombre de voix pour chaque candidat : {title}')

    # Afficher le diagramme
    if is_merge:
        plt.savefig(f'classements_des_saisons_en_fonction_des_methodes_sur_les_courses/voteUnTour_{title}.png')
    else:
        plt.savefig(f'fig_voteUnTour/voteUnTour_{title}.png')
    plt.close()


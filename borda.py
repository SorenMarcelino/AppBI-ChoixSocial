from matplotlib import pyplot as plt


def methodeBorda(data):
    result = init_dict(data)
    for x, y in data.items():
        point = len(y)
        for z in y:
            result[x] += point * z
            point -= 1
    print(result)

    return result


def vainqueurBorda(data):
    winning_key = ""
    winning_value = 0
    for x, y in data.items():
        if y > winning_value:
            winning_key = x
            winning_value = y

    return "Le gagnant de la méthode de Borda est: " + str(winning_key) + " avec un total de: " + str(winning_value) + " points."


def classementBorda(data):
    ranks = dict(sorted(data.items(), key=lambda key_val: key_val[1], reverse=True))
    print("Le classement de Borda est le suivant: ")
    print(ranks)

    # Extraire les noms des candidats et leurs scores
    candidates = list(ranks.keys())
    scores = list(ranks.values())

    # Créer le barplot
    plt.figure(figsize=(10, 6))
    plt.bar(candidates, scores, color='skyblue')

    # Ajouter des titres et étiquettes
    plt.title('Classement de Borda')
    plt.xlabel('Candidats')
    plt.ylabel('Scores')
    plt.xticks(rotation=45)  # Rotation des étiquettes sur l'axe x pour une meilleure lisibilité
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Afficher le barplot
    plt.tight_layout()
    plt.savefig("fig_borda/borda.png")


def init_dict(data):
    result = {}
    for x in data.keys():
        result[x] = 0
    return result

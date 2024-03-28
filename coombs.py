import matplotlib.pyplot as plt
import numpy as np

def vote_alternatif_coombs(data_frame, cols):
    clone = data_frame.copy()
    majority = cols / 2

    participants = {}
    participantsWinner = {}
    loosers = []
    tours = {}
    toursWinner = {}
    labelTour = 1
    for x in clone[list(clone)[0]]:
        participants[x] = 0
        participantsWinner[x] = 0
    winner = None
    while True:
        for x in participants.keys():
            participants[x] = 0
            participantsWinner[x] = 0
        for x, y in clone.items():
            reversedVal = y.copy().tolist()
            reversedVal.reverse()
            val = find_non_loser(reversedVal, loosers)
            valWinner = find_non_loser(y, loosers)
            participants[val] += 1
            participantsWinner[valWinner] += 1

        loosing_value = 0
        loosing_key = None
        for x, y in participants.items():
            if participantsWinner[x] > majority:
                return x
            if loosing_key is None or y > loosing_value:
                loosing_key = x
                loosing_value = y

        del participants[loosing_key]
        del participantsWinner[loosing_key]
        loosers.append(loosing_key)


def vote_alternatif_classement_coombs(data_frame):
    clone = data_frame.copy()
    participants = {}
    participantsWinner = {}
    loosers = []
    tours = {}
    toursWinner = {}
    labelTour = 1
    for x in clone[list(clone)[0]]:
        participants[x] = 0
        participantsWinner[x] = 0
    while len(participants.keys()) > 0:
        for x in participants.keys():
            participants[x] = 0
            participantsWinner[x] = 0
        for x, y in clone.items():
            reversedVal = y.copy().tolist()
            reversedVal.reverse()
            val = find_non_loser(reversedVal, loosers)
            valWinner = find_non_loser(y, loosers)
            if val is not None:
                participants[val] += 1
                participantsWinner[valWinner] += 1

        tours[labelTour] = participants.copy()
        toursWinner[labelTour] = participantsWinner.copy()
        loosing_value = 0
        loosing_key = None
        for x, y in participants.items():
            if loosing_key is None or y > loosing_value:
                loosing_key = x
                loosing_value = y

        labelTour += 1

        del participants[loosing_key]
        del participantsWinner[loosing_key]
        loosers.append(loosing_key)

    coombs_plot(tours, toursWinner)

    loosers.reverse()
    return loosers

def find_non_loser(y, loosers):
    for item in y:
        if item not in loosers:
            return item
    return None

def coombs_plot(data, dataWinner):
    participants = set(participant for tour in data.values() for participant in tour.keys())
    tours = sorted(data.keys())
    pourcentages = {participant: [] for participant in participants}
    pourcentagesWinner = {participant: [] for participant in participants}

    stopAt = None
    once = False
    # Calcul des pourcentages pour chaque participant à chaque tour
    for tour in tours:
        total_votes = sum(data[tour].values())
        for participant in participants:
            votes = data[tour].get(participant, 0)  # Obtenir le nombre de votes du participant pour ce tour
            votesWinner = dataWinner[tour].get(participant, 0)  # Obtenir le nombre de votes du participant pour ce tour
            pourcentage = (votes / total_votes) * 100 if total_votes != 0 else 0  # Calculer le pourcentage
            pourcentageWinner = (votesWinner / total_votes) * 100 if total_votes != 0 else 0  # Calculer le pourcentage
            pourcentages[participant].append(pourcentage)
            pourcentagesWinner[participant].append(pourcentageWinner)
            if max(pourcentagesWinner[participant]) > 50 and once is not True:
                once = True
                stopAt = tour


    if stopAt is not None:
        while tours[-1] != stopAt:
            tours.pop()
            for x in pourcentages.keys():
                pourcentages[x].pop()
                pourcentagesWinner[x].pop()

    # Création des données pour les barres empilées
    stacked_data = np.zeros((len(tours), len(participants)))
    stacked_data2 = np.zeros((len(tours), len(participants)))

    for i, participant in enumerate(participants):
        stacked_data[:, i] = pourcentages[participant]
        stacked_data2[:, i] = pourcentagesWinner[participant]

    # Création de l'histogramme empilé
    plt.figure(figsize=(10, 6))
    x = np.arange(len(tours))  # Positions des tours sur l'axe x
    width = 0.5  # Largeur des barres

    bottom = np.zeros(len(tours))  # Position de départ pour chaque participant

    for i, participant in enumerate(participants):
        plt.bar(x, stacked_data[:, i], bottom=bottom, label=participant)
        bottom += stacked_data[:, i]

    plt.axhline(y=50, color='yellow', linestyle='--', linewidth=0.5, label='Majorité')

    plt.xlabel('Tour')
    plt.ylabel('Pourcentage du nombre de voix')
    plt.title('Pourcentage du nombre de voix donnant le participant en dernière place à chaque tour')
    plt.xticks(x, tours)
    plt.legend()
    plt.grid(True)
    plt.savefig('fig_coombs/coombs_dernier.png')

    # Création de l'histogramme empilé
    plt.figure(figsize=(10, 6))
    x = np.arange(len(tours))  # Positions des tours sur l'axe x
    width = 0.5  # Largeur des barres

    bottom = np.zeros(len(tours))  # Position de départ pour chaque participant

    for i, participant in enumerate(participants):
        plt.bar(x, stacked_data2[:, i], bottom=bottom, label=participant)
        bottom += stacked_data2[:, i]

    plt.axhline(y=50, color='yellow', linestyle='--', linewidth=0.5, label='Majorité')

    plt.xlabel('Tour')
    plt.ylabel('Pourcentage du nombre de voix')
    plt.title('Pourcentage du nombre de voix donnant le participant en première place à chaque tour')
    plt.xticks(x, tours)
    plt.legend()
    plt.grid(True)
    plt.savefig('fig_coombs/coombs_premier.png')

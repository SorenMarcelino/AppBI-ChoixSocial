import math
from collections import defaultdict


def vainqueurAlternative(data):
    clone = data.copy()
    loosing_key = ''
    loosing_value = -1
    while len(clone) > 1:
        for x, y in clone.items():
            if loosing_value == -1:
                loosing_key = x
                loosing_value = y[0]
            elif y[0] < loosing_value:
                loosing_key = x
                loosing_value = y[0]
        del clone[loosing_key]
        loosing_key = ''
        loosing_value = -1

    winner_key = ""
    for x in clone.keys():
        winner_key = x
    print("Le gagnant du vote avec la méthode alternative est: " + winner_key)


def classementAlternative(data):
    clone = data.copy()
    ranks = []
    loosing_key = ''
    loosing_value = -1
    while len(clone) > 1:
        for x, y in clone.items():
            if loosing_value == -1:
                loosing_key = x
                loosing_value = y[0]
            elif y[0] < loosing_value:
                print(str(y[0]) + " < " + str(loosing_value))
                loosing_key = x
                loosing_value = y[0]
        ranks.append(loosing_key)
        del clone[loosing_key]
        loosing_key = ''
        loosing_value = -1

    ranks.append(clone.popitem()[0])
    ranks.reverse()
    final_ranks = ""
    print("Le classement du vote avec la méthode alternative est: ")
    for x in ranks:
        final_ranks += str(x) + " > "

    final_ranks = final_ranks[:-3]
    print(final_ranks)


def vote_alternatif(data_frame, cols):
    clone = data_frame.copy()
    majority = cols / 2

    participants = {}
    loosers = []
    for x in clone[list(clone)[0]]:
        participants[x] = 0
    winner = None
    while True:
        for x in participants.keys():
            participants[x] = 0
        for x, y in clone.items():
            val = find_non_loser(y, loosers)
            participants[val] += 1

        loosing_value = 0
        loosing_key = None
        for x, y in participants.items():
            if y > majority:
                return x
            if loosing_key is None or y < loosing_value:
                loosing_key = x
                loosing_value = y

        del participants[loosing_key]
        loosers.append(loosing_key)


def vote_alternatif_classement(data_frame):
    clone = data_frame.copy()
    participants = {}
    loosers = []
    for x in clone[list(clone)[0]]:
        participants[x] = 0
    while len(participants.keys()) > 0:
        for x in participants.keys():
            participants[x] = 0
        for x, y in clone.items():
            val = find_non_loser(y, loosers)
            participants[val] += 1

        loosing_value = 0
        loosing_key = None
        for x, y in participants.items():
            if loosing_key is None or y < loosing_value:
                loosing_key = x
                loosing_value = y

        del participants[loosing_key]
        loosers.append(loosing_key)

    loosers.reverse()
    return loosers

def find_non_loser(y, loosers):
    for item in y:
        if item not in loosers:
            return item
    return None
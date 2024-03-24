def vote_alternatif_coombs(data_frame, cols):
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
            reversedVal = y.copy().tolist()
            reversedVal.reverse()
            val = find_non_loser(reversedVal, loosers)
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


def vote_alternatif_classement_coombs(data_frame):
    clone = data_frame.copy()
    participants = {}
    loosers = []
    for x in clone[list(clone)[0]]:
        participants[x] = 0
    while len(participants.keys()) > 0:
        for x in participants.keys():
            participants[x] = 0
        for x, y in clone.items():
            reversedVal = y.copy().tolist()
            reversedVal.reverse()
            val = find_non_loser(reversedVal, loosers)
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
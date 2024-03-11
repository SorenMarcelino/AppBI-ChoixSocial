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


def init_dict(data):
    result = {}
    for x in data.keys():
        result[x] = 0
    return result

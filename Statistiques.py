import matplotlib.pyplot as plt


def size_of_dataset(data):
    row = len(data)
    columns = len(data.columns)
    return [row, columns]


def is_classement_uniq(data):
    codex = []
    occurence = []
    for column in data.columns[0:]:
        classement = []
        for val in data[column]:
            if isinstance(val, int):
                classement.append(str(val))
            else:
                classement.append(val)

        if classement not in codex:
            codex.append(classement)
            occurence.append(1)
        else:
            i = codex.index(classement)
            occurence[i] += 1

    return [codex, occurence]


def frequency_per_ranks_per_crit(data):
    dim = size_of_dataset(data)
    crits = is_classement_uniq(data)
    rslt = {}
    id = 0
    for x in crits[0]:
        if id == 0:
            for y in x:
                rslt[y] = []
                for z in range(0, len(x)):
                    rslt[y].append(0)

        index = 0
        for y in x:
            rslt[y][index] += 1 * crits[1][id]
            index += 1

        id += 1

    return rslt


def plot_frequency(data):
    pos = 0
    position = []

    for x in data.keys():
        position.append(pos)
        pos += 1

    print(data.keys(), data.values())

    for x, y in data.items():
        print(x,y)
        plt.plot(position, y, label=x)

    plt.legend()
    plt.show()

    fig, ax = plt.subplots()
    for x, y in data.items():
        ax.bar(position, y, width=1, edgecolor="white", linewidth=0.7)
        plt.legend = x
        plt.show()
        fig, ax = plt.subplots()
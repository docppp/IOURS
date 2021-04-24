import matplotlib.pyplot as plt
from ioumath import calculateHeals, getBestRunes


def plotHeals(pet1, pet2, bonus, rune):
    levels_list = list(range(290, 290+50))
    heals_list = []
    for i in range(290, 290+50):
        heals_list.append(calculateHeals(pet1, pet2, bonus, rune, i))

    print(levels_list)
    print(heals_list)
    fig, ax = plt.subplots()
    ax.plot(levels_list, heals_list)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()
    fig.savefig("test.png")
    plt.show()

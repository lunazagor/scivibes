import numpy as np
import matplotlib.pyplot as plt

def plot_vibestogram(vibes,vibe_color):

    # get the vibes in a format matplotlib can understand
    vibenames = []
    vibescores = []

    for vibe in vibes:
        vibenames.append(vibe[0])
        vibescores.append(vibe[1])

    # get the right bar colors
    barcolors = []

    for vibe in vibenames:
        barcolors.append(np.asarray(vibe_color[vibe]['Med'])/255)

    pos = np.arange(len(vibenames))
    width = 1.0

    fig, ax = plt.subplots(1, figsize=(16, 8))
    ax.barh(vibenames, vibescores, width, color=barcolors, edgecolor='black')

    # turn off the right spine/ticks
    #ax.spines['right'].set_color('none')
    #ax.yaxis.tick_left()

    # set the y-spine
    #ax.spines['bottom'].set_position('zero')

    # turn off the top spine/ticks
    #ax.spines['top'].set_color('none')
    #ax.xaxis.tick_bottom()

    for tick in ax.get_xticklabels():
        tick.set_rotation(90)

    #plt.setp(ax.xaxis.get_majorticklabels(), ha='right')    

    fig.suptitle("vibe check!! your total vibes")

    fig.savefig("vibestogram.jpg")

    return fig, ax
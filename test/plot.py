# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
plt.rcdefaults()

import numpy as np
import matplotlib.pyplot as plt


def draw_plot(items, perfs, xlabel, title, ytricks):
    y_pos = np.arange(len(items))
    error = np.random.rand(len(items))

    plt.figure(1)
    plt.barh(y_pos, perfs, xerr=error, height=0.4, align='center', alpha=0.4)
    plt.yticks(y_pos, ytricks)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.grid(True)

    plt.show()


def main(xlabel, title):
    items = []
    ytricks = []
    perfs = []

    with open('./profile.txt', 'rb') as f:
        for line in f:
            name, data = line.strip().split('|')
            items.append(name)
            ytricks.append(name)
            perfs.append(float(data))

    draw_plot(items, perfs, xlabel, title, ytricks)


if __name__ == '__main__':
    main('Response Time: ms', 'Average Reponse Time of Major APIs')

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def basic_seaborn():
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.figure(figsize=(8, 4))

    sns.set_style('darkgrid')
    sns.lineplot(x=x, y=y1, label='sin(x)', color='blue')
    sns.lineplot(x=x, y=y2, label='cos(x)', color='orange')
    plt.title(f"Линейный график в стиле '{"darkgrid"}'", fontsize=14)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

    plt.figure(figsize=(8, 4))
    sns.set_style('ticks')
    sns.lineplot(x=x, y=y1, label='sin(x)', color='blue')
    sns.lineplot(x=x, y=y2, label='cos(x)', color='orange')
    plt.title(f"Линейный график в стиле '{"ticks"}'", fontsize=14)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()


def adv_seaborn_1(data):
    x = np.random.rand(50)
    y = x * 2 + np.random.normal(0, 0.1, 50)

    plt.figure(figsize=(9, 9))
    plt.subplot(221)
    sns.scatterplot(x=x, y=y, s=70)
    plt.title("Точечный график", fontsize=14)
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.subplot(222)
    sns.histplot(data[2], bins=30, kde=True, color="purple")
    plt.title("Гистограмма", fontsize=14)
    plt.xlabel("Значения")
    plt.ylabel("Частота")

    plt.subplot(223)
    sns.barplot(x=data[4], y=data[5])
    plt.title("Столбчатая диаграмма", fontsize=14)
    plt.xlabel("Категории")
    plt.ylabel("Значения")
    plt.show()


def adv_seaborn_2(data):
    data = np.random.normal(0, 1, 100)

    plt.figure(figsize=(9, 9))
    plt.subplot(221)
    sns.boxplot(data=data, color="skyblue")
    plt.title("Диаграмма размаха", fontsize=14)

    data = np.random.rand(10, 10)
    plt.subplot(222)
    sns.heatmap(data, cmap="coolwarm", annot=True, fmt=".2f")
    plt.title("Тепловая карта", fontsize=14)

    plt.subplot(223)
    sns.lineplot(x=data[0], y=data[1], color="blue", label="sin(x)")
    plt.fill_between(data[0], data[1], color="lightblue", alpha=0.5)
    plt.title("Областной график", fontsize=14)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()

    plt.show()

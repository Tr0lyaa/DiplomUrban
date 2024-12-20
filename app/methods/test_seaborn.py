import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def basic_seaborn(data):
    plt.figure(figsize=(8, 4))

    sns.set_style('darkgrid')
    sns.lineplot(x=data[0], y=data[1], label='sin(x)', color='blue')
    sns.lineplot(x=data[0], y=data[3], label='cos(x)', color='orange')
    plt.title(f"Линейный график в стиле 'darkgrid'", fontsize=14)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

    plt.figure(figsize=(8, 4))
    sns.set_style('ticks')
    sns.lineplot(x=data[0], y=data[1], label='sin(x)', color='blue')
    sns.lineplot(x=data[0], y=data[3], label='cos(x)', color='orange')
    plt.title(f"Линейный график в стиле 'ticks'", fontsize=14)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()


def adv_seaborn_1(data, df):
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
    sns.barplot(x=df["Сезон"], y=df["Прибыль"])
    plt.title("Столбчатая диаграмма", fontsize=14)
    plt.xlabel("Категории")
    plt.ylabel("Значения")
    plt.show()


def adv_seaborn_2(data):
    data1 = np.random.normal(0, 1, 100)

    plt.figure(figsize=(9, 9))
    plt.subplot(221)
    sns.boxplot(data=data1, color="skyblue")
    plt.title("Диаграмма размаха", fontsize=14)

    data2 = np.random.rand(10, 10)
    plt.subplot(222)
    sns.heatmap(data2, cmap="coolwarm", annot=True, fmt=".2f")
    plt.title("Тепловая карта", fontsize=14)

    plt.subplot(223)
    sns.lineplot(x=data[0], y=data[1], color="blue", label="sin(x)")
    plt.fill_between(data[0], data[1], color="lightblue")
    plt.title("Областной график", fontsize=14)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()

    plt.show()

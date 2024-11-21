import numpy as np
import matplotlib.pyplot as plt


def basic_plot(data):
    plt.figure(figsize=(9, 9))

    plt.subplot(221)
    plt.plot(data[0], data[1], 'bs', data[0], data[2], 'g^')
    plt.title('График 1')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.subplot(222)
    plt.plot(data[0], data[1], 'b--')
    plt.title('График 2')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.subplot(223)
    plt.plot(data[0], data[2], "g^")
    plt.title('График 3')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.plot(data[0], data[1], 'bs', data[0], data[2], 'g^')
    plt.title('График 3.2')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.suptitle("Название группы графиков")
    plt.show()


def adv_plot_1(data):
    plt.figure(figsize=(9, 9))

    plt.subplot(221)
    plt.scatter(data[0], data[1], label="sin(x)", color='r')
    plt.title("Точечный график")
    plt.legend()

    plt.subplot(222)
    plt.hist(data[2], bins=20, color='g')
    plt.title("Гистограмма")

    plt.subplot(223)
    plt.bar(data[4], data[5], color='b')
    plt.title("Столбчатая диаграмма")

    plt.subplot(224)
    plt.pie(data[5], labels=data[4], autopct='%1.1f%%', colors=['c', 'm', 'y', 'b'])
    plt.title("Круговая диаграмма")

    plt.show()


def adv_plot_2(data):
    plt.figure(figsize=(9, 9))

    plt.subplot(221)
    plt.fill_between(data[0], data[1], color="skyblue", alpha=0.4)
    plt.plot(data[0], data[1], color="Slateblue", alpha=0.6)
    plt.title("Областной график")

    plt.subplot(222)
    y_err = 0.1 + 0.2 * np.sqrt(data[0])
    plt.errorbar(data[0], data[1], yerr=y_err, fmt='-o', ecolor='gray', alpha=0.6, label='Error Bars')
    plt.title("График ошибок")
    plt.legend()

    plt.subplot(223)
    heatmap_data = np.random.rand(10, 10)
    plt.imshow(heatmap_data, cmap='hot', interpolation='nearest')
    plt.title("Тепловая карта")

    plt.subplot(224)
    plt.boxplot(data[2], vert=False)
    plt.title("Диаграмма размаха")

    plt.show()

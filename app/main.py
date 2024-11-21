from methods import *
from database import initiate_db, get_all_data
import numpy as np
import pandas as pd

initiate_db()

# Первый набор данных - для показательной реализации библиотек.
data1 = np.array([[1, 2, 3, 4, 5], [1, 1, 1, 0, 1], [1, 3, 5, 7, 9]])
# Второй набор данных - различные данные для реализации множества разных графиков из библиотек.
x = np.linspace(0, 10, 100)
data2 = [x, np.sin(x), np.random.randn(1000), np.cos(x), ['A', 'B', 'C', 'D'], [3, 7, 8, 5]]
# Набор данных для работы pandas.
df1 = pd.DataFrame(get_all_data("data_1"), columns=["ID", "Сезон", "Прибыль"])
# df2 = pd.DataFrame(get_all_data("data_2"), columns=["ID", "День", "Число продаж", "Продавец"])

input_text = ("Для примеров Matplotlib, введите 1\nДля примеров Seaborn, введите 2\nДля примеров Plotly, введите 3\n"
              "Для выхода, введите 0\n")
test_number = input(input_text)

while test_number != "0":
    if test_number not in ["0", "1", "2", "3"]:
        test_number = input("Неверное значение! Попробуйте ещё раз.\n")
        continue
    elif test_number == "1":
        basic_plot(data1)
        adv_plot_1(data2)
        adv_plot_2(data2)
        test_number = input(input_text)
    elif test_number == "2":
        basic_seaborn()
        adv_seaborn_1(data2, df1)
        adv_seaborn_2(data2)
        test_number = input(input_text)
    elif test_number == "3":
        basic_plotly()
        adv_plotly()
        test_number = input(input_text)

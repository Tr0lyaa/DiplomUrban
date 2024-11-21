import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd


def basic_plotly():
    sizes = [25, 35, 20, 20]
    labels = ['A', 'B', 'C', 'D']

    fig = px.pie(values=sizes, names=labels, title="Круговая диаграмма в Plotly")
    fig.show()

    data = np.random.rand(10, 10)
    fig = px.imshow(data, title="Тепловая карта в Plotly")
    fig.show()

    categories = ['A', 'B', 'C', 'D']
    values = [5, 7, 3, 8]
    df = pd.DataFrame({'Category': categories, 'Values': values})
    fig = px.bar(df, x='Category', y='Values', title="Столбчатая диаграмма в Plotly")
    fig.show()

    x = np.random.rand(100)
    y = x * 2 + np.random.normal(0, 0.1, 100)
    fig = px.scatter(x=x, y=y, title="Точечный график в Plotly")
    fig.show()

    data = np.random.normal(0, 1, 1000)
    fig = px.histogram(data, nbins=30, title="Гистограмма в Plotly")
    fig.show()


def adv_plotly():
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    data_hist = np.random.normal(0, 1, 1000)
    categories = ['A', 'B', 'C', 'D']
    values = [5, 7, 3, 8]

    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=("Линейный график", "Гистограмма", "Точечный график", "Столбчатая диаграмма"),
    )

    fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name="sin(x)"), row=1, col=1)
    fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name="cos(x)", line=dict(color='red')), row=1, col=1)

    fig.add_trace(go.Histogram(x=data_hist, nbinsx=30, name="Гистограмма"), row=1, col=2)

    fig.add_trace(go.Scatter(x=x, y=y1 + np.random.normal(0, 0.1, len(x)), mode='markers', name="Точечный график"),
                  row=2, col=1)

    fig.add_trace(go.Bar(x=categories, y=values, name="Столбчатая диаграмма"), row=2, col=2)

    fig.update_layout(
        title="Объединённые графики в Plotly",
        showlegend=True,
        height=800,
        width=800,
    )

    fig.show()

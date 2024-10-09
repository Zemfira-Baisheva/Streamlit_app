import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import altair as alt
from vega_datasets import data


st.write("""# Исследование по чаевым""")

file = st.sidebar.file_uploader("Загрузите CSV-файл", type="csv")
if file is not None:
    tips = pd.read_csv(file)
    st.write(tips.head(5))
else:
    st.stop()

st.write("""## Создайте столбец `time_order`
Заполните его случайной датой в промежутке от 2023-01-01 до 2023-01-31
         """)

button_1 = st.button('Заполнить столбец')
if button_1:
    tips['time_order'] = np.random.choice(pd.date_range('2023-01-01', '2023-01-31'), 244)
st.write(tips.head(5))

st.write("""### 1. Постройте график показывающий динамику чаевых во времени""")

button_2 = st.button('Построить график')
if button_2:
    tips['time_order'] = np.random.choice(pd.date_range('2023-01-01', '2023-01-31'), 244)
    tips_copy = tips.copy()
    st.line_chart(data = tips_copy, x = "time_order", y = "tip", color = "#ffaa00", x_label = "Даты", y_label = "Сумма чаевых")
    sns.relplot(data = tips_copy, x = 'time_order', y = "tip", kind = 'line', height=10)
    plt.savefig('chart_1.png')
    plt.show()
    with open('chart_1.png', "rb") as img:
        button = st.sidebar.download_button(label = "Скачать текущий график",
                                            data = img,
                                            mime = "image/png")


st.write("""### 2. Нарисуйте гистограмму `total_bill` """)
button_3 = st.button('Построить гистограмму')
if button_3:
    fig, ax = plt.subplots()
    ax.hist(data = tips, x = 'total_bill')
    st.pyplot(fig)
    sns.displot(data = tips, x = 'total_bill')
    plt.savefig('chart_2.png')
    plt.show()
    with open('chart_2.png', "rb") as img:
        button = st.sidebar.download_button(label = "Скачать текущий график",
                                            data = img,
                                            mime = "image/png")


st.write("""### 3. Нарисуйте scatterplot, показывающий связь между `total_bill` and `tip` """)
button_4 = st.button('Построить scatterplot')
if button_4:
    st.scatter_chart(data = tips, x = 'total_bill', y = 'tip')
    sns.scatterplot(data = tips, x = 'total_bill', y = 'tip')
    plt.savefig('chart_3.png')
    plt.show()
    with open('chart_3.png', "rb") as img:
        button = st.sidebar.download_button(label = "Скачать текущий график",
                                            data = img,
                                            mime = "image/png")


st.write("""### 4. Нарисуйте 1 график, связывающий `total_bill`, `tip`, и `size`""")
button_5 = st.button("Нарисовать график")
if button_5:
    st.scatter_chart(tips, x = 'total_bill', y = 'tip', size ='size', color = "#FF0000")
    sns.relplot(data = tips, x = 'total_bill', y = 'tip', kind = 'scatter', size ='size', color = "#FF0000")
    plt.savefig('chart_4.png')
    plt.show()
    with open('chart_4.png', "rb") as img:
        button = st.sidebar.download_button(label = "Скачать текущий график",
                                            data = img,
                                            mime = "image/png")
    

st.write("""### 5. Покажите связь между днем недели и размером счета""")
button_6 = st.button("Показать")
if button_6:
    fig, ax = plt.subplots()
    st.scatter_chart(data = tips, x = 'day', y = 'total_bill')
    sns.relplot(data = tips, x = 'day', y = 'total_bill', kind = 'scatter')
    plt.savefig('chart_5.png')
    plt.show()
    with open('chart_5.png', "rb") as img:
        button = st.sidebar.download_button(label = "Скачать текущий график",
                                            data = img,
                                            mime = "image/png")


st.write("""### 6. Нарисуйте `scatter plot` с днем недели по оси **Y**, чаевыми по оси **X**, и цветом по полу""")
button_7 = st.button("Нарисовать scatter plot")
if button_7:
    st.scatter_chart(tips, x = 'tip',y = 'day', color = 'sex')
    sns.relplot(data = tips, x = 'tip', y = 'day', kind = 'scatter', hue = 'sex', color = "blue")
    plt.savefig('chart_6.png')
    plt.show()
    with open('chart_6.png', "rb") as img:
        button = st.sidebar.download_button(label = "Скачать текущий график",
                                            data = img,
                                            mime = "image/png")

st.write("""### 7. Нарисуйте `box plot` c суммой всех счетов за каждый день, разбивая по `time` (Dinner/Lunch)""")
button_8 = st.button("Построить box plot")
if button_8:
    fig, ax = plt.subplots()
    sns.boxplot(data = tips, x = 'total_bill', y = "day", hue = 'time')
    st.pyplot(fig)
    plt.savefig('chart_7.png')
    plt.show()
    with open('chart_7.png', "rb") as img:
        button = st.sidebar.download_button(label = "Скачать текущий график",
                                            data = img,
                                            mime = "image/png")


st.write("### 8. Нарисуйте 2 гистограммы чаевых на обед и ланч. Расположите их рядом по горизонтали")
button_9 = st.button("Построить 2 гистограммы")
if button_9:
    fig, ax = plt.subplots()
    sns.displot(data = tips, x = 'tip', kind = 'hist', col='time')
    plt.savefig('chart_8.png')
    plt.show()
    st.pyplot()
    with open('chart_8.png', "rb") as img:
        button = st.sidebar.download_button(label = "Скачать текущий график",
                                            data = img,
                                            mime = "image/png")


st.write("""### 9. Нарисуйте 2 scatterplots (для мужчин и женщин), показав связь размера счета и чаевых, дополнительно разбив по курящим/некурящим. Расположите их по горизонтали""")
button_10 = st.button("Построить 2 scatterplots")
if button_10:
    fig, ax = plt.subplots()
    sns.relplot(data = tips, x = 'total_bill', y = 'tip', col = 'sex', kind = 'scatter', hue = 'smoker')
    plt.savefig('chart_9.png')
    plt.show()
    st.pyplot()
    with open('chart_9.png', "rb") as img:
        button = st.sidebar.download_button(label = "Скачать текущий график",
                                            data = img,
                                            mime = "image/png")


st.write("""### 10. Построй тепловую карту зависимостей численных переменных""")
button_11 = st.button("Построить тепловую карту")
if button_11:
    tips['tip'] = tips['tip'].astype(float)
    tips['total_bill'] = tips['total_bill'].astype(float)
    tips['size'] = tips['size'].astype(int)
    tips_corr = tips[['total_bill', 'tip', 'size']]
    correlation_matrix = tips_corr.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.savefig('chart_10.png')
    plt.show()
    st.pyplot()
    with open('chart_10.png', "rb") as img:
        button = st.sidebar.download_button(label = "Скачать текущий график",
                                            data = img,
                                            mime = "image/png")
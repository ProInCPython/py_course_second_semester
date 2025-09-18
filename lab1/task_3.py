import pandas as pd
import matplotlib.pyplot as plt

dict_data = {"Товар":["Хот дог", "Чипсы", "Кола", "Хот дог", "Чипсы", "Кола", "Хот дог", "Чипсы", "Кола", "Кола"],
            "Цена":[50, 25, 30, 52, 27, 32, 54, None, None, 39],
            "Количество":[1, 10, 2, 3, 6, 15, -1230424, 1203103, None, 5]}

df = pd.DataFrame(dict_data)

df['Цена'] = df['Цена'].fillna(round(df['Цена'].mean(), 2))
df['Количество'] = df['Количество'].fillna(0)
df = df.drop(df[(df['Количество'] < 0) | (df['Количество'] > 100)].index)

df["Общая стоимость"] = df['Цена'] * df['Количество']
group_data = df.groupby('Товар')['Общая стоимость'].sum()
print(group_data)

ax = group_data.plot(kind='bar', figsize=(10,6), color="indigo", fontsize=10)
ax.set_alpha(0.8)
ax.set_title("Распределение выручки по товарам", fontsize=22)
ax.set_ylabel("Сумма выручки", fontsize=15)
plt.show()
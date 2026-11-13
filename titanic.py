import matplotlib.pyplot as plt # Подключаем библиотеки 
import pandas as pd
data_parquet = pd.read_parquet('titanic.parquet') # 1. Читаем parquet и сохраняем в csv
data_parquet.to_csv('titanic.csv', index=False)
data = pd.read_csv('titanic.csv') # Открываем сохраненный csv-файл для проверки
tablitsa = data.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0) # Группируем данные и переводим в проценты
tablitsa_procent = tablitsa.div(tablitsa.sum(axis=1), axis=0) * 100
tablitsa_procent.plot(kind='bar', stacked=True) # Строим диаграмму
plt.title('Статистика выживания на Титанике') # Оформляем подписи и выводим график
plt.xlabel('Класс билета')
plt.ylabel('Процент пассажиров (%)')
plt.xticks(rotation=0)
plt.legend(['Погиб', 'Спаслось'])
plt.show()

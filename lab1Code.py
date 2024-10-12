import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
/Users/Anton_1/PycharmProjects/pythonProject/venv/bin/lab1Code.py

# Зчитування даних з файлу CSV
# Змініть 'your_file.csv' на назву вашого файлу
df = pd.read_csv('/Users/Anton_1/Downloads/owid-covid-data-1.csv')

# Підрахунок сумарних значень для кожного континенту
result = df.groupby('continent')[['total_cases', 'total_deaths']].sum().reset_index()

# Розрахунок смертності у відсотках
result['Смертність у відсотках'] = (result['total_deaths'] / result['total_cases']) * 100
result['Смертність у відсотках'] = result['Смертність у відсотках'].fillna(0)  # Замінюємо NaN на 0

# Форматування виводу в консоль
print(f"{'Континент':<20} | {'Загальна кількість випадків':<35} | {'Загальна кількість смертей':<30} | {'Смертність у відсотках':<25}")
print("-" * 115)

for index, row in result.iterrows():
    print(f"{row['continent']:<20} | {row['total_cases']:<35} | {row['total_deaths']:<30} | {row['Смертність у відсотках']:<25.2f}")

# Візуалізація даних
plt.figure(figsize=(12, 6))

# Графік загальних випадків
plt.subplot(1, 3, 1)
plt.bar(result['continent'], result['total_cases'], color='skyblue')
plt.title('Total Cases by Continent')
plt.xlabel('Continent')
plt.ylabel('Total Cases')

# Графік загальних смертей
plt.subplot(1, 3, 2)
plt.bar(result['continent'], result['total_deaths'], color='salmon')
plt.title('Total Deaths by Continent')
plt.xlabel('Continent')
plt.ylabel('Total Deaths')

# Графік смертності у відсотках
plt.subplot(1, 3, 3)
plt.bar(result['continent'], result['Смертність у відсотках'], color='lightgreen')
plt.title('Mortality Rate by Continent (%)')
plt.xlabel('Continent')
plt.ylabel('Mortality Rate (%)')


# Функція для підрахунку пропусків у відсотках
def count_missing_values_percentage(df):
    total_records = len(df)
    total_cases_missing = df['total_cases'].isna().sum()
    total_deaths_missing = df['total_deaths'].isna().sum()

    # Обчислення відсотка пропусків
    total_cases_missing_percentage = (total_cases_missing / total_records) * 100
    total_deaths_missing_percentage = (total_deaths_missing / total_records) * 100

    return total_cases_missing_percentage, total_deaths_missing_percentage


# Обчислення пропусків у відсотках
total_cases_missing_percentage, total_deaths_missing_percentage = count_missing_values_percentage(df)

# Виведення результатів
print(f"Кількість пропусків у total_cases: {total_cases_missing_percentage:.2f}%")
print(f"Кількість пропусків у total_deaths: {total_deaths_missing_percentage:.2f}%")

plt.tight_layout()
plt.show()

# --------------------------------------------------------------------------------------

# Зчитуємо дані з CSV файлу
df = pd.read_csv('/Users/Anton_1/Downloads/owid-covid-data-1.csv')

# Видаляємо рядки з NaN у new_cases та new_deaths
df = df.dropna(subset=['new_cases', 'new_deaths'])

# Переконайтеся, що дані в колонках є цілочисельними
df['new_cases'] = df['new_cases'].astype(np.int64)
df['new_deaths'] = df['new_deaths'].astype(np.int64)

# Групуємо дані за континентами та обчислюємо статистики
statistics = {}
for continent in df['continent'].unique():
    continent_data = df[df['continent'] == continent]

    min_cases = continent_data['new_cases'].min()
    max_cases = continent_data['new_cases'].max()
    total_cases = continent_data['new_cases'].sum()

    min_deaths = continent_data['new_deaths'].min()
    max_deaths = continent_data['new_deaths'].max()
    total_deaths = continent_data['new_deaths'].sum()

    # Розрахунок додаткових статистик
    median_cases = continent_data['new_cases'].median()
    mean_cases = continent_data['new_cases'].mean()
    std_cases = continent_data['new_cases'].std()
    q1_cases = continent_data['new_cases'].quantile(0.25)
    q3_cases = continent_data['new_cases'].quantile(0.75)

    median_deaths = continent_data['new_deaths'].median()
    mean_deaths = continent_data['new_deaths'].mean()
    std_deaths = continent_data['new_deaths'].std()
    q1_deaths = continent_data['new_deaths'].quantile(0.25)
    q3_deaths = continent_data['new_deaths'].quantile(0.75)

    statistics[continent] = {
        'Мінімальні випадки': min_cases,
        'Максимальні випадки': max_cases,
        'Всього випадків': total_cases,
        'Медіана випадків': round(median_cases, 2),
        'Середнє випадків': round(mean_cases, 2),
        'Середнє квадратичне відхилення випадків': round(std_cases, 2),
        '1-й квартиль випадків': round(q1_cases, 2),
        '3-й квартиль випадків': round(q3_cases, 2),
        'Мінімальні смерті': min_deaths,
        'Максимальні смерті': max_deaths,
        'Всього смертей': total_deaths,
        'Медіана смертей': round(median_deaths, 2),
        'Середнє смертей': round(mean_deaths, 2),
        'Середнє квадратичне відхилення смертей': round(std_deaths, 2),
        '1-й квартиль смертей': round(q1_deaths, 2),
        '3-й квартиль смертей': round(q3_deaths, 2),
    }

# Виводимо результати
for continent, stats in statistics.items():
    print(f"Статистичні характеристики для континенту {continent}:")
    print(f"• Мінімальні випадки: {stats['Мінімальні випадки']}")
    print(f"• Максимальні випадки: {stats['Максимальні випадки']}")
    print(f"• Всього випадків: {stats['Всього випадків']}")
    print(f"• Медіана випадків: {stats['Медіана випадків']}")
    print(f"• Середнє випадків: {stats['Середнє випадків']}")
    print(f"• Середнє квадратичне відхилення випадків: {stats['Середнє квадратичне відхилення випадків']}")
    print(f"• 1-й квартиль випадків: {stats['1-й квартиль випадків']}")
    print(f"• 3-й квартиль випадків: {stats['3-й квартиль випадків']}")
    print(f"• Мінімальні смерті: {stats['Мінімальні смерті']}")
    print(f"• Максимальні смерті: {stats['Максимальні смерті']}")
    print(f"• Всього смертей: {stats['Всього смертей']}")
    print(f"• Медіана смертей: {stats['Медіана смертей']}")
    print(f"• Середнє смертей: {stats['Середнє смертей']}")
    print(f"• Середнє квадратичне відхилення смертей: {stats['Середнє квадратичне відхилення смертей']}")
    print(f"• 1-й квартиль смертей: {stats['1-й квартиль смертей']}")
    print(f"• 3-й квартиль смертей: {stats['3-й квартиль смертей']}")
    print()

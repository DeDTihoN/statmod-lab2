import numpy as np
import matplotlib.pyplot as plt

# Задана інтенсивність процесу
lambda_rate = 2  # події на одиницю часу
T = 50  # загальна тривалість моделювання

# Моделювання Пуассонівського процесу
np.random.seed(42)  # для відтворюваності результатів
interarrival_times = np.random.exponential(1 / lambda_rate, size=1000)
cumulative_times = np.cumsum(interarrival_times)
cumulative_times = cumulative_times[cumulative_times < T]

# Графік реалізації Пуассонівського процесу
plt.figure(figsize=(10, 6))
plt.step(np.concatenate([[0], cumulative_times]), np.arange(len(cumulative_times) + 1), where='post')
plt.xlabel('Час')
plt.ylabel('Кількість подій')
plt.title('Реалізація Пуассонівського процесу з інтенсивністю {}'.format(lambda_rate))
plt.grid()
plt.show()

# Гістограма часу появи заданої події (перша, друга, n-та)
n = 10
if len(cumulative_times) >= n:
    plt.figure(figsize=(10, 6))
    plt.hist(cumulative_times[:n], bins=n, alpha=0.7, color='b', edgecolor='black')
    plt.xlabel('Час появи події')
    plt.ylabel('Частота')
    plt.title(f'Гістограма часу появи перших {n} подій')
    plt.grid()
    plt.show()
else:
    print(f'Недостатньо подій для побудови гістограми перших {n} подій')

# Гістограма інтервалів між подіями
plt.figure(figsize=(10, 6))
plt.hist(interarrival_times[:len(cumulative_times)], bins=20, alpha=0.7, color='g', edgecolor='black')
plt.xlabel('Інтервал між подіями')
plt.ylabel('Частота')
plt.title('Гістограма інтервалів між подіями')
plt.grid()
plt.show()

# Гістограма появи рівно n подій за певний час
num_simulations = 10000
n = 100
counts = []
for _ in range(num_simulations):
    interarrival_times_sim = np.random.exponential(1 / lambda_rate, size=1000)
    cumulative_times_sim = np.cumsum(interarrival_times_sim)
    counts.append(np.sum(cumulative_times_sim < T))

counts = np.array(counts)
plt.figure(figsize=(10, 6))
plt.hist(counts, bins=np.arange(counts.min(), counts.max() + 1) - 0.5, alpha=0.7, color='r', edgecolor='black')
plt.xlabel('Кількість подій за час T')
plt.ylabel('Частота')
plt.title(f'Гістограма появи рівно {n} подій за час T={T}')
plt.grid()
plt.show()